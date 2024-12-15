import logging
from typing import List, Union
import p_data_structures as pds
import ast_parse
import p_utils
import p_consts


logger = logging.getLogger(__name__)


class TemplateTree(pds.PirelTree):
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

  def get_problematic_node(self) -> 'pds.PirelNode':
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
    def visit_fn(node: pds.PirelNode):
      print('~~~ node_type =', node.get_type())
      print('~~~ node_id =', node.get_id())
      print('~~~ node_text:')
      print(node.get_text())
      print()
    def visit_fn_2(node: pds.PirelNode):
      print(node)
      print()
    self._pre_order(self.root_node, visit_fn_2)
    print('~~~ root_node:', self.get_root_node())
    print('~~~ problematic_node:', self.get_problematic_node())

  def _count_leading_spaces(self, text: str) -> int:
      return len(text) - len(text.lstrip(' '))

  def node_can_be_templatized_template_node(self, node: pds.PirelNode, template_node: pds.PirelNode) -> bool:
    '''
    Return True if `node` can be templatized
    '''

    # Rule 1: cannot templatize the template node itself
    if node == template_node:

      # this condition covers cases where problematic node already has a single terminal child
      # such as literal nodes (int, float, bool, etc.) or identifier nodes.
      # this case also appears in p_llm_val._tsp_candidate_analyze()
      if node.has_single_terminal_child():
        return True

      return False

    # Rule 2: node is terminal
    if node.is_terminal():
      return False

    # Rule 3: do not templatize built-in function names
    if self.node_contains_builtin_token(node, p_consts.TEX_UPTO_DEPTH_BUILTIN_TOKEN):
      return False

    # Rule 4: has a grammar terminal child
    if self.node_contains_grammar_terminal_child(node):
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
    if self.node_exceeds_depth_threshold(node, p_consts.TEX_TEMPLATIZATION_DEPTH_THRESHOLD_TEMPLATE_NODE):
      return True

    return False

  def node_exceeds_depth_threshold(self, node: pds.PirelNode, threshold: int) -> bool:
    '''
    check if `node` is too deep
    needed for templatizing the node

    IDEA
    Non-terminals with a single terminal child have a depth=2.
    They are templatized by default, and usually are identifiers and literals.
    '''
    return node.get_depth() > threshold

  def node_contains_builtin_token(self, node: pds.PirelNode, upto_depth: int) -> bool:
    '''
    check if `node` contains a built-in token (e.g. function name such as 'print')
    up to a certain depth
    '''

    terminals = node.get_terminals_upto_depth(upto_depth)
    for terminal in terminals:
      if terminal in p_consts.PY_BUILT_IN_FUNCTIONS:
        return True
    return False

  def node_contains_grammar_terminal_child(self, node: pds.PirelNode) -> bool:
    '''
    check if `node` contains a child that is a grammar terminal
    (e.g. brackets, parentheses, etc.)
    '''

    grammar_terminals = [child.get_type() for child in node.get_children() if child.is_grammar_terminal()]
    for gt in grammar_terminals:
      if gt in p_consts.NON_TEMPLATIZABLE_GRAMMAR_TERMINALS:
        return True
    return False

  def node_can_be_templatized_context_node(self, some_context_node: pds.PirelNode, template_node: pds.PirelNode) -> bool:
    '''
    Return True if `node` can be templatized
    '''

    if some_context_node.is_ancestor_or_itself(template_node):
      return False

    # TODO maybe should update to 'string of NT-NT-T of width 1'?
    if some_context_node.has_single_terminal_child():
      return False

    # Rule 4: has a grammar terminal child
    if self.node_contains_grammar_terminal_child(some_context_node):
      return False

    if self.node_exceeds_depth_threshold(some_context_node, p_consts.TEX_TEMPLATIZATION_DEPTH_THRESHOLD_CONTEXT_NODE):
      return True

    return False

  # implementation that relies on annotation (start, end marks)
  def get_template_dict_for_node_id(
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
    def _get_updated_template_context_nodes(template_node: pds.PirelNode, context_node: pds.PirelNode):
      ''''''
      # 1 find the path to template_node from parent_node
      rel_path = context_node.get_path_to_child(template_node)
      # 2 get the template text
      context_text = context_node.get_text()
      context_text = _remove_leading_spaces(context_text)
      # 3 parse the text as it is
      context_ast_text, context_annotation = ast_parse.parse_text_dbg(context_text, lang=lang, keep_text=True)
      context_tree = pds.PirelTree(context_ast_text, annotation=context_annotation)
      context_tree._fix_indentation()
      # 4 get updated template_node and parent_node
      # NOTE root node is always top level node (moduly in python)
      # the template_node, however, is its only child (related to rule inference)
      new_context_node = context_tree.get_root_node().get_children()[0]
      new_template_node = new_context_node.get_child_by_path(rel_path)
      return context_tree, new_template_node, new_context_node
    tree_fixed_indentation, template_node, context_node = _get_updated_template_context_nodes(template_node, context_node)

    # 2
    return_data = {}

    templatized_node_ids_template : dict = {}
    templatized_node_ids_context : dict = {}

    def _rec_collect_templatized_nodes_context_node(at_node: pds.PirelNode, template_node: pds.PirelNode, context_node: pds.PirelNode) -> None:
      '''modifies templatized_node_ids_context'''
      nonlocal templatized_node_ids_context
      if at_node == template_node:
        _rec_collect_templatized_nodes_template_node(template_node, template_node, context_node)
        return
      if self.node_can_be_templatized_context_node(at_node, template_node):
        templatized_node_ids_context[at_node.get_id()] = context_node.get_path_to_child(at_node)
        return
      for child_node in at_node.get_children():
        _rec_collect_templatized_nodes_context_node(child_node, template_node, context_node)

    def _rec_collect_templatized_nodes_template_node(at_node: pds.PirelNode, template_node: pds.PirelNode, context_node: pds.PirelNode) -> None:
      '''
      modifies templatized_node_ids_template
      '''
      nonlocal templatized_node_ids_template
      if self.node_can_be_templatized_template_node(at_node, template_node):
        templatized_node_ids_template[at_node.get_id()] = context_node.get_path_to_child(at_node)
        return
      for child_node in at_node.get_children():
        _rec_collect_templatized_nodes_template_node(child_node, template_node, context_node)

    _rec_collect_templatized_nodes_context_node(context_node, template_node, context_node)

    def _rec_templatize(
      node: pds.PirelNode,
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

    template_context_simplification = _rec_templatize(
      context_node,
      list(templatized_node_ids_context.keys()),
      p_consts.PLACEHOLDER_TEXT,
      [],
      ''
    )
    template_context_str_replace = _rec_templatize(
      context_node,
      list(templatized_node_ids_context.keys()),
      p_consts.CONTEXT_PH_TEXT,
      list(templatized_node_ids_template.keys()),
      p_consts.PLACEHOLDER_TEXT
    )
    template_context_simplification = _remove_leading_spaces(template_context_simplification)
    return_data['template_context_simplification'] = template_context_simplification
    return_data['template_context_str_replace'] = template_context_str_replace
    return_data['template_origin'] = context_node.get_text()
    return_data['templatized_node_ids'] = templatized_node_ids_template
    return_data['templatized_node_ids_context'] = templatized_node_ids_context
    return_data['problematic_node_path'] = context_node.get_path_to_child(template_node)

    return return_data


def extract_templates(
  problematic_ast: list,
  full_ast: list,
  full_ast_text: list,
  ast_annotation: dict,
  lang: str,
  contexts: List[dict],
  **kwargs
):
  '''
  IDEAS
  - Grow the context starting from the problematic node up until the root node
  - Generate 'shallow' templates

  RETURN
  templates_dict = {
    problematic_node_type: str,
    problematic_node_id: int,
    template_id: {
      template_id: int,
      template_origin: str,
      templatized_node_ids: dict,
      py_block_replaced: bool,
      context_node_type: str,
      template_origin_node_type: str,
      is_valid_template: bool,
      [error: str],
      contexts: dict
    },
    num_templates: int
  }

  templatized_node_ids = {
    node_id: path_to_node,
    ...
  }

  contexts = {

  }
  '''

  _subject_name = kwargs['subject_name']
  p_utils.log_json_time(f'{_subject_name}_problematic_ast.json', problematic_ast)
  p_utils.log_json_time(f'{_subject_name}_full_ast_text.json', full_ast_text)
  p_utils.log_json_time(f'{_subject_name}_full_ast.json', full_ast)

  # 1 instantiate a `TemplateTree` - data structure for creating templates
  problematic_node_id = problematic_ast[1]
  template_tree = TemplateTree(full_ast_text, ast_annotation, problematic_node_id)
  problematic_node = template_tree.get_problematic_node()

  # 2 instantiate templates_dict
  templates_dict = {}
  templates_dict['problematic_node_type'] = problematic_node.get_type().split('.')[1]
  templates_dict['problematic_node_id'] = problematic_node.get_id()

  # 3 loop over a context
  context_node_cursor = problematic_node
  template_id = 0
  while context_node_cursor is not None:

    # 4 filter out invalid templates
    validation_result = _validate_template(lang, full_ast_text, context_node_cursor, template_id)
    if validation_result is not None:
      templates_dict[template_id] = validation_result
      template_id += 1
      context_node_cursor = context_node_cursor.get_parent()
      continue

    # 5 get the template for the current context
    template_dict = template_tree.get_template_dict_for_node_id(problematic_node.get_id(), context_node_cursor.get_id(), lang)
    templates_dict[template_id] = {
      'template_id': template_id,
      'template_context_simplification': template_dict['template_context_simplification'],
      'template_context_str_replace': template_dict['template_context_str_replace'],
      'template_origin': template_dict['template_origin'],
      'templatized_node_ids': template_dict['templatized_node_ids'],
      'templatized_node_ids_context': template_dict['templatized_node_ids_context'],
      'problematic_node_path': template_dict['problematic_node_path'],
      'context_node_type': context_node_cursor.get_type().split('.')[1],
      'is_valid_template': True,
      'is_insert_secret_fn': does_need_secret_fn_insertion(template_dict['template_context_str_replace']),
      'contexts': parse_context_dict(contexts, template_id),
    }
    template_id += 1
    context_node_cursor = context_node_cursor.get_parent()

    # TODO break for now, save only the first valid template
    break

  templates_dict['num_templates'] = template_id
  return templates_dict


def _validate_template(
  lang: str,
  full_ast_text: list,
  context_node: pds.PirelNode,
  template_id: int
) -> Union[dict, None]:
  '''
  Validate template.
  Return None if template is valid, dict otherwise.
  '''

  reference_tree_full = pds.PirelTree(full_ast_text)
  reference_tree_full._fix_indentation()

  reference_template_node = reference_tree_full.get_node_with_id(context_node.get_id())
  reference_template_text = reference_template_node.get_text()

  if p_utils.does_have_parse_error(reference_template_text, lang):
    return {
      'template_id': template_id,
      'template_origin': reference_template_text,
      'context_node_type': context_node.get_type(),
      'template_origin_node_type': None,
      'is_valid_template': False,
      'error': 'parse error of template_origin'
    }

  reference_template_ast_text, _ = ast_parse.parse_text_dbg(reference_template_text, lang, keep_text=True)
  reference_template_tree = pds.PirelTree(reference_template_ast_text)

  error = None
  template_origin_node_type = reference_template_node.get_type()

  if p_utils.does_have_parse_error(reference_template_text, lang):
    error = 'template origin has a parse error when parsed as it is'
  elif len(reference_template_tree.get_root_node().get_children()) > 1:
    error = 'template origin contains multiple nodes'
  elif not context_node.is_type_isomorphic_to(reference_template_tree.get_root_node().get_children()[0]):
    error = 'template origin is not type-isomorphic to the context node'
    template_origin_node_type = reference_template_tree.get_root_node().get_children()[0].get_type()

  # template is good
  if error is None:
    return None

  return {
    'template_id': template_id,
    'template_origin': reference_template_text,
    'context_node_type': context_node.get_type(),
    'template_origin_node_type': template_origin_node_type,
    'is_valid_template': False,
    'error': error
  }


# TODO consider refactoring this function
def parse_context_dict(
  contexts: List[dict],
  template_id: int
) -> list:
  '''
  '''
  template_contexts = []
  for context in contexts:
    source_context = context['source_context']
    target_context = context['target_context']
    source_context_per_trans_rule = context['scptr']
    target_context_per_trans_rule = context['tcptr']

    source_context_prev_siblings = [] if template_id == 0 else source_context[0][1:]
    target_context_prev_siblings = [] if template_id == 0 else target_context[0][1:]

    # source_context_parents = list(map(lambda x: x[0], source_context[1:1+template_id]))
    # target_context_parents = list(map(lambda x: x[0], target_context[1:1+template_id]))
    source_context_parents = []
    target_context_parents = []

    # TODO consider refactoring this block of code
    # The following block of code is an upgrade to the way how
    # source_context_parents and target_context_parents are built.
    # The problem it solves is the following: sometimes translation rules have
    # match and expand patterns of different lengths (e.g. cond.expr -> parent.expr-cond.expr)
    # This messes up parent contexts if we blindly slice the context list.
    # The solution uses a custom data structure from grammar_expand.TransSession.pirel_get_contexts_for_slot()
    if template_id != 0:
      num_source_parents_added = 0
      flag_outer_loop = True
      for sceptr, tceptr in zip(source_context_per_trans_rule[1:], target_context_per_trans_rule[1:]):
        if not flag_outer_loop:
          break
        # both should be parent
        # NOTE what if corresponding elements are not both parents, but one of them?
        if not (sceptr[0] == 'parent' and tceptr[0] == 'parent'):
          continue
        for e in sceptr[1]:
          source_context_parents.append(e[0])
          num_source_parents_added += 1
          if num_source_parents_added >= template_id:
            flag_outer_loop = False
            break
        for e in tceptr[1]:
          target_context_parents.append(e[0])
          # NOTE do we need to count number of parents added in target context?


    template_contexts.append({
      'source_context': {'siblings': source_context_prev_siblings, 'parents': source_context_parents},
      'target_context': {'siblings': target_context_prev_siblings, 'parents': target_context_parents},
    })

  return template_contexts


# TODO consider refactoring this function
def does_need_secret_fn_insertion(template: str) -> bool:
  '''
  NOTE current implementation is written with Python source code in mind.
  For other languages we may need different implementation.
  '''
  def _count_leading_spaces(text: str) -> int:
    return len(text) - len(text.lstrip(' '))
  def _get_indentations_set(lines: List[str]) -> List[int]:
    return list(set(map(_count_leading_spaces, lines)))
  lines = template.split('\n')
  # NOTE very sketchy
  lines = [line for line in lines if 'pirel_context_hole' not in line and '__' in line]
  # assert len(lines) > 0
  if len(lines) == 1:
    return False
  if len(_get_indentations_set(lines)) > 1:
    return True
  return False
