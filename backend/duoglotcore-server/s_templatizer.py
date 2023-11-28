'''
Module for generating templates from ASTs.
author: @satbekmyrza

INV1: lang in ['py', 'js']
'''


from typing import List, Union, Callable, Dict
import json
import sys
import s_consts
from s_data_structures import *
import s_parse_utils
import s_grammar
import ast_parse


# ~~~ for debugging, can be removed later
import debugpy
def _breakpoint():
  debugpy.listen(('0.0.0.0', 4444))
  debugpy.wait_for_client()
  debugpy.breakpoint()


PLACEHOLDER_TEXT = '__'  # string representation of a hole


class TemplateTree(PirelTree):
  '''
  Features:
  1. It is formed only from the full AST
  2. It accepts a problematic node id and marks the respective
     node in the Tree as problematic. This is accomplished based
     on the fact that sub-AST is a child of full AST and has the
     same node_id's for the corresponding nodes.
  3. It allows configurable templatization. That is, any node can
     be templatized.
  4. It allows Tree reduction/simplification:
     To make more compact templates (e.g. with function bodies of
     arbitrary size to be replaced with smaller statements)
  '''

  def __init__(
    self,
    full_ast_text: list,
    annotation: dict,
    problematic_node_id: int,
  ) -> None:
    '''
    full_ast_text: Pirel-style AST of the full program
    problematic_node_id: id of problematic node

    full_ast_text:
    Complete AST with pretty-print ready text.
      grammar:
      Node: [type_text, id, Node+] || str
      type_text: [type, text]
      id: int
    '''

    super().__init__(full_ast_text, annotation=annotation)

    assert isinstance(full_ast_text, list)
    assert isinstance(problematic_node_id, int)

    problematic_node_ref = self.get_node_with_id(problematic_node_id)
    assert problematic_node_ref is not None, 'cannot find a problematic node with given problematic AST'
    self.problematic_node = problematic_node_ref

  def get_problematic_node(self) -> 'PirelNode':
    return self.problematic_node

  def get_copy_with_fixed_indentation(self):
    '''
    return a copy instead of mutating self
    NOTE self.full_ast_text is available from superclass
    '''
    tree = TemplateTree(
      self.full_ast_text,
      self.annotation,
      self.problematic_node.get_id()
    )
    tree._fix_indentation()
    return tree

  def debug_print(self):
    def visit_fn(node: PirelNode):
      print('~~~ node_type =', node.get_type())
      print('~~~ node_id =', node.get_id())
      print('~~~ node_text:')
      print(node.get_text())
      print()
    def visit_fn_2(node: PirelNode):
      print(node)
      print()
    self._pre_order(self.root_node, visit_fn_2)
    print('~~~ root_node:', self.get_root_node())
    print('~~~ problematic_node:', self.get_problematic_node())

  def _count_leading_spaces(self, text: str) -> int:
      return len(text) - len(text.lstrip(' '))

  def v1_get_template_for_node_id_fluid_ids(self, parent_node_id: int, node_id: int) -> dict:
    '''
    A different implementation for getting a template where
    templatized_node_ids in template are relative to the template itself
    as if it is a program on its own.
    This is needed because of how rule inference works.
    '''

    # TODO move out of this method
    def _remove_leading_spaces_update_bounds(text: str, start_idx: int, end_idx: int) -> str:
      '''
      remove equal number of leading spaces from all lines in `text` until possible
      while at the same time updating the bounds
      '''
      # 1 count number of spaces to trim from the left
      lines = text.split('\n')
      num_spaces_to_remove = min([self._count_leading_spaces(line) for line in lines])

      # 2 split the text into segments
      pre_segment = text[:start_idx]
      segment = text[start_idx:end_idx]
      post_segment = text[end_idx:]

      # 3 do the pre segment, removing spaces shifts the entire bounded region
      # NOTE segment may start with leading spaces, and may not
      pre_segment_lines = pre_segment.split('\n')
      pre_segment_lines_trimmed = []
      for pre_segment_line in pre_segment_lines:
        if pre_segment_line.startswith(' ' * num_spaces_to_remove):
          pre_segment_lines_trimmed.append(pre_segment_line[num_spaces_to_remove:])
          start_idx -= num_spaces_to_remove
          end_idx -= num_spaces_to_remove
        else:
          pre_segment_lines_trimmed.append(pre_segment_line)
      pre_segment_trimmed = '\n'.join(pre_segment_lines_trimmed)

      # 4 do the segment, removing spaces shift only the end_idx
      # NOTE segment may start with leading spaces, and may not
      segment_lines = segment.split('\n')
      segment_lines_trimmed = []
      for segment_line in segment_lines:
        if segment_line.startswith(' ' * num_spaces_to_remove):
          segment_lines_trimmed.append(segment_line[num_spaces_to_remove:])
          end_idx -= num_spaces_to_remove
        else:
          segment_lines_trimmed.append(segment_line)
      segment_trimmed = '\n'.join(segment_lines_trimmed)

      # 5 do the post segment, it has no effect on the bounded region
      # NOTE segment may start with leading spaces, and may not
      post_segment_lines = post_segment.split('\n')
      post_segment_lines_trimmed = []
      for post_segment_line in post_segment_lines:
        if post_segment_line.startswith(' ' * num_spaces_to_remove):
          post_segment_lines_trimmed.append(post_segment_line[num_spaces_to_remove:])
        else:
          post_segment_lines_trimmed.append(post_segment_line)
      post_segment_trimmed = '\n'.join(post_segment_lines_trimmed)

      # 6 return data
      return pre_segment_trimmed + segment_trimmed + post_segment_trimmed, start_idx, end_idx

    def _remove_leading_spaces(text: str) -> str:
      '''remove equal number of leading spaces from all lines in `text` until possible'''
      lines = text.split('\n')
      num_spaces_to_remove = min([self._count_leading_spaces(line) for line in lines])
      return '\n'.join([line[num_spaces_to_remove:] for line in lines])

    tree_fixed_indentation = self.get_copy_with_fixed_indentation()

    template_node = tree_fixed_indentation.get_node_with_id(node_id)
    parent_node = tree_fixed_indentation.get_node_with_id(parent_node_id)

    # sanity check
    assert template_node is not None, f'Node (template) with node_id={node_id} is not found.'
    assert parent_node is not None, f'Node (parent) with node_id={node_id} is not found.'
    assert parent_node.is_ancestor_or_itself(template_node), 'The node to be templatized should be descendant of parent node or itself'

    # 1 find bounds of template node within parent node (with fixed indentation)
    # NOTE bug: infinite loop for L0004 `py.type[float]` in `py.func_def`
    # the bug is fixed with a different implementation `_find_bounds_v2()`
    # this function can be removed later on, keeping it for reference
    def _find_bounds(outer_node: PirelNode, search_node: PirelNode):
      assert outer_node.is_ancestor_or_itself(search_node)
      search_start_idx = 0
      outer_cursor = outer_node
      while True:
        search_cursor = search_node
        if outer_cursor.get_id() == search_cursor.get_id():
          break
        outer_text = outer_cursor.get_text()
        search_text = search_cursor.get_text()
        times = outer_text.count(search_text)
        assert times >= 1, f'this should not happen, debugging needed: {outer_node.get_id()}, {search_node.get_id()}'
        # this loop increases the inner search node
        while times != 1:
          search_cursor = search_cursor.get_parent()
          search_text = search_cursor.get_text()
          times = outer_text.count(search_text)
          assert times >= 1, 'this should not happen, debugging needed'
        search_start_idx += outer_text.index(search_text)
        outer_cursor = search_cursor
      return search_start_idx, search_start_idx + len(search_node.get_text())

    def _find_bounds_v2(outer_node: PirelNode, search_node: PirelNode):
      '''
      this is the second way to find the boundary of search_node inside outer_node
      IDEA
      1. find nodes within `outer_node` that have the same text as `search_node` -> _N
      2. from _N, select a node that has the same node_id as `search_node` -> _node
      3. remember the order of _node within _N, this order is the same as string search
      '''
      def __rec_search(outer_node: PirelNode, search_node_text: str) -> None:
        nonlocal _N
        if outer_node.get_text() == search_node_text:
          _N.append(outer_node)
          return
        for child in outer_node.get_children():
          __rec_search(child, search_node_text)

      assert outer_node.is_ancestor_or_itself(search_node)
      outer_text = outer_node.get_text()
      search_text = search_node.get_text()
      assert outer_text.count(search_text) >= 1, 'this should not happen, debugging needed'

      # base case: search_node.get_text() appears only once in outer_node.get_text()
      if outer_text.count(search_text) == 1:
        search_start_idx = outer_text.index(search_text)
        search_end_idx = search_start_idx + len(search_text)
        return search_start_idx, search_end_idx

      _N = []
      __rec_search(outer_node, search_node.get_text())
      search_idx = _N.index(search_node)
      search_start_idx = 0
      search_end_idx = 0
      for i in range(search_idx + 1):
        search_start_idx = outer_text.index(search_text, search_end_idx)
        search_end_idx = search_start_idx + len(search_text)
      return search_start_idx, search_end_idx

    # start_idx, end_idx = _find_bounds(parent_node, template_node)
    start_idx, end_idx = _find_bounds_v2(parent_node, template_node)

    # 2 at this point we have
    # - the parent node text as if it was a program on its own
    # - bounds of the template node within the parent node
    # parse the text of the parent node
    parent_text, start_idx, end_idx = _remove_leading_spaces_update_bounds(parent_node.get_text(), start_idx, end_idx)
    # NOTE hard-coded to python
    parent_ast_text, _ = ast_parse.parse_text_dbg_keep_text(parent_text, 'py')
    parent_tree = PirelTree(parent_ast_text)
    parent_tree._fix_indentation()
    candidate_template_nodes = parent_tree.get_nodes_by_bounds(start_idx, end_idx)
    nt_nodes = list(filter(lambda node: node.is_nonterminal(), candidate_template_nodes))
    assert len(nt_nodes) > 0, f'something is wrong, debugging needed: {parent_node_id}, {node_id}'
    # node with the higher node_id is the one that is smaller
    new_template_node = max(nt_nodes, key=lambda node: node.get_id())

    # 3 the template node is known
    template_tree = TemplateTree(parent_ast_text, new_template_node.get_id())
    return template_tree.v1_get_template_for_problematic_node()

  def v1_get_template_for_problematic_node(self) -> dict:
    return self.v1_get_template_for_node_id(self.root_node.get_id(), self.problematic_node.get_id())

  def v1_get_template_for_node_id(self, parent_node_id: int, node_id: int) -> dict:
    '''
    Given a parent_node_id, node_id,
    return a template rooted at parent_node_id with node_id templatized
    PRE1: node_id is sub-node of parent_node_id

    TEMPLATABLE NODES
    1. All nodes that have a single terminal child
      EXCEPT cases where the parent of the node is `call`
      e.g. (call (identifier "enumerate") (argument_list (...)))
    refer to `PirelNode._PY_can_be_templatized()`

    FORMATTING
    Rely on `.text` attribute of Tree-sitter Node class for pretty-printing.

    TERMS
    template_node: node that should be templatized
    parent_node: ancestor of template_node, which is a larger tree or template_node itself.

    RETURN FORMAT
    data {
      template: <template>,
      py_block_replaced: <bool>
    }
    '''
    def _reduce_template_replace_block_with_secret(parent_node: 'PirelNode', template_node: 'PirelNode') -> bool:
      '''
      Replace a `py.block` node with secret function call at a specific location in `parent_node`

      The corresponding function that reduces the generated rule is
      `replace_secret_with_placeholder`

      TERMS
      parent_node: the root of template
      template_node: a node that will be templatized

      PRE1: is_ancestor(parent_node, template_node)
      PRE2: parent_node is not None
      PRE3: template_node is not None

      Returns True if `py.block` is replaced with secret function call, False otherwise.

      NOTE this is a Python-specific function.
      '''

      def _build_function_call_ast_PY(function_name: str) -> 'NTTextNode':
        '''
        Builds a Python-specific AST for a function call.
        Returns root of the generated AST.

        NOTE sets the node_id's to -1 for all nodes.
        NOTE need to set a parent for the returned node
        NOTE need to adjust the indentation (leading spaces) for text attribute

        (py.call               NT1
          (py.identifier       NT2
            "set"              T3
          )
          (py.argument_list    NT4
            "("                T5
            ")"                T6
          )
        )
        '''
        NT1 = NTTextNode("py.call", None, f"{function_name}()", -1)
        NT2 = NTTextNode("py.identifier", NT1, f"{function_name}", -1)
        NT1.add_child(NT2)
        T3 = TTextNode(f"{function_name}", NT2, f"{function_name}")
        NT2.add_child(T3)
        NT4 = NTTextNode("py.argument_list", NT1, "()", -1)
        NT1.add_child(NT4)
        T5 = TTextNode("(", NT4, "(")
        NT4.add_child(T5)
        T6 = TTextNode(")", NT4, ")")
        NT4.add_child(T6)
        return NT1

      # base case parent_node is template_node
      if parent_node.get_id() == template_node.get_id():
        return False

      # 1 identify all candidate nodes (py.block nodes) that can be replaced
      all_candidate_nodes : List[PirelNode] = []
      visited_template_node = False
      def _visit_identify_replaceable_PY(node: 'PirelNode'):
        if node.is_terminal():
          return
        nonlocal all_candidate_nodes
        nonlocal visited_template_node
        nonlocal template_node
        if node.get_id() == template_node.get_id():
          visited_template_node = True
        # skip all nodes that come before template_node in pre-order traversal
        if not visited_template_node:
          return
        # collect the node if its type is `py.block`
        if node.get_type() == 'py.block':
          all_candidate_nodes.append(node)
      self._pre_order(parent_node, _visit_identify_replaceable_PY)
      # no `py.block`s, nothing to replace
      if len(all_candidate_nodes) == 0:
        return False

      # 2 select a single candidate node
      # IDEA: node_id of an ancestor node is smaller
      # PRE: there IS a single candidate node that is an ancestor of all other nodes
      # TODO this precondition might be restrictive in the future
      # TODO fix this (debugging example L0017 with problematic node ```n = len(digits)```)
      ancestor_reducible_node = max(all_candidate_nodes, key=lambda x: -x.get_id())
      all_candidate_nodes_are_children_of_ancestor = all([ancestor_reducible_node.is_ancestor_or_itself(_node) for _node in all_candidate_nodes])
      if not all_candidate_nodes_are_children_of_ancestor:
        return False
      assert all_candidate_nodes_are_children_of_ancestor, 'all candidate nodes have to be children of a single ancestor node'

      # 3 replace all children of `ancestor_reducible_node` with secret node
      secret_function_call_node = _build_function_call_ast_PY(s_consts.SECRET_FUNCTION_NAME)
      ancestor_reducible_node.set_children([secret_function_call_node])
      secret_function_call_node.set_parent(ancestor_reducible_node)

      # 4 update texts (needed for template_origin)
      # 4.1 first iteration is manual
      cursor_node = ancestor_reducible_node.get_children()[0]
      old_parent_text = cursor_node.get_parent().get_text()
      num_leading_spaces = len(old_parent_text) - len(old_parent_text.lstrip(' '))
      new_parent_text = ' ' * num_leading_spaces + secret_function_call_node.get_text()

      cursor_node = cursor_node.get_parent()
      cursor_node.set_text(new_parent_text)
      # 4.2 next iterations are looped
      while cursor_node.get_parent() is not None:
        old_current_node_text = old_parent_text
        old_parent_text = cursor_node.get_parent().get_text()
        new_parent_text = old_parent_text.replace(old_current_node_text, new_parent_text)
        cursor_node.get_parent().set_text(new_parent_text)
        cursor_node = cursor_node.get_parent()

      # 5 adjust the node_id's
      next_id = 0
      def _visit_adjust_id(node: 'PirelNode') -> None:
        if node.is_terminal():
          return
        nonlocal next_id
        if node.get_id() is not None:
          assert isinstance(node.get_id(), int)
          node.set_id(next_id)
          next_id += 1
      self._pre_order(parent_node.get_root_node(), _visit_adjust_id)

      # we have replaced py.block with secret function call -> return True
      return True

    global PLACEHOLDER_TEXT

    return_data = {}

    tree_fixed_indentation = self.get_copy_with_fixed_indentation()

    template_node = tree_fixed_indentation.get_node_with_id(node_id)
    parent_node = tree_fixed_indentation.get_node_with_id(parent_node_id)

    # sanity check
    assert template_node is not None, f'Node (template) with node_id={node_id} is not found.'
    assert parent_node is not None, f'Node (parent) with node_id={node_id} is not found.'
    assert parent_node.is_ancestor_or_itself(template_node), 'The node to be templatized should be descendant of parent node or itself'

    # this is a location where secret node insertion should be performed
    # TODO parametrized reduction?
    py_block_replaced = _reduce_template_replace_block_with_secret(parent_node, template_node)
    return_data['py_block_replaced'] = py_block_replaced

    def _remove_leading_spaces(text: str) -> str:
      '''remove equal number of leading spaces from all lines in `text` until possible'''
      lines = text.split('\n')
      num_spaces_to_remove = min([self._count_leading_spaces(line) for line in lines])
      return '\n'.join([line[num_spaces_to_remove:] for line in lines])

    def _rec_templatize(node: PirelNode) -> str:
      nonlocal templatized_node_ids
      # base cases
      if node._PY_can_be_templatized():
        templatized_node_ids.append(node.get_id())
        return PLACEHOLDER_TEXT
      if node.is_terminal():
        return node.get_text()
      # TODO parametrize this: recurse down to block or not. current is NOT.
      if node.get_type() == 'py.block':
        return node.get_text()

      node_text = node.get_text()
      node_template = ''

      first_child = node.children[0]
      first_child_text = first_child.get_text().lstrip(' ')
      first_child_template = _rec_templatize(first_child)
      node_template += ' ' * self._count_leading_spaces(node_text)
      node_template += first_child_template.lstrip(' ')
      prev_children_lens = self._count_leading_spaces(node_text) + len(first_child_text)

      for subs_child in node.get_children()[1:]:
        subs_child_text = subs_child.get_text()
        subs_child_begin_idx = node_text.index(subs_child_text, prev_children_lens)
        subs_child_template = _rec_templatize(subs_child)
        skipped_text = node_text[prev_children_lens:subs_child_begin_idx]
        node_template += skipped_text
        node_template += subs_child_template
        prev_children_lens += len(subs_child_text) + len(skipped_text)

      return node_template

    def _rec_templatize_relative_to(fixed_node: PirelNode, relative_node: PirelNode) -> str:
      '''
      TERMS
      fixed_node: a node which will be templatized
      relative_node: node in which fixed_node is sub-ast. relative_node is not templatized
      '''
      if id(fixed_node) == id(relative_node):
        return _rec_templatize(fixed_node)
      if relative_node.is_terminal():
        return relative_node.get_text()

      rel_node_text = relative_node.get_text()
      rel_node_template = ''

      rel_first_child = relative_node.children[0]
      rel_first_child_text = rel_first_child.get_text().lstrip(' ')
      rel_first_child_template = _rec_templatize_relative_to(fixed_node, rel_first_child)
      rel_node_template += ' ' * self._count_leading_spaces(rel_node_text)
      rel_node_template += rel_first_child_template.lstrip(' ')
      rel_prev_children_lens = self._count_leading_spaces(rel_node_text) + len(rel_first_child_text)

      for rel_subs_child in relative_node.get_children()[1:]:
        rel_subs_child_text = rel_subs_child.get_text()
        rel_subs_child_begin_idx = rel_node_text.index(rel_subs_child_text, rel_prev_children_lens)
        rel_subs_child_template = _rec_templatize_relative_to(fixed_node, rel_subs_child)
        rel_skipped_text = rel_node_text[rel_prev_children_lens:rel_subs_child_begin_idx]
        rel_node_template += rel_skipped_text
        rel_node_template += rel_subs_child_template
        rel_prev_children_lens += len(rel_subs_child_text) + len(rel_skipped_text)

      return rel_node_template

    templatized_node_ids : List[int] = []
    template = _rec_templatize_relative_to(template_node, parent_node)
    template = _remove_leading_spaces(template)
    return_data['template'] = template
    return_data['template_origin'] = parent_node.get_text()
    return_data['templatized_node_ids'] = templatized_node_ids
    return return_data

  def v2_get_template_dict_for_node_id(
    self,
    parent_node_id: int,
    node_id: int,
  ) -> dict:
    '''
    Given a parent_node_id, node_id,
    return a template rooted at parent_node_id with node_id templatized

    PRE1: node_id is sub-node of parent_node_id

    PARAMS
    parent_node_id - id of node within self, root node of context
    node_id - id of node within self, root of templatized nodes

    IDEAS
    - Templatize all 'relevant' nodes under `node_id` within the context `parent_node_id`.
    - Templatize == replace the node text with a placeholder `__`
    - Any non-terminal node is subject to be templatized (previously it was only terminals)
    - Rely on `.text` attribute of Tree-sitter Node class for pretty-printing.

    INTERNAL
    template_node - node at node_id, root node of all nodes that will be templatized
    parent_node - node at parent_node_id, root node of context
    tree_fixed_indentation - complete copy of `self`, safe to do anything w/ it

    RETURN FORMAT
    data {
      template: <template>,
    }
    '''

    tree_fixed_indentation = self.get_copy_with_fixed_indentation()

    template_node = tree_fixed_indentation.get_node_with_id(node_id)
    parent_node = tree_fixed_indentation.get_node_with_id(parent_node_id)

    # sanity check
    assert template_node is not None, f'Node (template) with node_id={node_id} is not found.'
    assert parent_node is not None, f'Node (parent) with node_id={node_id} is not found.'
    assert parent_node.is_ancestor_or_itself(template_node), 'The node to be templatized should be descendant of parent node or itself'

    # 1 extract template node as if it is a program on its own
    def _get_updated_template_parent_nodes(template_node: PirelNode, parent_node: PirelNode):
      ''''''
      # 1 find the path to template_node from parent_node
      rel_path = parent_node.get_path_to_child(template_node)

      # 2 get the template text
      template_text = parent_node.get_text()

      # 3 parse the text as it is
      template_ast_text, _ = ast_parse.parse_text_dbg_keep_text(template_text, 'py')
      template_tree = PirelTree(template_ast_text)
      template_tree._fix_indentation()

      # 4 get updated template_node and parent_node
      # NOTE root node is always top level node (moduly in python)
      # the template_node, however, is its only child (related to rule inference)
      new_parent_node = template_tree.get_root_node().get_children()[0]
      new_template_node = new_parent_node.get_child_by_path(rel_path)

      return template_tree, new_template_node, new_parent_node
    tree_fixed_indentation, template_node, parent_node = _get_updated_template_parent_nodes(template_node, parent_node)

    # 1.1 simplify the template
    # TODO automatic simplification invocation
    # simplification_result_dict = self.v2_simplify_template(tree_fixed_indentation, template_node, parent_node)

    # 1.2 manual simplification invocation
    def _reduce_template_replace_block_with_secret(parent_node: 'PirelNode', template_node: 'PirelNode') -> bool:
      '''
      Replace a `py.block` node with secret function call at a specific location in `parent_node`

      The corresponding function that reduces the generated rule is
      `replace_secret_with_placeholder`

      TERMS
      parent_node: the root of template
      template_node: a node that will be templatized

      PRE1: is_ancestor(parent_node, template_node)
      PRE2: parent_node is not None
      PRE3: template_node is not None

      Returns True if `py.block` is replaced with secret function call, False otherwise.

      NOTE this is a Python-specific function.
      '''

      def _build_function_call_ast_PY(function_name: str) -> 'NTTextNode':
        '''
        Builds a Python-specific AST for a function call.
        Returns root of the generated AST.

        NOTE sets the node_id's to -1 for all nodes.
        NOTE need to set a parent for the returned node
        NOTE need to adjust the indentation (leading spaces) for text attribute

        (py.call               NT1
          (py.identifier       NT2
            "set"              T3
          )
          (py.argument_list    NT4
            "("                T5
            ")"                T6
          )
        )
        '''
        NT1 = NTTextNode("py.call", None, f"{function_name}()", -1)
        NT2 = NTTextNode("py.identifier", NT1, f"{function_name}", -1)
        NT1.add_child(NT2)
        T3 = TTextNode(f"{function_name}", NT2, f"{function_name}")
        NT2.add_child(T3)
        NT4 = NTTextNode("py.argument_list", NT1, "()", -1)
        NT1.add_child(NT4)
        T5 = TTextNode("(", NT4, "(")
        NT4.add_child(T5)
        T6 = TTextNode(")", NT4, ")")
        NT4.add_child(T6)
        return NT1

      # base case parent_node is template_node
      if parent_node.get_id() == template_node.get_id():
        return False

      # 1 identify all candidate nodes (py.block nodes) that can be replaced
      all_candidate_nodes : List[PirelNode] = []
      visited_template_node = False
      def _visit_identify_replaceable_PY(node: 'PirelNode'):
        if node.is_terminal():
          return
        nonlocal all_candidate_nodes
        nonlocal visited_template_node
        nonlocal template_node
        if node.get_id() == template_node.get_id():
          visited_template_node = True
        # skip all nodes that come before template_node in pre-order traversal
        if not visited_template_node:
          return
        # collect the node if its type is `py.block`
        if node.get_type() == 'py.block':
          all_candidate_nodes.append(node)
      self._pre_order(parent_node, _visit_identify_replaceable_PY)
      # no `py.block`s, nothing to replace
      if len(all_candidate_nodes) == 0:
        return False

      # 2 select a single candidate node
      # IDEA: node_id of an ancestor node is smaller
      # PRE: there IS a single candidate node that is an ancestor of all other nodes
      # TODO this precondition might be restrictive in the future
      # TODO fix this (debugging example L0017 with problematic node ```n = len(digits)```)
      ancestor_reducible_node = max(all_candidate_nodes, key=lambda x: -x.get_id())
      all_candidate_nodes_are_children_of_ancestor = all([ancestor_reducible_node.is_ancestor_or_itself(_node) for _node in all_candidate_nodes])
      if not all_candidate_nodes_are_children_of_ancestor:
        return False
      assert all_candidate_nodes_are_children_of_ancestor, 'all candidate nodes have to be children of a single ancestor node'

      # 3 replace all children of `ancestor_reducible_node` with secret node
      secret_function_call_node = _build_function_call_ast_PY(s_consts.SECRET_FUNCTION_NAME)
      ancestor_reducible_node.set_children([secret_function_call_node])
      secret_function_call_node.set_parent(ancestor_reducible_node)

      # 4 update texts (needed for template_origin)
      # 4.1 first iteration is manual
      cursor_node = ancestor_reducible_node.get_children()[0]
      old_parent_text = cursor_node.get_parent().get_text()
      num_leading_spaces = len(old_parent_text) - len(old_parent_text.lstrip(' '))
      new_parent_text = ' ' * num_leading_spaces + secret_function_call_node.get_text()

      cursor_node = cursor_node.get_parent()
      cursor_node.set_text(new_parent_text)
      # 4.2 next iterations are looped
      while cursor_node.get_parent() is not None:
        old_current_node_text = old_parent_text
        old_parent_text = cursor_node.get_parent().get_text()
        new_parent_text = old_parent_text.replace(old_current_node_text, new_parent_text)
        cursor_node.get_parent().set_text(new_parent_text)
        cursor_node = cursor_node.get_parent()

      # 5 adjust the node_id's
      next_id = 0
      def _visit_adjust_id(node: 'PirelNode') -> None:
        if node.is_terminal():
          return
        nonlocal next_id
        if node.get_id() is not None:
          assert isinstance(node.get_id(), int)
          node.set_id(next_id)
          next_id += 1
      self._pre_order(parent_node.get_root_node(), _visit_adjust_id)

      # we have replaced py.block with secret function call -> return True
      return True
    py_block_replaced = _reduce_template_replace_block_with_secret(parent_node, template_node)

    # 2
    global PLACEHOLDER_TEXT
    return_data = {}
    return_data['py_block_replaced'] = py_block_replaced

    # 3 collect nodes that can be templatized
    templatized_node_ids : dict = {}
    def _rec_collect_templatized_node_ids(node: PirelNode, template_node: PirelNode, parent_node: PirelNode) -> None:
      '''
      PARAMS
      node - node that is templatized
      template_node - used for making sure that we do not templatize the template node itself
      '''
      nonlocal templatized_node_ids

      if self.v3_node_can_be_templatized_template_node(node, template_node):
        templatized_node_ids[node.get_id()] = parent_node.get_path_to_child(node)
        return

      # recurse to children
      for child_node in node.get_children():
        _rec_collect_templatized_node_ids(child_node, template_node, parent_node)
    _rec_collect_templatized_node_ids(template_node, template_node, parent_node)

    def _remove_leading_spaces(text: str) -> str:
      '''remove equal number of leading spaces from all lines in `text` until possible'''
      lines = text.split('\n')
      num_spaces_to_remove = min([self._count_leading_spaces(line) for line in lines])
      return '\n'.join([line[num_spaces_to_remove:] for line in lines])

    def _rec_templatize(node: PirelNode) -> str:
      nonlocal templatized_node_ids
      # base cases
      if node.is_terminal():
        return node.get_text()
      if node.get_id() in templatized_node_ids:
        return PLACEHOLDER_TEXT

      node_text = node.get_text()
      node_template = ''

      first_child = node.children[0]
      first_child_text = first_child.get_text().lstrip(' ')
      first_child_template = _rec_templatize(first_child)
      node_template += ' ' * self._count_leading_spaces(node_text)
      node_template += first_child_template.lstrip(' ')
      prev_children_lens = self._count_leading_spaces(node_text) + len(first_child_text)

      for subs_child in node.get_children()[1:]:
        subs_child_text = subs_child.get_text()
        subs_child_begin_idx = node_text.index(subs_child_text, prev_children_lens)
        subs_child_template = _rec_templatize(subs_child)
        skipped_text = node_text[prev_children_lens:subs_child_begin_idx]
        node_template += skipped_text
        node_template += subs_child_template
        prev_children_lens += len(subs_child_text) + len(skipped_text)

      return node_template

    def _rec_templatize_relative_to(fixed_node: PirelNode, relative_node: PirelNode) -> str:
      '''
      TERMS
      fixed_node: a node which will be templatized
      relative_node: node in which fixed_node is sub-ast. relative_node is not templatized
      '''
      if id(fixed_node) == id(relative_node):
        return _rec_templatize(fixed_node)
      if relative_node.is_terminal():
        return relative_node.get_text()

      rel_node_text = relative_node.get_text()
      rel_node_template = ''

      rel_first_child = relative_node.children[0]
      rel_first_child_text = rel_first_child.get_text().lstrip(' ')
      rel_first_child_template = _rec_templatize_relative_to(fixed_node, rel_first_child)
      rel_node_template += ' ' * self._count_leading_spaces(rel_node_text)
      rel_node_template += rel_first_child_template.lstrip(' ')
      rel_prev_children_lens = self._count_leading_spaces(rel_node_text) + len(rel_first_child_text)

      for rel_subs_child in relative_node.get_children()[1:]:
        rel_subs_child_text = rel_subs_child.get_text()
        rel_subs_child_begin_idx = rel_node_text.index(rel_subs_child_text, rel_prev_children_lens)
        rel_subs_child_template = _rec_templatize_relative_to(fixed_node, rel_subs_child)
        rel_skipped_text = rel_node_text[rel_prev_children_lens:rel_subs_child_begin_idx]
        rel_node_template += rel_skipped_text
        rel_node_template += rel_subs_child_template
        rel_prev_children_lens += len(rel_subs_child_text) + len(rel_skipped_text)

      return rel_node_template

    template = _rec_templatize_relative_to(template_node, parent_node)
    template = _remove_leading_spaces(template)
    return_data['template'] = template
    return_data['template_origin'] = parent_node.get_text()
    return_data['templatized_node_ids'] = templatized_node_ids

    return return_data

  # ~~~ entry point for template creation
  def v3_get_template_dict_for_node_id(
    self,
    template_node_id: int,
    context_node_id: int,
  ) -> dict:
    '''
    Given a parent_node_id, node_id,
    return a template rooted at parent_node_id with node_id templatized

    PRE1: node_id is sub-node of parent_node_id

    PARAMS
    parent_node_id - id of node within self, root node of context
    node_id - id of node within self, root of templatized nodes

    IDEAS
    - Templatize all 'relevant' nodes under `node_id` within the context `parent_node_id`.
    - Templatize == replace the node text with a placeholder `__`
    - Any non-terminal node is subject to be templatized (previously it was only terminals)
    - Rely on `.text` attribute of Tree-sitter Node class for pretty-printing.

    INTERNAL
    template_node - node at node_id, root node of all nodes that will be templatized
    parent_node - node at parent_node_id, root node of context
    tree_fixed_indentation - complete copy of `self`, safe to do anything w/ it

    RETURN FORMAT
    data {
      template: <template>,
    }
    '''

    tree_fixed_indentation = self.get_copy_with_fixed_indentation()

    template_node = tree_fixed_indentation.get_node_with_id(template_node_id)
    context_node = tree_fixed_indentation.get_node_with_id(context_node_id)

    # sanity check
    assert template_node is not None, f'Node (template) with node_id={template_node_id} is not found.'
    assert context_node is not None, f'Node (context) with node_id={template_node_id} is not found.'
    assert context_node.is_ancestor_or_itself(template_node), 'The node to be templatized should be descendant of context node or itself'

    def _remove_leading_spaces(text: str) -> str:
      '''remove equal number of leading spaces from all lines in `text` until possible'''
      lines = text.split('\n')
      num_spaces_to_remove = min([self._count_leading_spaces(line) for line in lines])
      return '\n'.join([line[num_spaces_to_remove:] for line in lines])

    # 1 extract template node as if it is a program on its own
    def _get_updated_template_context_nodes(template_node: PirelNode, context_node: PirelNode):
      ''''''
      # 1 find the path to template_node from parent_node
      rel_path = context_node.get_path_to_child(template_node)
      # 2 get the template text
      context_text = context_node.get_text()
      context_text = _remove_leading_spaces(context_text)
      # 3 parse the text as it is
      context_ast_text, _ = ast_parse.parse_text_dbg_keep_text(context_text, 'py')
      context_tree = PirelTree(context_ast_text)
      context_tree._fix_indentation()
      # 4 get updated template_node and parent_node
      # NOTE root node is always top level node (moduly in python)
      # the template_node, however, is its only child (related to rule inference)
      new_context_node = context_tree.get_root_node().get_children()[0]
      new_template_node = new_context_node.get_child_by_path(rel_path)
      return context_tree, new_template_node, new_context_node
    tree_fixed_indentation, template_node, context_node = _get_updated_template_context_nodes(template_node, context_node)

    # 2
    global PLACEHOLDER_TEXT
    return_data = {}

    templatized_node_ids_template : dict = {}
    templatized_node_ids_context : dict = {}

    def _rec_collect_templatized_nodes_context_node(at_node: PirelNode, template_node: PirelNode, context_node: PirelNode) -> None:
      '''modifies templatized_node_ids_context'''
      nonlocal templatized_node_ids_context
      if at_node == template_node:
        _rec_collect_templatized_nodes_template_node(template_node, template_node, context_node)
        return
      if self.v3_node_can_be_templatized_context_node(at_node, template_node):
        templatized_node_ids_context[at_node.get_id()] = context_node.get_path_to_child(at_node)
        return
      for child_node in at_node.get_children():
        _rec_collect_templatized_nodes_context_node(child_node, template_node, context_node)

    def _rec_collect_templatized_nodes_template_node(at_node: PirelNode, template_node: PirelNode, context_node: PirelNode) -> None:
      '''
      modifies templatized_node_ids_template
      '''
      nonlocal templatized_node_ids_template
      if self.v3_node_can_be_templatized_template_node(at_node, template_node):
        templatized_node_ids_template[at_node.get_id()] = context_node.get_path_to_child(at_node)
        return
      for child_node in at_node.get_children():
        _rec_collect_templatized_nodes_template_node(child_node, template_node, context_node)

    _rec_collect_templatized_nodes_context_node(context_node, template_node, context_node)

    def _rec_templatize(
      node: PirelNode,
      templatized_node_ids_context: List[int],
      placeholder_context: str,
      templatized_node_ids_template: List[int],
      placeholder_template: str,
    ) -> str:
      # base cases
      if node.is_terminal():
        return node.get_text()
      if node.get_id() in templatized_node_ids_context:
        return ' ' * self._count_leading_spaces(node.get_text()) + placeholder_context
      if node.get_id() in templatized_node_ids_template:
        return ' ' * self._count_leading_spaces(node.get_text()) + placeholder_template

      node_text = node.get_text()
      node_template = ''

      first_child = node.children[0]
      first_child_text = first_child.get_text().lstrip(' ')
      first_child_template = _rec_templatize(
        first_child,
        templatized_node_ids_context,
        placeholder_context,
        templatized_node_ids_template,
        placeholder_template,
      )
      node_template += ' ' * self._count_leading_spaces(node_text)
      node_template += first_child_template.lstrip(' ')
      prev_children_lens = self._count_leading_spaces(node_text) + len(first_child_text)

      for subs_child in node.get_children()[1:]:
        subs_child_text = subs_child.get_text()
        subs_child_begin_idx = node_text.index(subs_child_text, prev_children_lens)
        subs_child_template = _rec_templatize(
          subs_child,
          templatized_node_ids_context,
          placeholder_context,
          templatized_node_ids_template,
          placeholder_template,
        )
        skipped_text = node_text[prev_children_lens:subs_child_begin_idx]
        node_template += skipped_text
        node_template += subs_child_template
        prev_children_lens += len(subs_child_text) + len(skipped_text)

      return node_template

    template_context = _rec_templatize(
      context_node,
      list(templatized_node_ids_context.keys()),
      PLACEHOLDER_TEXT,
      [],
      ''
    )
    template_context_str_repl = _rec_templatize(
      context_node,
      list(templatized_node_ids_context.keys()),
      '<|pirel_context_hole|>',
      list(templatized_node_ids_template.keys()),
      PLACEHOLDER_TEXT
    )
    template_context = _remove_leading_spaces(template_context)
    return_data['template_context'] = template_context
    return_data['template_context_str_repl'] = template_context_str_repl
    return_data['template_origin'] = context_node.get_text()
    return_data['templatized_node_ids'] = templatized_node_ids_template
    return_data['templatized_node_ids_context'] = templatized_node_ids_context

    return return_data

  def v3_node_can_be_templatized_template_node(self, node: PirelNode, template_node: PirelNode) -> bool:
    '''
    Return True if `node` can be templatized
    '''

    # Rule 1: cannot templatize the template node itself
    if node == template_node:
      return False

    # Rule 2: node is terminal
    if node.is_terminal():
      return False

    # Rule 3: do not templatize built-in function names
    UPTO_DEPTH = 3
    if self.v3_node_contains_builtin_token(node, UPTO_DEPTH):
      return False

    # Rule 4: has a grammar terminal child
    if self.v3_node_contains_grammar_terminal_child(node):
      return False

    # Rule 5: node is a single non-terminal child of its parent
    # e.g. identifiers, literals
    if node.get_num_siblings() == 0 and node.is_nonterminal():
      return False

    # Rule 6: has terminal children
    # TODO maybe should update to 'string of NT-NT-T of width 1'?
    if node.has_single_terminal_child():
      return True

    # Rule 7: node exceeds depth threshold
    DEPTH_THRESHOLD = 2
    if self.v3_node_exceeds_depth_threshold(node, DEPTH_THRESHOLD):
      return True

    return False

  def v3_node_exceeds_depth_threshold(self, node: PirelNode, threshold: int) -> bool:
    '''
    check if `node` is too deep
    needed for templatizing the node

    IDEA
    Non-terminals with a single terminal child have a depth=2.
    They are templatized by default, and usually are identifiers and literals.
    '''
    return node.get_depth() > threshold

  def v3_node_contains_builtin_token(self, node: PirelNode, upto_depth: int) -> bool:
    '''
    check if `node` contains a built-in token (e.g. function name such as 'print')
    up to a certain depth
    '''

    terminals = node.get_terminals_upto_depth(upto_depth)
    for terminal in terminals:
      if terminal in s_consts.PY_BUILT_IN_FUNCTIONS:
        return True
    return False

  def v3_node_contains_grammar_terminal_child(self, node: PirelNode) -> bool:
    '''
    check if `node` contains a child that is a grammar terminal
    (e.g. brackets, parentheses, etc.)
    '''

    grammar_terminals = [child.get_type() for child in node.get_children() if child.is_grammar_terminal()]
    for gt in grammar_terminals:
      if gt in s_consts.NON_TEMPLATIZABLE_GRAMMAR_TERMINALS:
        return True
    return False

  def v3_node_can_be_templatized_context_node(self, some_context_node: PirelNode, template_node: PirelNode) -> bool:
    '''
    Return True if `node` can be templatized
    '''

    if some_context_node.is_ancestor_or_itself(template_node):
      return False

    # TODO maybe should update to 'string of NT-NT-T of width 1'?
    if some_context_node.has_single_terminal_child():
      return False

    DEPTH_THRESHOLD = 2
    if self.v3_node_exceeds_depth_threshold(some_context_node, DEPTH_THRESHOLD):
      return True

    return False

  # implementation that relies on annotation (start, end marks)
  def v4_get_template_dict_for_node_id(
    self,
    template_node_id: int,
    context_node_id: int,
    lang: str
  ) -> dict:
    '''
    Given a context_node_id, template_node_id,
    return a template rooted at context_node_id with template_node_id templatized

    PRE1: template_node_id is sub-node of context_node_id

    PARAMS
    context_node_id - id of node within self, root node of context
    template_node_id - id of node within self, root of templatized nodes

    IDEAS
    - Templatize all 'relevant' nodes under `template_node_id` within the context `context_node_id`.
    - Templatize == replace the node text with a placeholder `__`
    - Any non-terminal node is subject to be templatized (previously it was only terminals)
    - Rely on `.text` attribute of Tree-sitter Node class for pretty-printing.

    INTERNAL
    template_node - node at template_node_id, root node of all nodes that will be templatized
    context_node - node at context_node_id, root node of context

    RETURN FORMAT
    data {
      template: <template>,
    }
    '''

    tree_fixed_indentation = self.get_copy_with_fixed_indentation()

    template_node = tree_fixed_indentation.get_node_with_id(template_node_id)
    context_node = tree_fixed_indentation.get_node_with_id(context_node_id)

    # sanity check
    assert template_node is not None, f'Node (template) with node_id={template_node_id} is not found.'
    assert context_node is not None, f'Node (context) with node_id={template_node_id} is not found.'
    assert context_node.is_ancestor_or_itself(template_node), 'The node to be templatized should be descendant of context node or itself'

    def _remove_leading_spaces(text: str) -> str:
      '''remove equal number of leading spaces from all lines in `text` until possible'''
      lines = text.split('\n')
      num_spaces_to_remove = min([self._count_leading_spaces(line) for line in lines])
      return '\n'.join([line[num_spaces_to_remove:] for line in lines])

    # 1 extract template node as if it is a program on its own
    def _get_updated_template_context_nodes(template_node: PirelNode, context_node: PirelNode):
      ''''''
      # 1 find the path to template_node from parent_node
      rel_path = context_node.get_path_to_child(template_node)
      # 2 get the template text
      context_text = context_node.get_text()
      context_text = _remove_leading_spaces(context_text)
      # 3 parse the text as it is
      context_ast_text, context_annotation = ast_parse.parse_text_dbg_keep_text(context_text, lang=lang)
      context_tree = PirelTree(context_ast_text, annotation=context_annotation)
      context_tree._fix_indentation()
      # 4 get updated template_node and parent_node
      # NOTE root node is always top level node (moduly in python)
      # the template_node, however, is its only child (related to rule inference)
      new_context_node = context_tree.get_root_node().get_children()[0]
      new_template_node = new_context_node.get_child_by_path(rel_path)
      return context_tree, new_template_node, new_context_node
    tree_fixed_indentation, template_node, context_node = _get_updated_template_context_nodes(template_node, context_node)

    # 2
    global PLACEHOLDER_TEXT
    return_data = {}

    templatized_node_ids_template : dict = {}
    templatized_node_ids_context : dict = {}

    def _rec_collect_templatized_nodes_context_node(at_node: PirelNode, template_node: PirelNode, context_node: PirelNode) -> None:
      '''modifies templatized_node_ids_context'''
      nonlocal templatized_node_ids_context
      if at_node == template_node:
        _rec_collect_templatized_nodes_template_node(template_node, template_node, context_node)
        return
      if self.v3_node_can_be_templatized_context_node(at_node, template_node):
        templatized_node_ids_context[at_node.get_id()] = context_node.get_path_to_child(at_node)
        return
      for child_node in at_node.get_children():
        _rec_collect_templatized_nodes_context_node(child_node, template_node, context_node)

    def _rec_collect_templatized_nodes_template_node(at_node: PirelNode, template_node: PirelNode, context_node: PirelNode) -> None:
      '''
      modifies templatized_node_ids_template
      '''
      nonlocal templatized_node_ids_template
      if self.v3_node_can_be_templatized_template_node(at_node, template_node):
        templatized_node_ids_template[at_node.get_id()] = context_node.get_path_to_child(at_node)
        return
      for child_node in at_node.get_children():
        _rec_collect_templatized_nodes_template_node(child_node, template_node, context_node)

    _rec_collect_templatized_nodes_context_node(context_node, template_node, context_node)

    def _rec_templatize(
      node: PirelNode,
      templatized_node_ids_context: List[int],
      placeholder_context: str,
      templatized_node_ids_template: List[int],
      placeholder_template: str,
    ) -> str:
      ''''''
      nonlocal tree_fixed_indentation
      orig_text = node.get_text()
      templatized_node_ids = []
      templatized_node_ids.extend([(tnic, 'context') for tnic in templatized_node_ids_context])
      templatized_node_ids.extend([(tnit, 'template') for tnit in templatized_node_ids_template])
      templatized_node_ids = sorted(templatized_node_ids, reverse=True)
      for tni, tntype in templatized_node_ids:
        start_point = tree_fixed_indentation.annotation[tni][0]
        end_point = tree_fixed_indentation.annotation[tni][1]
        assert tntype in ['context', 'template']
        phtext = placeholder_context if tntype == 'context' else placeholder_template
        orig_text = orig_text[:start_point] + phtext + orig_text[end_point:]
      return orig_text

    template_context = _rec_templatize(
      context_node,
      list(templatized_node_ids_context.keys()),
      PLACEHOLDER_TEXT,
      [],
      ''
    )
    template_context_str_repl = _rec_templatize(
      context_node,
      list(templatized_node_ids_context.keys()),
      '<|pirel_context_hole|>',
      list(templatized_node_ids_template.keys()),
      PLACEHOLDER_TEXT
    )
    template_context = _remove_leading_spaces(template_context)
    return_data['template_context'] = template_context
    return_data['template_context_str_repl'] = template_context_str_repl
    return_data['template_origin'] = context_node.get_text()
    return_data['templatized_node_ids'] = templatized_node_ids_template
    return_data['templatized_node_ids_context'] = templatized_node_ids_context

    return return_data


class SubTemplateTree(PirelTree):
  '''
  This class is dedicated to creating sub-templates from templates.
  For example, consider this Python program:
  ```nums = [d for d in digits]``` (template origin)
  The template for the list_comprehension node is:
  ```nums = [__ for __ in __]```
  It is rather difficult to fill the first and second hole with the same identifier.
  So we split this template into sub-templates:
  ```nums = [__ for __ in digits]```
  ```nums = [d for d in __]```
  We generate pairs for each sub-template, learn translation rules, and merge them later.
  '''

  def __init__(self, full_ast_text) -> None:
    '''
    full_ast_text - Pirel style AST of template origin
    '''
    super().__init__(full_ast_text)
    self.full_ast_text = full_ast_text

  def get_all_sub_templates(self, templatized_node_ids: List[int]):
    '''
    Given templatized node ids of the template,
    return ALL sub-templates.

    return_data = {
      num_sub_templates: int,
      sub_template_id (int): {
        sub_template_id: int,
        template: str,
        templatized_node_ids: List[int],
        masked_token: str,
        masked_token_type: str,
        has_repeating_tokens
      }
    }

    TODO consider templatized node type, e.g. `d-2` is different from `d-n`
    so the template `d-__` cannot be filled arbitrarily, the type of the hole should be considered
    '''

    def _group_tokens(node_id_token_dict: Dict[int, Tuple[str, str]]) -> Dict[Tuple[str, str], List[int]]:
      '''Essentially reverse the dict'''
      groups = {}
      for k, v in node_id_token_dict.items():
        groups.setdefault(v, []).append(k)
      return groups

    return_data = {}

    # 1 get all tokens at templatized nodes
    terminal_tokens_at_templatized_nodes = self._get_terminal_tokens_at_templatized_nodes(templatized_node_ids)

    # 2 identify repeating and non-repeating tokens
    groups = _group_tokens(terminal_tokens_at_templatized_nodes)
    return_data['num_sub_templates'] = len(groups)

    # 3 iterate over every group (one group -> one sub-template)
    for sub_template_id, token_n_type in enumerate(groups):
      node_ids = groups[token_n_type]
      token, token_type = token_n_type
      sub_template = self._get_sub_template(node_ids)
      return_data[sub_template_id] = {
        'sub_template_id': sub_template_id,
        'template': sub_template,
        'templatized_node_ids': node_ids,
        'masked_token': token,
        'masked_token_type': token_type,
        'has_repeating_tokens': len(node_ids) > 1
      }

    return return_data

  def _get_terminal_tokens_at_templatized_nodes(self, templatized_node_ids: List[int]) -> Dict[int, str]:
    '''
    Given a list of templatized node ids, return a list of terminal tokens at each of them.

    POST: len(templatized_node_ids) == len(tokens)

    INTERNAL
    tokens = {
      templatized_node_id: Tuple[token (str), token_type (str)],
      ...
    }
    '''

    tokens = {}

    for templatized_node_id in templatized_node_ids:
      _templatized_node = self.get_node_with_id(templatized_node_id)

      _lang_dot_type = _templatized_node.get_type()
      _parts = _lang_dot_type.split('.')
      _token_type = _parts[1]

      # sanity check
      assert len(_parts) == 2
      assert _templatized_node._PY_can_be_templatized(), 'The node is not templatizable'

      tokens_at_templatized_node = self.get_terminal_tokens_at(templatized_node_id)

      # sanity check
      assert len(tokens_at_templatized_node) == 1, 'The templatized node can have only one terminal'

      tokens[templatized_node_id] = (tokens_at_templatized_node[0], _token_type)

    return tokens

  def _get_sub_template(self, templatized_node_ids: List[int]) -> str:
    '''
    Return a template by templatizing (masking) all templatized nodes whose ids are given.
    '''
    global PLACEHOLDER_TEXT

    # we don't need to touch self, because `update_terminal_token_at_templatizable_node()` is mutating method
    template_origin_tree = PirelTree(self.full_ast_text)
    for templatized_node_id in templatized_node_ids:
      template_origin_tree.update_terminal_token_at_templatizable_node(templatized_node_id, PLACEHOLDER_TEXT)
    return template_origin_tree.get_root_node().get_text()


def _test_templatization():
  '''
  Function for testing templatization: the code is used in s_extract_templates.extract_templates
  '''
  with open('temporary_full_ast_text.json') as fin:
    full_ast_text = json.loads(fin.read())
  with open('temporary_problematic_ast.json') as fin:
    problematic_ast = json.loads(fin.read())

  problematic_node_id = problematic_ast[1]
  template_tree = TemplateTree(full_ast_text, problematic_node_id)
  problematic_node = template_tree.get_problematic_node()

  return_data = {}
  return_data['problematic_node_type'] = problematic_node.get_type().split('.')[1]
  return_data['problematic_node_id'] = problematic_node.get_id()

  context_node_cursor = problematic_node
  template_id = 0  # the lower the level, the closer to the problematic node

  template_origin_tree = PirelTree(full_ast_text)
  template_origin_tree._fix_indentation()

  # loop over the context (from smallest to largest)
  while context_node_cursor is not None:

    # 1 get the original code from which template is generated
    template_origin_node = template_origin_tree.get_node_with_id(context_node_cursor.get_id())
    template_origin = template_origin_node.get_text()

    # 2 save the template_origin (temporary block of code)
    with open(f'temporary_template_origin_level_{template_id}.md', 'w') as fout:
      fout.write('```Python\n')
      fout.write(template_origin)
      fout.write('\n```')

    # 3 (filter) check template itself for parseability
    if s_parse_utils.has_parse_error(template_origin, parser=None, lang='py'):
      print(f'Skip this template origin due to parse error:\n"""\n{template_origin}\n"""', file=sys.stderr)
      return_data[template_id] = {
        'template_id': template_id,
        'template_origin': template_origin,
        'context_node_type': context_node_cursor.get_type().split('.')[1],
        'is_valid_template': False,
        'error': 'template origin has a parse error when parsed as it is',
      }
      # go up the tree in AST
      template_id += 1
      context_node_cursor = context_node_cursor.get_parent()
      continue

    # 4 (filter) check template for type-isomorphism with problematic node
    template_origin_at_cursor_ast_text, _ = ast_parse.parse_text_dbg_keep_text(template_origin, 'py')
    template_origin_at_cursor_tree = PirelTree(template_origin_at_cursor_ast_text)
    # need to check if `problematic_node` is a sub-tree of `template_origin_at_cursor_tree`
    problematic_node_is_subtree_of_template_origin = problematic_node.is_full_subtree_of(
      template_origin_at_cursor_tree.get_root_node()
    )
    # TODO this is hard-coded to Python
    # NOTE this might potentially lead to false positives (valid templates being counted as invalid) (not tested)
    if not problematic_node_is_subtree_of_template_origin:
      print(f'Skip this template origin because it is not super-tree of problematic node:', file=sys.stderr)
      print(f'"""\n{template_origin}\n"""', file=sys.stderr)
      return_data[template_id] = {
        'template_id': template_id,
        'template_origin': template_origin,
        'context_node_type': context_node_cursor.get_type(),
        'is_valid_template': False,
        'error': 'template origin is not a super-tree of problematic node',
      }
      # go up the tree in AST
      template_id += 1
      context_node_cursor = context_node_cursor.get_parent()
      continue

    # 5 get the template data
    template_data = template_tree.v1_get_template_for_node_id_fluid_ids(context_node_cursor.get_id(), problematic_node.get_id())

    # 6 get sub-templates for this template
    sub_template_ast_text, _ = ast_parse.parse_text_dbg_keep_text(template_data['template_origin'], 'py')
    sub_template_tree = SubTemplateTree(sub_template_ast_text)
    # sub_template_tree = s_templatizer.SubTemplateTree(template_origin_at_cursor_ast_text)
    sub_template_dict = sub_template_tree.get_all_sub_templates(template_data['templatized_node_ids'])

    template_info_ith_level = {
      'template_id': template_id,
      'template': template_data['template'],
      'template_origin': template_data['template_origin'],
      'templatized_node_ids': template_data['templatized_node_ids'],
      'py_block_replaced': template_data['py_block_replaced'],
      'context_node_type': context_node_cursor.get_type().split('.')[1],
      'is_valid_template': True,
      'sub_templates': sub_template_dict
    }

    return_data[template_id] = template_info_ith_level

    template_id += 1
    context_node_cursor = context_node_cursor.get_parent()  # go up the tree in AST

  return_data['num_templates'] = template_id

  with open('temporary_templates.json', 'w') as fout:
    fout.write(json.dumps(return_data))


# ~~~
def _test_templatization_v2():
  '''
  Function for testing templatization: the code is used in s_extract_templates.extract_templates

  INTERNAL
  full_ast_text
  src_grammar
  problematic_node_id
  template_tree
  problematic_node
  return_data
  context_node_cursor
  template_id
  '''
  with open('temporary_full_ast_text.json') as fin:
    full_ast_text = json.loads(fin.read())

  # 2 instantiate a `TemplateTree` - data structure for creating templates
  problematic_node_id = 7
  template_tree = TemplateTree(full_ast_text, problematic_node_id)
  problematic_node = template_tree.get_problematic_node()

  # 3 instantiate return_data
  return_data = {}
  return_data['problematic_node_type'] = problematic_node.get_type().split('.')[1]
  return_data['problematic_node_id'] = problematic_node.get_id()

  # 4
  context_node_cursor = problematic_node
  template_id = 0

  # we need this for checking the context of the template
  reference_tree = PirelTree(full_ast_text)
  reference_tree._fix_indentation()

  # 5 loop over a context
  while context_node_cursor is not None:

    # 5.1 filtering stage
    # data structures needed for filtering invalid templates
    reference_template_node = reference_tree.get_node_with_id(context_node_cursor.get_id())
    reference_template_text = reference_template_node.get_text()

    # (filter) context node has parse error when parsed as it is
    if s_parse_utils.has_parse_error(reference_template_text, parser=None, lang='py'):
      # print(f'Skip this context due to parse error:\n"""\n{reference_template_text}\n"""')
      return_data[template_id] = {
        'template_id': template_id,
        'template_origin': reference_template_text,
        'context_node_type': context_node_cursor.get_type(),
        'template_origin_node_type': reference_template_node.get_type(),
        'is_valid_template': False,
        'error': 'template origin has a parse error when parsed as it is',
      }
      template_id += 1
      context_node_cursor = context_node_cursor.get_parent()
      continue

    # (filter) context node is multiple nodes
    reference_template_ast_text, _ = ast_parse.parse_text_dbg_keep_text(reference_template_text, 'py')
    reference_template_tree = PirelTree(reference_template_ast_text)
    if len(reference_template_tree.get_root_node().get_children()) > 1:
      # print(f'Skip this context because it contains multiple children nodes:\n"""\n{reference_template_text}\n"""')
      return_data[template_id] = {
        'template_id': template_id,
        'template_origin': reference_template_text,
        'context_node_type': context_node_cursor.get_type(),
        'template_origin_node_type': reference_template_node.get_type(),
        'is_valid_template': False,
        'error': 'template origin contains multiple nodes',
      }
      template_id += 1
      context_node_cursor = context_node_cursor.get_parent()
      continue

    # (filter) context node is not type-isomorphic to itself when parsed as it is
    if not context_node_cursor.is_type_isomorphic_to(reference_template_tree.get_root_node().get_children()[0]):
      # print(f'Skip this context because it is not type-isomorphic to ...:\n"""\n{reference_template_text}\n"""')
      return_data[template_id] = {
        'template_id': template_id,
        'template_origin': reference_template_text,
        'context_node_type': context_node_cursor.get_type(),
        'template_origin_node_type': reference_template_tree.get_root_node().get_children()[0].get_type(),
        'is_valid_template': False,
        'error': 'template origin is not type-isomorphic to the context node',
      }
      template_id += 1
      context_node_cursor = context_node_cursor.get_parent()
      continue

    # 5.2 get the template for the current context
    template_dict = template_tree.v2_get_template_dict_for_node_id(context_node_cursor.get_id(), problematic_node.get_id())

    template_dict_ith_level = {
      'template_id': template_id,
      'template': template_dict['template'],
      'template_origin': template_dict['template_origin'],
      'templatized_node_ids': template_dict['templatized_node_ids'],
      'py_block_replaced': template_dict['py_block_replaced'],
      'context_node_type': context_node_cursor.get_type().split('.')[1],
      'is_valid_template': True,
      'sub_templates': None,
    }

    # 5.2 update the return_data
    return_data[template_id] = template_dict_ith_level

    # 5.3 increment the context by one level
    template_id += 1
    context_node_cursor = context_node_cursor.get_parent()

  # last
  with open('temporary_templates.json', 'w') as fout:
    fout.write(json.dumps(return_data))


def _test_sub_templatization():
  '''
  Test function for sub templatization
  '''
  template_origin = "strs = [chars[int(d) - 2] for d in digits]"
  templatized_node_ids = [6, 11, 12, 14, 15]

  full_ast_text, _ = ast_parse.parse_text_dbg_keep_text(template_origin, 'py')
  sub_template_tree = SubTemplateTree(full_ast_text)

  sub_templates_dict = sub_template_tree.get_all_sub_templates(templatized_node_ids)

  with open('temporary_sub_templates_dict.json', 'w') as fout:
    fout.write(json.dumps(sub_templates_dict))


if __name__ == '__main__':
  _test_templatization_v2()
  # _test_v2_simplify_template()
