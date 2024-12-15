'''
Module that contains data structures for manipulating DuoGlot-style and Pirel-style AST's.

These classes are used for:
- template generation and manipulation.
- checking whether LLM generated programs conform provided templates.

These classes are not used for manipulating translation rules.
For manipulating translation rules, classes in p_post_process_translation_rule.py are used.
p_post_process_translation_rule.py data structures are a bit different than DuoGlot-style AST's.
'''

from typing import Callable, List, Tuple, Union, Set
import json
import re
import grammar_dlmparser as gdp
import ast_parse


# ERROR CLASSES
class TreeConstructionError(Exception):
  '''
  This is an error that is thrown when the input AST
  for DuoGlotTree or PirelTree contains an ERROR
  node after being parsed by TreeSitter.
  '''
  def __init__(self, *args: object) -> None:
    super().__init__(*args)


# DUOGLOT-STYLE AST
class DuoGlotTree:
  '''
  Tree for DuoGlot-style AST
  '''
  def __init__(self, full_ast) -> None:
    '''raises TreeConstructionError'''
    self.full_ast = full_ast
    root_node_type, root_node_id, children_ast = self.parse_ast(full_ast)
    self.root_node = NTNode(root_node_type, None, root_node_id)
    for child_ast in children_ast:
      self._rec_construct_at(self.root_node, child_ast)

  def __str__(self) -> str:
    return str(self.tree_as_list())

  def _rec_construct_at(self, parent_node: 'NTNode', ast: Union[list, str]) -> None:
    # special treatment of string nodes in DuoGlot-style AST
    # for more info, refer to the json-formatted output of AST
    if isinstance(ast, list) and isinstance(ast[2], list) and ast[2][0] == 'anno':
      self._special_treatment_strings(parent_node, ast)
      return
    # base case: terminal node
    is_terminal = isinstance(ast, str)
    if is_terminal:
      node_type = ast.strip('"')  # terminals in ast_text come in double quotes
      node = TNode(node_type, parent_node)
      parent_node.add_child(node)
      return
    # non-terminal node
    node_type, node_id, children_ast = self.parse_ast(ast)
    node = NTNode(node_type, parent_node, node_id)
    parent_node.add_child(node)
    # recurse children
    for ast_child in children_ast:
      self._rec_construct_at(node, ast_child)

  # TODO needs refactoring for programs with complex string usage
  def _special_treatment_strings(self, parent: 'NTNode', ast: list) -> None:
    '''Treat strings specially'''
    # create the root string node
    strnode_type, strnode_id, strnode_children = self.parse_ast(ast)
    strnode = NTNode(strnode_type, parent, strnode_id)
    parent.add_child(strnode)
    # string type (i.e. b'', f'', etc) and quote type (i.e. ''', """, ', ")
    str_type = strnode_children[0][1][1].strip('"')
    quote_type = strnode_children[0][2][1][1:-1].replace('\\', '')
    # create string type node, if any (i.e. byte string or regex string, etc.)
    if str_type != '':
      str_type_node = TNode(str_type, strnode)
      strnode.add_child(str_type_node)
    # create left quote node
    left_quote_node = TNode(quote_type, strnode)
    strnode.add_child(left_quote_node)
    # create string content node and its child if not empty string
    if len(strnode_children) == 4:  # empty strings have 3 child nodes (anno, open quotes, close quotes)
      content_node_type, content_node_id, content_children = self.parse_ast(strnode_children[2])
      content_node = NTNode(content_node_type, strnode, content_node_id)
      strnode.add_child(content_node)
      # child of string content
      # TODO there should be a better way to handle string contents
      assert len(content_children) == 1
      content_child_node = TNode(content_children[0][1:-1].replace('\\', ''), content_node)
      content_node.add_child(content_child_node)
    # create right quote node
    right_quote_node = TNode(quote_type, strnode)
    strnode.add_child(right_quote_node)

  def parse_ast(self, ast: list) -> Tuple[str, int, list]:
    '''
    Given a DuoGlot-style AST, parse it and return
    node_type, node_id, children_ast as a tuple.
    '''
    # the block of code below is for sanity check:
    # we don't allow creating DuoGlotTree from `ast`
    # that contains 'ERROR' nodes when parsed by TreeSitter.
    parts = ast[0].split('.')
    assert len(parts) == 2, 'DuoGlotTree._parse_ast(): should not happen, debugging needed'
    lang_prefix, node_type_in_lang = parts[0], parts[1]
    if node_type_in_lang == 'ERROR':
      raise TreeConstructionError('Pirel._parse_ast(): cannot construct a tree with error nodes')

    return (ast[0], ast[1], ast[2:])

  def _pre_order(self, start_node: 'DuoGlotNode', visit_fn: Callable) -> None:
    def _rec_pre_order(node: 'DuoGlotNode', visit_fn: Callable):
      visit_fn(node)
      for child in node.get_children():
        _rec_pre_order(child, visit_fn)
    _rec_pre_order(start_node, visit_fn)

  def get_root_node(self):
    return self.root_node

  def get_node_with_id(self, node_id: int) -> Union['DuoGlotNode', None]:
    def _rec_search(node: DuoGlotNode, node_id: int) -> Union[DuoGlotNode, None]:
      if node.is_terminal():
        return None
      if node.get_id() == node_id:
        return node
      for child in node.get_children():
        child_res = _rec_search(child, node_id)
        if child_res is not None:
          return child_res
      return None
    return _rec_search(self.root_node, node_id)

  def get_terminal_tokens_at(self, node_id: int) -> List[str]:
    '''
    Given a node_id that belongs to the tree,
    return a list of terminal tokens in pre-order traversal.

    NOTE this method is used in s_llm_code_post_process module
    '''
    tokens = []
    def _visit_collect_tokens(node: 'DuoGlotNode'):
      nonlocal tokens
      if node.is_terminal():
        tokens.append(node.get_type())
    node = self.get_node_with_id(node_id)
    # sanity check
    assert node is not None, f'{node_id} does not belong to the tree\nTree:\n{self.debug_str()}'
    self._pre_order(node, _visit_collect_tokens)
    return tokens

  def get_terminal_tokens_at_node(self, node: 'DuoGlotNode') -> List[str]:
    '''
    Given a node_id that belongs to the tree,
    return a list of terminal tokens in pre-order traversal.

    NOTE this method is used in s_llm_code_post_process module
    '''
    tokens = []
    def _visit_collect_tokens(node: 'DuoGlotNode'):
      nonlocal tokens
      if node.is_terminal():
        tokens.append(node.get_type())
    self._pre_order(node, _visit_collect_tokens)
    return tokens

  def tree_as_list(self) -> list:
    '''
    for calculating tree edit distance
    '''
    def _pre_order(node: DuoGlotNode) -> list:
      if node.is_terminal():
        return node.get_type()
      result = [node.get_type()]
      for child in node.get_children():
        child_res = _pre_order(child)
        result.append(child_res)
      return result
    return _pre_order(self.get_root_node())

  def debug_print(self) -> None:
    def visit_fn(node: 'DuoGlotNode'):
      print('~~~ ', node)
    self._pre_order(self.root_node, visit_fn)
    print('~~~ root_node:', self.get_root_node())

  def debug_str(self) -> str:
    tree_as_str = ""
    def visit_fn(node: 'DuoGlotNode'):
      nonlocal tree_as_str
      tree_as_str += f'{str(node)}\n'
    self._pre_order(self.root_node, visit_fn)
    return tree_as_str

  @classmethod
  def from_code_str(cls, code_str: str, code_lang: str) -> 'DuoGlotTree':
    '''code_lang in ['py', 'js', ...]'''
    code_ast, _ = ast_parse.parse_text_dbg(code_str, code_lang)
    code_tree = DuoGlotTree(code_ast)
    return code_tree

class DuoGlotNode():
  def __init__(self, node_type: str, parent_node: 'DuoGlotNode') -> None:
    self.node_type = node_type
    self.parent = parent_node
    self.children : List[DuoGlotNode] = []

  def __str__(self) -> str:
    return f'node_type="{self.node_type}"'

  def is_root_node(self) -> bool:
    return self.parent is None

  def get_parent(self) -> 'DuoGlotNode':
    return self.parent

  def set_parent(self, parent_node: 'DuoGlotNode') -> None:
    self.parent = parent_node

  def add_child(self, child: 'DuoGlotNode') -> None:
    assert self.is_nonterminal(), 'can add a child to non-terminal only'
    self.children.append(child)

  def get_children(self) -> List['DuoGlotNode']:
    return self.children

  def has_parent(self) -> bool:
    return self.parent is not None

  def get_type(self) -> str:
    return self.node_type

  def is_ancestor_or_itself(self, other_node: 'DuoGlotNode') -> bool:
    '''
    Return True of `self` is an ancestor of `other_node`.
    Return True if `self == other_node`
    NOTE works only if the nodes belong to the same `DuoGlotTree`
    '''
    def _recurse(node1: 'DuoGlotNode', node2: 'DuoGlotNode') -> bool:
      '''node2 is stanionary'''
      if id(node1) == id(node2):
        return True
      for child_node in node1.get_children():
        child_res = _recurse(child_node, node2)
        if child_res:
          return True
      return False
    return _recurse(self, other_node)

  def get_path_to_child(self, child_node: 'DuoGlotNode') -> List[int]:
    '''
    Return a relative path from self to child_node
    PRE1: self is not child_node
    PRE2: self.is_ancestor_or_itself(child_node)
    '''
    assert self is not child_node
    assert self.is_ancestor_or_itself(child_node)

    def _rec_pre_order(path: List[int], node: DuoGlotNode) -> Union[None, List[int]]:
      nonlocal child_node
      if node == child_node:
        return path
      for i, nd in enumerate(node.get_children()):
        child_result = _rec_pre_order(path + [i], nd)
        if child_result is not None:
          return child_result
      return None
    path = _rec_pre_order([], self)
    assert path is not None, 'should not happen'
    return path

  def get_child_by_path(self, rel_path: List[int]) -> Union['DuoGlotNode', None]:
    '''
    Return a child node of self by a relative path
    Return None if rel_path does not exist
    '''
    try:
      child_node = self
      for child_idx in rel_path:
        child_node = child_node.get_children()[child_idx]
      return child_node
    except IndexError:
      return None

  def get_depth(self) -> int:
    '''
    depth between `self` and the furthest terminal node under `self`
    '''

    # base case
    if self.is_terminal():
      return 1
    max_depth = 0
    def _rec_update_max_depth(node: DuoGlotNode, current_depth: int) -> None:
      nonlocal max_depth
      if node.is_terminal():
        max_depth = max(max_depth, current_depth + 1)
      for child_node in node.get_children():
        _rec_update_max_depth(child_node, current_depth + 1)
    _rec_update_max_depth(self, 0)
    return max_depth

  def get_siblings(self) -> List['DuoGlotNode']:
    '''
    POST: self not in return_list
    '''
    if self.is_root_node():
      return []
    siblings = self.get_parent().get_children()[:]  # copy the references
    siblings.remove(self)
    return siblings

  def get_siblings_include_self(self) -> List['DuoGlotNode']:
    ''''''
    if not self.has_parent():
      return [self]
    return self.parent.children

  def get_siblings_to_the_left(self) -> List['DuoGlotNode']:
    ''''''
    siblings = self.get_siblings_include_self()
    self_idx = siblings.index(self)
    return siblings[:self_idx]

  def get_num_siblings(self) -> int:
    '''
    Number of siblings (excluding self)
    '''
    return len(self.get_siblings())

  def get_terminal_tokens(self, is_skip_grammar_terminal=True) -> List[str]:
    '''
    NOTE differentiates between
    grammar terminals (i.e. '-', '[', '=', etc.)
    and program terminals (i.e. literals, identifiers)
    '''
    tokens = []
    def _pre_order(node: 'DuoGlotNode') -> None:
      nonlocal tokens
      if node.is_terminal():
        if is_skip_grammar_terminal:
          # ensure that we are dealing with literal-, identifier-like terminals only
          if node.get_num_siblings() == 0:
            tokens.append(node.get_type())
        else:
          tokens.append(node.get_type())
      for child in node.get_children():
        _pre_order(child)
    _pre_order(self)
    return tokens

  def is_ast_width_1(self) -> bool:
    '''
    Starting from self and down the tree,
    return True if the width of the tree is 1 down to the T node
    return False otherwise
    '''
    cursor_node = self
    while cursor_node.is_nonterminal():
      if len(cursor_node.get_children()) != 1:
        return False
      cursor_node = cursor_node.get_children()[0]
    return True

  def has_single_terminal_child(self) -> bool:
    return len(self.children) == 1 and self.children[0].is_terminal()

  def get_num_nt_siblings(self) -> int:
    ''''''
    nt_siblings = [sibling for sibling in self.get_parent().get_children() if sibling != self and sibling.is_nonterminal()]
    return len(nt_siblings)

  def get_num_nt_children(self) -> int:
    ''''''
    nt_children = [child for child in self.get_children() if child.is_nonterminal()]
    return len(nt_children)

  def debug_str(self) -> str:
    '''return str repr of AST rooted at this node in pre-order traversal'''
    def _pre_order(node: 'DuoGlotNode'):
      result = node.get_type()
      for child in node.get_children():
        result += ' ' + _pre_order(child)
      return result
    return _pre_order(self)

  # abstract methods
  def is_terminal(self) -> bool:
    raise NotImplementedError

  def is_nonterminal(self) -> bool:
    raise NotImplementedError

  def get_id(self) -> int:
    raise NotImplementedError

  def set_id(self, node_id: int) -> None:
    raise NotImplementedError


class TNode(DuoGlotNode):
  # implementing abstract methods
  def is_terminal(self) -> bool:
    return True

  def is_nonterminal(self) -> bool:
    return False

  def get_id(self) -> int:
    raise AttributeError('Terminal nodes do not have node_id')

  def set_id(self, node_id: int) -> None:
    raise AttributeError('Terminal nodes cannot have node_id')


class NTNode(DuoGlotNode):
  # overridden methods
  def __init__(self, node_type: str, parent: DuoGlotNode, node_id: int) -> None:
    super().__init__(node_type, parent)
    self.node_id = node_id

  def __str__(self) -> str:
    return super().__str__() + f', node_id={self.node_id}'

  # implementing abstract methods
  def is_terminal(self) -> bool:
    return False

  def is_nonterminal(self) -> bool:
    return True

  def get_id(self) -> int:
    return self.node_id

  def set_id(self, new_id: int) -> None:
    self.node_id = new_id


# PIREL-STYLE AST
class PirelTree:
  '''
  Tree for Pirel-style AST
  '''
  def __init__(self, full_ast_text, annotation=None) -> None:
    '''
    PRE: `full_ast_text` does not have ERROR nodes when parsed by Tree-sitter
    annotation: second object returned from ast_parse.parse_text_dbg()
    '''
    self.full_ast_text = full_ast_text
    root_node_type, root_node_id, root_node_text, children_ast = self._parse_ast(full_ast_text)
    self.root_node = NTTextNode(root_node_type, None, root_node_text, root_node_id)
    for child_ast in children_ast:
      self._rec_construct_at(self.root_node, child_ast)
    self.annotation = annotation

  def _parse_ast(self, ast: list) -> Tuple[str, int, list]:
    '''
    Given a Pirel-style AST, parse it and return
    node_type, node_id, node_text, children_ast as a tuple.
    '''
    # the block of code below is for sanity check:
    # we don't allow creating PirelTree from `ast`
    # that contains 'ERROR' nodes when parsed by TreeSitter.
    parts = ast[0][0].split('.')
    assert len(parts) == 2, 'PirelTree._parse_ast(): should not happen, debugging needed'
    lang_prefix, node_type_in_lang = parts[0], parts[1]
    if node_type_in_lang == 'ERROR':
      raise TreeConstructionError('Pirel._parse_ast(): cannot construct a tree with error nodes')

    return (ast[0][0], ast[1], ast[0][1], ast[2:])

  def _rec_construct_at(self, parent_node: 'NTTextNode', ast_text: Union[list, str]) -> None:
    # special treatment of string nodes in DuoGlot-style AST
    # for more info, refer to the json-formatted output of AST
    if isinstance(ast_text, list) and isinstance(ast_text[2], list) and ast_text[2][0] == 'anno':
      self._special_treatment_strings(parent_node, ast_text)
      return
    # base case: terminal node
    is_terminal = isinstance(ast_text, str)
    if is_terminal:
      node_type = ast_text.strip('"')  # terminals in ast_text come in double quotes
      node = TTextNode(node_type, parent_node, node_type)
      parent_node.add_child(node)
      return
    # non-terminal node
    node_type, node_id, node_text, children_ast = self._parse_ast(ast_text)
    node = NTTextNode(node_type, parent_node, node_text, node_id)
    parent_node.add_child(node)
    # recurse children
    for ast_child in children_ast:
      self._rec_construct_at(node, ast_child)

  # TODO needs refactoring for programs with complex string usage
  def _special_treatment_strings(self, parent: 'PirelNode', ast_text: list) -> None:
    '''Treat strings specially'''
    # create the root string node
    strnode_type, strnode_id, strnode_text, strnode_children = self._parse_ast(ast_text)
    string_node = NTTextNode(strnode_type, parent, strnode_text, strnode_id)
    parent.add_child(string_node)
    # string type (i.e. b'', f'', etc) and quote type (i.e. ''', """, ', ")
    str_type = strnode_children[0][1][1].strip('"')
    quote_type = strnode_children[0][2][1][1:-1].replace('\\', '')
    # create string type node, if any (i.e. byte string or regex string, etc.)
    if str_type != '':
      str_type_node = TTextNode(str_type, string_node, str_type)
      string_node.add_child(str_type_node)
    # create left quote node
    left_quote_node = TTextNode(quote_type, string_node, quote_type)
    string_node.add_child(left_quote_node)
    # create string content node and its child if not empty string
    if len(strnode_children) == 4:  # empty strings have 3 child nodes (anno, open quotes, close quotes)
      content_node_type, content_node_id, content_node_text, content_children = self._parse_ast(strnode_children[2])
      content_node = NTTextNode(content_node_type, string_node, content_node_text, content_node_id)
      string_node.add_child(content_node)
      # child of string content
      # TODO there should be a better way to handle string contents
      assert len(content_children) == 1
      the_actual_string = content_children[0][1:-1].replace('\\', '')
      content_child_node = TTextNode(the_actual_string, content_node, the_actual_string)
      content_node.add_child(content_child_node)
    # create right quote node
    right_quote_node = TTextNode(quote_type, string_node, quote_type)
    string_node.add_child(right_quote_node)

  def _pre_order(self, start_node: 'PirelNode', visit_fn: Callable) -> None:
    def _rec_pre_order(node: 'PirelNode', visit_fn: Callable):
      visit_fn(node)
      for child in node.get_children():
        _rec_pre_order(child, visit_fn)
    _rec_pre_order(start_node, visit_fn)

  def get_root_node(self):
    return self.root_node

  def get_node_with_id(self, node_id: int) -> Union['PirelNode', None]:
    def _rec_search(node: PirelNode, node_id: int) -> PirelNode:
      if node.is_terminal():
        return None
      if node.get_id() == node_id:
        return node
      for child in node.get_children():
        child_res = _rec_search(child, node_id)
        if child_res is not None:
          return child_res
      return None
    return _rec_search(self.root_node, node_id)

  def debug_print(self) -> None:
    def visit_fn(node: 'PirelNode'):
      print('~~~ ', node)
    self._pre_order(self.root_node, visit_fn)
    print('~~~ root_node:', self.get_root_node())

  def __str__(self) -> str:
    raise NotImplementedError

  def _fix_indentation(self):
    '''
    Nested AST nodes have a broken node_text as follows:
    Regardless of the level of nestedness, first line always has zero indentation.
    This method prepends necessary indentation to the first line.
    PRE1: we assume that the root node has properly formatted node_text
    POST1: self is mutated
    '''
    def _visit_fix_indentation_at_node(node: PirelNode):
      if not node.has_parent():
        return
      is_multiline = '\n' in node.get_text()
      if not is_multiline:
        return
      parent_text = node.get_parent().get_text()
      node_text = node.get_text()
      node_text_start_idx = parent_text.index(node_text)  # NOTE be careful here
      # go left and count space characters until hit a newline character or reached the edge
      num_spaces = 0
      search_start_idx = node_text_start_idx - 1
      while parent_text[search_start_idx] != '\n' and search_start_idx >= 0:
        num_spaces += 1
        search_start_idx -= 1
      node.set_text(' ' * num_spaces + node_text)
    self._pre_order(self.root_node, _visit_fix_indentation_at_node)

  def get_nodes_by_bounds(self, start_idx, end_idx) -> List['PirelNode']:
    '''
    Given bounds in a self.root_node.node_text
    return the list of nodes that fully contain the bounds
    '''
    nodes_within_bounds = []
    def _rec_collect_nodes(node: PirelNode, start_idx: int, end_idx: int):
      nonlocal nodes_within_bounds
      node_text = node.get_text()
      # base case: self is the node
      node_start_idx = 0
      node_end_idx = len(node_text)
      # add node IFF the bounds are exact
      if node_start_idx == start_idx and node_end_idx == end_idx:
        nodes_within_bounds.append(node)
      # recurse children
      child_search_start_idx = 0
      for child in node.get_children():
        child_text = child.get_text()
        child_start_idx = node_text.index(child_text, child_search_start_idx)
        child_end_idx = child_start_idx + len(child_text)
        if start_idx >= child_start_idx and end_idx <= child_end_idx:
          # update the start_idx, end_idx relative to the child
          _rec_collect_nodes(child, start_idx - child_start_idx, end_idx - child_start_idx)
        else:
          child_search_start_idx += len(child_text)
    _rec_collect_nodes(self.root_node, start_idx, end_idx)
    return nodes_within_bounds

  def get_terminal_tokens_at(self, node_id: int) -> List[str]:
    '''
    Given a node_id that belongs to the tree,
    return a list of terminal tokens in pre-order traversal.
    '''
    tokens = []
    def _visit_collect_tokens(node: 'PirelNode'):
      nonlocal tokens
      if node.is_terminal():
        tokens.append(node.get_type())
    node = self.get_node_with_id(node_id)
    # sanity check
    assert node is not None, f'{node_id} does not belong to the tree'
    self._pre_order(node, _visit_collect_tokens)
    return tokens


class PirelNode():
  def __init__(self, node_type: str, parent_node: 'PirelNode', node_text: str) -> None:
    self.node_type = node_type
    self.parent = parent_node
    self.node_text = node_text
    self.children : List[PirelNode] = []

  def __str__(self) -> str:
    return f'node_type="{self.node_type}" node_text="{self.node_text}"'

  def get_type(self) -> str:
    return self.node_type

  def set_type(self, new_type: str) -> None:
    self.node_type = new_type

  def get_parent(self) -> 'PirelNode':
    return self.parent

  def set_parent(self, parent_node: 'PirelNode') -> None:
    self.parent = parent_node

  def get_text(self) -> str:
    return self.node_text

  def set_text(self, text: str) -> None:
    self.node_text = text

  def add_child(self, child: 'PirelNode') -> None:
    assert self.is_nonterminal(), 'can add a child only to non-terminal node'
    self.children.append(child)

  def get_children(self) -> List['PirelNode']:
    return self.children

  def set_children(self, children: List['PirelNode']) -> None:
    self.children = children

  def has_parent(self) -> bool:
    return self.parent is not None

  def is_root_node(self) -> bool:
    return self.parent is None

  def is_ancestor_or_itself(self, other_node) -> bool:
    '''
    Return True of `self` is an ancestor of `other_node`.
    Return True if `self == other_node`
    NOTE works only if the nodes belong to the same `PirelTree`
    '''
    def _recurse(node1: 'PirelNode', node2: 'PirelNode') -> bool:
      '''node2 is stanionary'''
      if id(node1) == id(node2):
        return True
      for child_node in node1.get_children():
        child_res = _recurse(child_node, node2)
        if child_res:
          return True
      return False
    return _recurse(self, other_node)

  def is_type_isomorphic_to(self, other_node: 'PirelNode') -> bool:
    '''
    Return True if self and other_node are type-isomorphic:
    1. Identical structure
    2. Corresponding non-terminal nodes have the same types

    NOTE
    1. This method is used in p_templates.extract_templates() to filter out
    invalid templates.
    2. Might be weak (take into account terminals except identifiers?)
    '''
    def _recurse(node1: 'PirelNode', node2: 'PirelNode') -> bool:
      # 1 terminalities differ in corresponding nodes -> not type-isomorphic
      if node1.is_terminal() and node2.is_nonterminal():
        return False
      if node1.is_nonterminal() and node2.is_terminal():
        return False
      # 2 both nodes are terminal
      if node1.is_terminal() and node2.is_terminal():
        return True
      # 3 both node1 and node2 are non-terminal at this point
      # 4 types are different
      if node1.get_type() != node2.get_type():
        return False
      # 5 number of children is different
      if len(node1.get_children()) != len(node2.get_children()):
        return False
      # 6 recurse children
      children_result = []
      for child1, child2 in zip(node1.get_children(), node2.get_children()):
        child_result = _recurse(child1, child2)
        children_result.append(child_result)
      return all(children_result)
    return _recurse(self, other_node)

  def is_full_subtree_of(self, other_node: 'PirelNode') -> bool:
    '''
    Return True if `self` is a sub-tree of `other_node` iff:
    1. non-terminal nodes match
    2. terminal nodes match
    3. node ids do not have to match

    NOTE this is a lazy implementation, consider optimizing
    '''
    # TODO move this function to utils module?
    def _get_full_encoding(node: PirelNode) -> str:
      def _rec_post_order(node: PirelNode):
        if isinstance(node, TTextNode):
          return node.get_type()
        children_encoding = ''
        for child in node.get_children():
          children_encoding += _rec_post_order(child) + ' '
        return f'({node.get_type()} {children_encoding[:-1]})'
      return _rec_post_order(node)

    sub_node_encoding = _get_full_encoding(self)
    super_node_encoding = _get_full_encoding(other_node)
    return sub_node_encoding in super_node_encoding

  def get_root_node(self) -> 'PirelNode':
    '''
    Return reference to the root node from arbitrary node down the tree
    '''
    cursor = self
    while cursor.has_parent():
      cursor = cursor.get_parent()
    return cursor

  def has_single_terminal_child(self) -> bool:
    return len(self.children) == 1 and self.children[0].is_terminal()

  def get_index_as_child(self) -> int:
    if self.is_root_node():
      return 0
    return self.get_parent().get_children().index(self)

  def get_siblings(self) -> List['PirelNode']:
    '''
    POST: self not in return_list
    '''
    if self.is_root_node():
      return []
    siblings = self.get_parent().get_children()[:]  # copy the references
    siblings.remove(self)
    return siblings

  def get_num_siblings(self) -> int:
    '''
    Number of siblings (excluding self)
    '''
    return len(self.get_siblings())

  def has_terminal_sibling(self) -> bool:
    '''
    As name suggests, return True if `self` has at least one terminal sibling
    Used in templatization v2
    '''
    siblings = self.get_siblings()
    return any(map(lambda node: node.is_terminal(), siblings))

  def has_terminal_child(self) -> bool:
    return any(map(lambda node: node.is_terminal(), self.get_children()))

  def get_depth(self) -> int:
    '''
    depth between `self` and the furthest terminal node under `self`
    '''

    # base case
    if self.is_terminal():
      return 1
    max_depth = 0
    def _rec_update_max_depth(node: PirelNode, current_depth: int) -> None:
      nonlocal max_depth
      if node.is_terminal():
        max_depth = max(max_depth, current_depth + 1)
      for child_node in node.get_children():
        _rec_update_max_depth(child_node, current_depth + 1)
    _rec_update_max_depth(self, 0)
    return max_depth

  def get_path_to_child(self, child_node: 'PirelNode') -> List[int]:
    '''
    Return a relative path from self to child_node
    PRE: self.is_ancestor_or_itself(child_node)
    '''
    assert self.is_ancestor_or_itself(child_node)

    def _rec_pre_order(path: List[int], node: PirelNode) -> Union[None, List[int]]:
      nonlocal child_node
      if node == child_node:
        return path
      for i, nd in enumerate(node.get_children()):
        child_result = _rec_pre_order(path + [i], nd)
        if child_result is not None:
          return child_result
      return None
    path = _rec_pre_order([], self)
    assert path is not None, 'should not happen'
    return path

  def get_node_by_id(self, node_id: int) -> List[int]:
    '''
    get a reference to a node with id node_id
    that belongs to the same tree as self
    '''
    cursor = self
    # move up to the root
    while cursor.has_parent():
      cursor = cursor.get_parent()

    def _rec_pre_order(node: PirelNode, node_id: int) -> Union[None, PirelNode]:
      ''''''
      if node.is_terminal():
        return None
      if node.get_id() == node_id:
        return node
      for child_node in node.get_children():
        child_result = _rec_pre_order(child_node, node_id)
        if child_result is not None:
          return child_result
      return None
    node = _rec_pre_order(cursor, node_id)
    assert node is not None, 'prerequisite not met, node does not exist'
    return node

  def get_child_by_path(self, rel_path: List[int]) -> Union['PirelNode', None]:
    '''
    Return a child node of self by a relative path
    PRE: rel_path exists in self
    '''
    try:
      child_node = self
      for child_idx in rel_path:
        child_node = child_node.get_children()[child_idx]
      return child_node
    except IndexError:
      return None

  def get_ast_as_list(self) -> list:
    '''
    Given a PirelNode (i.e. self), return a list representation of sub-AST
    rooted at self of a tree self belongs to.
    Returns sth similar to a full_ast_text that PirelTree was constructed from.
    '''
    def _rec_pre_order(node: PirelNode, ast_as_list: list) -> list:
      '''NOTE includes NT and T nodes'''
      ast_as_list.append(node.get_type())
      for child in node.get_children():
        child_ast_as_list = _rec_pre_order(child, [])
        ast_as_list.append(child_ast_as_list)
      return ast_as_list

    ast_as_list = _rec_pre_order(self, [])
    return ast_as_list

  def get_terminals_upto_depth(self, depth: int) -> Set[str]:
    '''
    self is at depth 1
    '''
    terminals = set()
    def _rec_pre_order(node: PirelNode, current_depth: int) -> None:
      nonlocal depth, terminals
      if current_depth > depth:
        return
      if node.is_terminal() and node.get_num_siblings() == 0:
        terminals.add(node.get_type())
        return
      for child_node in node.get_children():
        _rec_pre_order(child_node, current_depth + 1)
    _rec_pre_order(self, 1)
    return terminals

  def is_grammar_terminal(self) -> bool:
    '''
    grammar terminal - terminals that appear in grammar
    '''
    if self.is_terminal():
      if self.get_num_siblings() > 0:
        return True
    return False

  # abstract methods
  def is_terminal(self) -> bool:
    raise NotImplementedError

  def is_nonterminal(self) -> bool:
    raise NotImplementedError

  def get_id(self) -> int:
    raise NotImplementedError

  def set_id(self, node_id: int) -> None:
    raise NotImplementedError


class TTextNode(PirelNode):
  # implementing abstract methods
  def is_terminal(self) -> bool:
    return True

  def is_nonterminal(self) -> bool:
    return False

  def get_id(self) -> int:
    raise AttributeError('Terminal nodes do not have node_id')

  def set_id(self, node_id: int) -> None:
    raise AttributeError('Terminal nodes cannot have node_id')


class NTTextNode(PirelNode):
  # overridden methods
  def __init__(self, node_type: str, parent: PirelNode, node_text: str, node_id: int) -> None:
    super().__init__(node_type, parent, node_text)
    self.node_id = node_id

  def __str__(self) -> str:
    return f'node_id={self.node_id}, ' + super().__str__()

  # implementing abstract methods
  def is_terminal(self) -> bool:
    return False

  def is_nonterminal(self) -> bool:
    return True

  def get_id(self) -> int:
    return self.node_id

  def set_id(self, new_id: int) -> None:
    self.node_id = new_id


# PATTERN TREE
class PatternTree:
  '''
  A read-only tree class.

  A simplified representation of a pattern.
  That is, a fragment, rule, etc.
  Initially designed for parsing translation
  rule fragments during context extraction
  in grammar_expand.pirel_get_all_contexts().
  '''
  def __init__(self, pattern: list, lang: str) -> None:
    self.pattern = pattern
    self.lang = lang
    self.re_dotstar_num = re.compile(r'^"([\.\*])(\d+)"$')
    self.re_dotstar_only = re.compile(r'^"[\.\*]"$')
    self.dotstar_counter = 1
    root_node_type, root_children = self._parse_pattern(pattern)
    self.root_node = PatternNode(root_node_type, None)
    for child_pattern in root_children:
      self._rec_construct_at(self.root_node, child_pattern)

  def _parse_pattern(self, pattern: Union[list, str]) -> Tuple[str, Union[list, str]]:
    assert isinstance(pattern, (list, str))
    # terminal node
    if isinstance(pattern, str):
      return pattern, []
    node_type = pattern[0]
    children = pattern[1:]
    return node_type, children

  def _rec_construct_at(self, parent_node: 'PatternNode', pattern: Union[list, str]) -> None:
    node_type, children = self._parse_pattern(pattern)
    new_node = self._new_node(node_type, children, parent_node)
    parent_node.add_child(new_node)
    for child_pattern in children:
      self._rec_construct_at(new_node, child_pattern)

  def _new_node(self, node_type: str, children_pattern: list, parent_node: 'PatternNode') -> 'PatternNode':
    # NT node
    if len(children_pattern) > 0:
      new_node = PatternNode(node_type, parent_node)
      return new_node

    # T node
    dotstar_num_match = self.re_dotstar_num.match(node_type)
    if node_type in ['"."', '"*"']:
      new_node = PhNode(node_type, parent_node, self.dotstar_counter)
      self.dotstar_counter += 1
    elif dotstar_num_match:
      new_node = PhNode(node_type, parent_node, int(dotstar_num_match.group(2)))
    else:
      new_node = PatternNode(node_type, parent_node)
    return new_node

  def _pre_order(self, start_node: 'PatternNode', visit_fn: Callable) -> None:
    def _rec_pre_order(node: 'PatternNode', visit_fn: Callable):
      visit_fn(node)
      for child in node.get_children():
        _rec_pre_order(child, visit_fn)
    _rec_pre_order(start_node, visit_fn)

  def get_node_with_type(self, node_type: str) -> Union['PatternNode', None]:
    '''
    return first occurence in pre-order traversal
    intended to be looking for placeholder nodes
    NOTE target patterns may contain the same placeholders (e.g. .1, .1)
    '''
    counter = 1
    def _rec_search_counter(node: PatternNode, node_type: str) -> Union[PatternNode, None]:
      nonlocal counter
      if self.re_dotstar_num.match(node_type):
        # target pattern
        if self.re_dotstar_num.match(node.get_type()):
          if node.get_type() == node_type:
            return node
        # source pattern
        if self.re_dotstar_only.match(node.get_type()):
          if f'''"{node.get_type().strip('"')}{str(counter)}"''' == node_type:
            assert node.get_phid() == counter
            return node
          else:
            counter += 1
      for child in node.get_children():
        child_res = _rec_search_counter(child, node_type)
        if child_res is not None:
          return child_res
      return None

    return _rec_search_counter(self.root_node, node_type)

  def debug_print(self) -> None:
    def visit_fn(node: 'PatternNode'):
      print('~~~ ', node)
    self._pre_order(self.root_node, visit_fn)


class PatternNode():
  '''
  A read-only node class

  Attributes:
  - node_type
  - parent
  - children
  '''
  def __init__(self, node_type: str, parent: 'PatternNode') -> None:
    self.node_type = node_type
    self.parent = parent
    self.children : List['PatternNode'] = []
    self.re_nt = re.compile(r'^"[a-z]+\.[a-z_]+"$')  # NT, e.g. py.integer
    self.re_dotstar_num = re.compile(r'^"([\.\*])(\d+)"$')  # ".1"

  def __str__(self) -> str:
    return self.node_type

  def get_type(self) -> str:
    return self.node_type

  def add_child(self, child: 'PatternNode') -> None:
    self.children.append(child)

  def get_children(self) -> List['PatternNode']:
    return self.children

  def is_root_node(self) -> bool:
    return not self.has_parent()

  def is_terminal(self) -> bool:
    return len(self.children) == 0

  def is_nonterminal(self) -> bool:
    return not self.is_terminal()

  def has_parent(self) -> bool:
    return self.parent is not None

  def get_parent(self) -> Union['PatternNode', None]:
    return self.parent

  def has_previous_sibling(self) -> bool:
    return self.get_index_as_child() > 0

  def get_previous_sibling(self) -> Union['PatternNode', None]:
    self_idx = self.get_index_as_child()
    if self_idx == 0:
      return None
    return self.get_parent().get_children()[self_idx - 1]

  def get_index_as_child(self) -> int:
    if self.is_root_node():
      return 0
    return self.get_parent().get_children().index(self)

  def get_path_to_root_source(self, expansion: gdp.Expansion) -> list:

    def _get_path(node: PatternNode, expansion: gdp.Expansion) -> Union[str, None]:
      node_type = node.get_type()

      # regular NT node
      if self.re_nt.match(node_type):
        return node_type

      # when building path in source, should not see target PH nodes
      elif self.re_dotstar_num.match(node_type):
        raise RuntimeError('should not happen')

      # when building path in source, meet a PH node
      elif node_type in ['"."', '"*"']:
        phid = node.get_phid()
        slot_name = f'''"{node_type.strip('"') + str(phid)}"'''

        # NOTE `slot_name` may not be in `expansion.slot_names`
        # if it is not being used. That is, there might be a placeholder
        # in the source matcher that does not appear in the target matcher.
        # assert slot_name in expansion.slot_names
        if slot_name not in expansion.slot_names:
          assert node_type == '"."', 'currently works with dot placeholder only'
          return 'pirel_anynode'

        node_slot : gdp.Slot = expansion.slots[expansion.slot_names.index(slot_name)]

        slot_range_cursor = node_slot.range_cursor
        slot_child_node_ids = node_slot.slot_node_ids

        slot_ast = slot_range_cursor[0]
        slot_start_idx = slot_range_cursor[1]
        slot_end_idx = slot_range_cursor[2]

        node_ast = None
        for _cursor_idx in range(slot_start_idx, slot_end_idx):
          node_ast = slot_ast[_cursor_idx]
          if node_ast[1] in slot_child_node_ids:
            break
        assert node_ast is not None

        slot_type = node_ast[0]
        return slot_type

      return None

    path = [[]]
    cursor_node = self
    while cursor_node.has_parent():
      while cursor_node.has_previous_sibling():
        cursor_node = cursor_node.get_previous_sibling()
        cursor_path = _get_path(cursor_node, expansion)
        if cursor_path is not None:
          path[0].insert(0, cursor_path)
      cursor_node = cursor_node.get_parent()
      cursor_path = _get_path(cursor_node, expansion)
      if cursor_path is not None:
        path.insert(0, [cursor_path])
    return path

  def get_path_to_root_target(self, expansion: gdp.Expansion, slot_expand_info_dict: dict) -> list:

    def _get_path(node: PatternNode, expansion: gdp.Expansion, slot_expand_info_dict: dict) -> Union[str, None]:
      node_type = node.get_type()

      # regular NT node
      if self.re_nt.match(node_type):
        return node_type

      # when building path in target, should not see source PH nodes
      elif node_type in ['"."', '"*"']:
        raise RuntimeError('should not happen')

      # when building path in target, meet a PH node
      elif self.re_dotstar_num.match(node_type):
        slot_name = node_type
        assert slot_name in expansion.slot_names
        node_slot : gdp.Slot = expansion.slots[expansion.slot_names.index(slot_name)]
        all_expansions_node_slot = _get_slot_possible_expansions(node_slot, slot_expand_info_dict)
        assert all_expansions_node_slot is not None, 'should not happen'
        # TODO in what cases need to choose others?
        pos_exp = all_expansions_node_slot[0]
        # NOTE might do sth sophisticated here, but we just need to the name of the top-most node,
        # w/o going down the entire tree
        node_type = pos_exp.expan_fragment[1][0]
        return node_type

      return None

    def _get_slot_possible_expansions(slot: gdp.Slot, slot_expand_info_dict: dict) -> Union[List[gdp.Expansion], None]:
      '''
      return all possible expansions that might be created from this slot (down)

      might return
      1. None - in case expansions were not generated for this slot
      2. empty list - no translation rule matched for slot
      3. non-empty list - expansions
      '''

      slot_id = slot.slot_id

      # slot was created, but expansions for this slot were not
      if slot_id not in slot_expand_info_dict:
        return None

      return slot_expand_info_dict[slot_id][0]

    path = [[]]
    cursor_node = self
    while cursor_node.has_parent():
      while cursor_node.has_previous_sibling():
        cursor_node = cursor_node.get_previous_sibling()
        cursor_path = _get_path(cursor_node, expansion, slot_expand_info_dict)
        if cursor_path is not None:
          path[0].insert(0, cursor_path)
      cursor_node = cursor_node.get_parent()
      cursor_path = _get_path(cursor_node, expansion, slot_expand_info_dict)
      if cursor_path is not None:
        path.insert(0, [cursor_path])
    return path

  def get_phid(self):
    raise NotImplementedError


class PhNode(PatternNode):
  def __init__(self, node_type: str, parent: PatternNode, phid: int) -> None:
    super().__init__(node_type, parent)
    self.phid = phid

  def __str__(self) -> str:
    return super().__str__() + f' {self.phid}'

  def get_phid(self) -> int:
    return self.phid
