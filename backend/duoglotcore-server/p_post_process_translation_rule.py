'''
A module for post-processing match patterns in DuoGlot.
Match pattern is an s-expression that matches either a source program, or a target program.
Match pattern is a return value of frontend/pirel/rule_inference.js::ruleInfAPI_ns.inferTranslationRule()
Match pattern is directly pretty-printed into a translation rule.

In simple words, this module is for manipulating translation rules.
'''
# Class hierarchy:
#                                       AbstractNode
#                                         /--  --\
#                                     /---        ---\
#                                 ---                ---
#                       NonTerminalNode             TerminalNode
#                                                   /------\
#                                           /-------        -----\
#                                       ----                      ---
#                               PlainTerminalNode                  PhNode
#                                                             ------------\
#                                             ---------------/             ------\
#                                   --------/                                    ----
#                             SourcePhNode                                       TargetPhNode
#                           --------\                                           --- |----\
#               -----------/   -/    ---\                                 -----/    \     -------\
#         ------/              /          ---                          ---/           |            -----
# SourceValPhNode   SourceStrPhNode   SourceDotStarPhNode    TargetValPhNode   TargetStrPhNode   TargetDotStarPhNode

# TODO add support for (nostr) nodes


from typing import Union, Callable, List, Tuple
import json
import re


class AbstractNode:
  '''
  Abstract Node class for pattern tree node types.
  '''

  def __init__(self, node_type: str, parent: 'AbstractNode') -> None:
    '''
    node_type: e.g. 'py.identifier'
    parent: parent AbstractNode. None if self is root.
    children: List[AbstractNode].
    '''
    self.node_type : str = node_type
    self.parent : Union[AbstractNode, None] = parent
    self.children : List[AbstractNode] = []

  def get_type(self) -> str:
    return self.node_type

  def set_type(self, new_type: str) -> None:
    self.node_type = new_type

  def get_parent(self) -> Union['AbstractNode', None]:
    return self.parent

  def set_parent(self, new_parent: 'AbstractNode') -> None:
    self.parent = new_parent

  def get_children(self) -> List['AbstractNode']:
    return self.children

  def is_root_node(self) -> bool:
    return self.parent is None

  def has_parent(self) -> bool:
    return self.parent is not None

  def num_children(self) -> int:
    return len(self.children)

  def get_siblings_include_self(self) -> List['AbstractNode']:
    if not self.has_parent():
      return [self]
    return self.parent.children

  def get_siblings_to_the_left(self) -> List['AbstractNode']:
    siblings = self.get_siblings_include_self()
    self_idx = siblings.index(self)
    return siblings[:self_idx]

  def get_child_by_path(self, rel_path: List[int]) -> Union['AbstractNode', None]:
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

  def get_src_dotstar_ph_nodes_under(self) -> List['SourceDotStarPhNode']:
    ''''''
    nodes = []
    def _pre_order(node: 'AbstractNode'):
      nonlocal nodes
      if isinstance(node, SourceDotStarPhNode):
        nodes.append(node)
      for child in node.get_children():
        _pre_order(child)
    _pre_order(self)
    return nodes

  def __str__(self) -> str:
    return f'class={type(self).__name__}\n' + \
    f'type={self.node_type}\n' + \
    f'num_children={len(self.children)}'

  def debug_str(self) -> str:
    '''return str repr of AST rooted at this node in pre-order traversal'''
    def _pre_order(node: 'AbstractNode'):
      result = node.get_type()
      for child in node.get_children():
        result += ' ' + _pre_order(child)
      return result
    return _pre_order(self)

  # abstract methods
  def add_child(self, child: 'AbstractNode') -> None:
    raise NotImplementedError

  def add_child_at(self, child: 'AbstractNode', idx: int) -> None:
    raise NotImplementedError

  def set_children(self, children: Union[str, list]) -> None:
    raise NotImplementedError

  def is_terminal(self) -> bool:
    raise NotImplementedError

  def is_nonterminal(self) -> bool:
    raise NotImplementedError

  def get_index_as_child(self) -> int:
    '''get index of `self` in `self.parent.children`'''
    raise NotImplementedError

  def get_num_siblings(self) -> int:
    raise NotImplementedError

  def get_siblings_to_the_right(self) -> List['AbstractNode']:
    raise NotImplementedError

  def has_single_terminal_child(self) -> bool:
    raise NotImplementedError

  def str_node_has_single_terminal_child(self) -> bool:
    raise NotImplementedError


class NonTerminalNode(AbstractNode):
  '''
  Non-terminal node: works for any tree
  '''
  def __init__(self, node_type: str, parent: AbstractNode) -> None:
    super().__init__(node_type, parent)

  # overridden methods
  def add_child(self, child: AbstractNode):
    self.children.append(child)

  def add_child_at(self, child: 'AbstractNode', idx: int) -> None:
    assert 0 <= idx <= len(self.children)
    self.children.insert(idx, child)

  def set_children(self, children: Union[str, list]) -> None:
    self.children = children

  def is_terminal(self) -> bool:
    return False

  def is_nonterminal(self) -> bool:
    return True

  def get_index_as_child(self) -> int:
    if self.is_root_node():
      return 0
    return self.get_parent().get_children().index(self)

  def get_num_siblings(self) -> int:
    if self.is_root_node():
      return 0
    return len(self.get_parent().get_children()) - 1

  def get_siblings_to_the_right(self) -> List['AbstractNode']:
    if self.is_root_node():
      return []
    return self.get_parent().get_children()[self.get_index_as_child()+1:]

  def has_single_terminal_child(self) -> bool:
    if self.num_children() == 1 and isinstance(self.children[0], TerminalNode):
      return True
    return False

  def str_node_has_single_terminal_child(self) -> bool:
    '''
    Terminal nodes for syntax elements such as `:`, `,`, `(`
    are represented under `str` node type in translation rule patterns.
    This method is for checking if a node is such.
    '''
    if self.has_single_terminal_child() and self.get_type() == 'str':
      return True
    return False


class TerminalNode(AbstractNode):
  '''
  Terminal node for pattern on source side.
  '''
  # overridden methods
  def add_child(self, child: AbstractNode) -> None:
    raise AttributeError('Cannot add a child to a terminal node.')

  def add_child_at(self, child: 'AbstractNode', idx: int) -> None:
    raise AttributeError('Cannot add a child to a terminal node.')

  def set_children(self, children: Union[str, list]) -> None:
    raise AttributeError('Cannot add a child to a terminal node.')

  def is_terminal(self) -> bool:
    return True

  def is_nonterminal(self) -> bool:
    return False

  def get_index_as_child(self) -> int:
    return 0

  def get_num_siblings(self) -> int:
    return 0

  def get_siblings_to_the_right(self) -> List['AbstractNode']:
    return []

  def has_single_terminal_child(self) -> bool:
    return False


class PlainTerminalNode(TerminalNode):
  '''
  Terminal node non-PH nodes.
  '''
  def __init__(self, node_type: str, parent: AbstractNode) -> None:
    super().__init__(node_type, parent)


class PhNode(TerminalNode):
  '''
  Terminal node for PH nodes.
  '''
  def __init__(self, node_type: str, parent: AbstractNode, phid: int) -> None:
    super().__init__(node_type, parent)
    self.phid = phid

  def get_phid(self) -> int:
    return self.phid

  def set_phid(self, phid: int) -> None:
    self.phid = phid


class SourcePhNode(PhNode):
  pass


class TargetPhNode(PhNode):
  pass


class SourceValPhNode(SourcePhNode):
  def __str__(self) -> str:
    return f'Source _val_ PH node id={self.get_phid()}'


class SourceStrPhNode(SourcePhNode):
  def __str__(self) -> str:
    return f'Source _str_ PH node id={self.get_phid()}'


class SourceDotStarPhNode(SourcePhNode):
  def __str__(self) -> str:
    return f'Source .|* PH node id={self.get_phid()}'


class TargetValPhNode(TargetPhNode):
  def __str__(self) -> str:
    return f'Target _val<d>_ PH node id={self.get_phid()}'


class TargetStrPhNode(TargetPhNode):
  def __str__(self) -> str:
    return f'Target _str<d>_ PH node id={self.get_phid()}'


class TargetDotStarPhNode(TargetPhNode):
  def __str__(self) -> str:
    return f'Target .<d>|*<d> PH node id={self.get_phid()}'


class TranslationRule:
  '''
  A mutable tree representation of translation rule patterns.
  '''
  def __init__(self, src_pattern_s_expr, tar_pattern_s_expr) -> None:
    '''
    src_pattern_s_expr: DuoGlot-style pattern s-expression (srcUnifiedPattern in rule_inference.js)
    tar_pattern_s_expr: DuoGlot-style pattern s-expression (tarUnifiedPattern in rule_inference.js)

    TODO update this grammar
    *pattern_s_expr grammar:
      pattern: [node]
      node: [node_type_nt, children] | [node_type_t, terminal] | placeholder
      node_type_nt: "str"
      node_type_t: str
      placeholder: "*" | "."
      children: Sequence[node]
      terminal: "str"

    TERMS
    S - set of placeholders in source pattern
    T - set of placeholders in target pattern
    STmap_val, STmap_str, STmap_dotstar - mapping of placeholders from S to T (1 -> 0,1,2,...)
    TSmap_val, TSmap_str, TSmap_dotstar - mapping of placeholders from T to S (1 -> 1)
    '''

    # re objects used in parsing the input
    self._re_tar_dot_star_ph = re.compile(r'^"([\.\*])(\d+)"$')
    self._re_val_ph = re.compile(r'^"_val(\d+)_"$')
    self._re_str_ph = re.compile(r'^"_str(\d+)_"$')

    # src root node
    src_root_node_type : str = src_pattern_s_expr[0]
    self.src_root_node = NonTerminalNode(src_root_node_type, None)
    self.src_dot_star_next_phid = 1
    self.src_val_next_phid = 1
    self.src_str_next_phid = 1
    # recurse src children
    src_root_node_children = src_pattern_s_expr[1:]
    for child_s_expr in src_root_node_children:
      self._rec_construct_at(self.src_root_node, child_s_expr)

    # tar root node
    tar_root_node_type : str = tar_pattern_s_expr[0]
    self.tar_root_node = NonTerminalNode(tar_root_node_type, None)
    # recurse tar children
    tar_root_node_children = tar_pattern_s_expr[1:]
    for child_s_expr in tar_root_node_children:
      self._rec_construct_at(self.tar_root_node, child_s_expr)

    # set of placeholders S and T
    self._update_placeholder_sets()

    # mappings
    self.STmap_val, self.TSmap_val, self.STmap_str, self.TSmap_str, self.STmap_dotstar, self.TSmap_dotstar = self._get_placeholder_mappings()

  def _rec_construct_at(self, parent_node: AbstractNode, s_expr) -> None:
    # base case: terminal node
    if isinstance(s_expr, str):
      # s_expr is a child of `str` node -> not PH
      if parent_node.get_type() in ['str', 'val']:
        node = PlainTerminalNode(s_expr, parent_node)
        parent_node.add_child(node)
        return

      if s_expr == '"."' or s_expr == '"*"':
        node = SourceDotStarPhNode(s_expr, parent_node, self.src_dot_star_next_phid)
        parent_node.add_child(node)
        self.src_dot_star_next_phid += 1
        return
      elif s_expr == '"_val_"':
        node = SourceValPhNode(s_expr, parent_node, self.src_val_next_phid)
        parent_node.add_child(node)
        self.src_val_next_phid += 1
        return
      elif s_expr == '"_str_"':
        node = SourceStrPhNode(s_expr, parent_node, self.src_str_next_phid)
        parent_node.add_child(node)
        self.src_str_next_phid += 1
        return

      dot_star_match = self._re_tar_dot_star_ph.match(s_expr)
      val_match = self._re_val_ph.match(s_expr)
      str_match = self._re_str_ph.match(s_expr)
      assert sum(list(map(bool, [dot_star_match, val_match, str_match]))) == 1
      if dot_star_match:
        node = TargetDotStarPhNode(s_expr, parent_node, int(dot_star_match.group(2)))
        parent_node.add_child(node)
        return
      elif val_match:
        node = TargetValPhNode(s_expr, parent_node, int(val_match.group(1)))
        parent_node.add_child(node)
        return
      elif str_match:
        node = TargetDotStarPhNode(s_expr, parent_node, int(str_match.group(1)))
        parent_node.add_child(node)
        return

      raise RuntimeError('Something is wrong. Should not reach this. Debugging needed.')

    # non-terminal node
    node_type = s_expr[0]
    node = NonTerminalNode(node_type, parent_node)
    parent_node.add_child(node)
    # recurse children
    s_expr_children = s_expr[1:]
    for s_expr_child in s_expr_children:
      self._rec_construct_at(node, s_expr_child)

  def _update_placeholder_sets(self) -> None:
    self.S = self._get_placeholders(self.src_root_node)
    self.T = self._get_placeholders(self.tar_root_node)
    assert all([isinstance(S_i, SourcePhNode) for S_i in self.S])
    assert all([isinstance(T_i, TargetPhNode) for T_i in self.T])
    self.Sfiltered_val = list(filter(lambda x: isinstance(x, SourceValPhNode), self.S))
    self.Sfiltered_str = list(filter(lambda x: isinstance(x, SourceStrPhNode), self.S))
    self.Sfiltered_dotstar = list(filter(lambda x: isinstance(x, SourceDotStarPhNode), self.S))
    self.Tfiltered_val = list(filter(lambda x: isinstance(x, TargetValPhNode), self.T))
    self.Tfiltered_str = list(filter(lambda x: isinstance(x, TargetStrPhNode), self.T))
    self.Tfiltered_dotstar = list(filter(lambda x: isinstance(x, TargetDotStarPhNode), self.T))

  def src_as_s_expression(self) -> List:
    '''
    Construct s-expression from self.src_root_node (reverse of __init__())
    '''
    return self._rec_build_s_expression(self.src_root_node)

  def tar_as_s_expression(self) -> List:
    '''
    Construct s-expression from self.tar_root_node (reverse of __init__())
    '''
    return self._rec_build_s_expression(self.tar_root_node)

  def _rec_build_s_expression(self, node: AbstractNode) -> List:
    if node.is_terminal():
      return node.get_type()
    node_as_list = [node.get_type()]
    for child in node.get_children():
      node_as_list.append(self._rec_build_s_expression(child))
    return node_as_list

  def get_src_root_node(self) -> AbstractNode:
    return self.src_root_node

  def get_tar_root_node(self) -> AbstractNode:
    return self.tar_root_node

  def debug_print(self):
    def visit_fn(node: AbstractNode):
      print(str(node) + '\n')
    print('~~~ SOURCE PATTERN:')
    self._pre_order(visit_fn, self.src_root_node)
    print('\n\n\n~~~ TARGET PATTERN:')
    self._pre_order(visit_fn, self.tar_root_node)

  def _pre_order(self, visit_fn: Callable, start_node: AbstractNode) -> None:
    def _rec_pre_order(node: AbstractNode, visit_fn: Callable):
      visit_fn(node)
      for child in node.get_children():
        _rec_pre_order(child, visit_fn)
    _rec_pre_order(start_node, visit_fn)

  def __str__(self) -> str:
    raise NotImplementedError()

  # deprecated
  def replace_secret_and_after_with_placeholder(self, secret: str) -> None:
    '''
    TODO what to do with non-terminal siblings to the left? (e.g. `{` NTs `}`)
    NOTE this is a deprecated method, as now we are using `self.replace_secret_with_placeholder()`

    Given a 'secret' identifier (function name, or any other identifier),
    replace it and everything after with an appropriate placeholder (`"*"` or `"."`).
    As a convention, the function assumes that the 'secret' is a function call.

    IDEA
    Hacky for each language. Find the location of `secret` node,
    go up until (not including) `py.block` or 'js.statement_block`.
    Another idea is to leverage the template that was used to generate the pairs for this rule.

    TERMS
    SP - set of placeholder nodes in the source pattern that are under the nodes to-be-pruned
    SP_bar - set of placeholder nodes in the source pattern that are under the nodes NOT to-be-pruned
    TP - set of placeholder nodes in the target pattern that are under the nodes to-be-pruned
    TP_bar - set of placeholder nodes in the target pattern that are under the nodes NOT to-be-pruned
    '''

    def _hack_parent_is_stop(node: 'AbstractNode'):
      assert node is not None, 'Did not find the secret node'
      return node.has_parent() and node.get_parent().get_type() in ['"py.block"', '"js.statement_block"']

    # 1 find the secret node
    src_secret_node = self._rec_find_secret_node(self.src_root_node, secret)
    tar_secret_node = self._rec_find_secret_node(self.tar_root_node, secret)

    # 2 go up to the stop node
    src_stop_node = src_secret_node
    while not _hack_parent_is_stop(src_stop_node):
      src_stop_node = src_stop_node.get_parent()
    src_stop_parent_node = src_stop_node.get_parent()

    tar_stop_node = tar_secret_node
    while not _hack_parent_is_stop(tar_stop_node):
      tar_stop_node = tar_stop_node.get_parent()
    tar_stop_parent_node = tar_stop_node.get_parent()

    # 3 determine siblings to the right
    src_siblings_right = src_stop_node.get_siblings_to_the_right()
    tar_siblings_right = tar_stop_node.get_siblings_to_the_right()

    # 4 identify placeholders SP, SP_bar, TP, TP_bar
    SP, TP = [], []
    for _node in [src_stop_node] + src_siblings_right:
      SP.extend(self._get_placeholders(_node))
    for _node in [tar_stop_node] + tar_siblings_right:
      TP.extend(self._get_placeholders(_node))
    SP_bar = [_node for _node in self.S if _node not in SP]
    TP_bar = [_node for _node in self.T if _node not in TP]

    # 5 assert precondition: all_mapped(SP, TP). Note that all_mapped(TP, SP) is not necessary
    # this check is needed to not prune placeholder nodes in SP that are used in TP_bar
    for SP_i in SP:
      for T_i in self._get_mapping_of(SP_i):
        assert T_i in TP

    # 6 prune both source and target
    del src_stop_node.get_parent().get_children()[src_stop_node.get_index_as_child():]
    del tar_stop_node.get_parent().get_children()[tar_stop_node.get_index_as_child():]

    # 7 create a placeholder in both source and target and map them to each other
    src_num_nodes_removed = len(src_siblings_right) + 1
    if src_num_nodes_removed == 1:
      src_placeholder_node = SourceDotStarPhNode('"."', src_stop_parent_node, self.src_dot_star_next_phid)
      src_stop_parent_node.add_child(src_placeholder_node)
      tar_placeholder_node = TargetDotStarPhNode(f'".{self.src_dot_star_next_phid}"', tar_stop_parent_node, self.src_dot_star_next_phid)
      tar_stop_parent_node.add_child(tar_placeholder_node)
    else:
      src_placeholder_node = SourceDotStarPhNode('"*"', src_stop_parent_node, self.src_dot_star_next_phid)
      src_stop_parent_node.add_child(src_placeholder_node)
      tar_placeholder_node = TargetDotStarPhNode(f'"*{self.src_dot_star_next_phid}"', tar_stop_parent_node, self.src_dot_star_next_phid)
      tar_stop_parent_node.add_child(tar_placeholder_node)

    self.STmap_dotstar[self.src_dot_star_next_phid] = [tar_placeholder_node]
    self.TSmap_dotstar[self.src_dot_star_next_phid] = src_placeholder_node
    self.src_dot_star_next_phid += 1

    # 8 remove mappings for nodes in pruned branches in both source and target
    for TP_i in TP:
      S_i = self._get_mapping_of(TP_i)
      if isinstance(TP_i, TargetValPhNode):
        self.STmap_val[S_i.get_phid()].remove(TP_i)  # may throw ValueError
        del self.TSmap_val[TP_i.get_phid()]
      if isinstance(TP_i, TargetStrPhNode):
        self.STmap_str[S_i.get_phid()].remove(TP_i)  # may throw ValueError
        del self.TSmap_str[TP_i.get_phid()]
      if isinstance(TP_i, TargetDotStarPhNode):
        self.STmap_dotstar[S_i.get_phid()].remove(TP_i)  # may throw ValueError
        del self.TSmap_dotstar[TP_i.get_phid()]

    # 9 pre-order source pattern, and update ph_id's incrementally
    self._recalculate_phids_and_remap(SP, TP)

    # 10
    self._update_placeholder_sets()

  def replace_secret_with_placeholder(self, secret_identifier: str) -> None:
    '''
    Given a 'secret' identifier (function name, or any other identifier),
    replace ONLY it with a placeholder `"*"`.
    As a convention, the function assumes that the 'secret' is a function call.

    IDEA
    Hacky for each language. Find the location of `secret` node,
    go up until (not including) `py.block` or 'js.statement_block` (a.k.a. stop node).
    Another idea is to leverage the template that was used to generate the pairs for this rule.

    TERMS
    SP - set of placeholder nodes in the source pattern that are under the nodes to-be-pruned
    SP_bar - set of placeholder nodes in the source pattern that are under the nodes NOT to-be-pruned
    TP - set of placeholder nodes in the target pattern that are under the nodes to-be-pruned
    TP_bar - set of placeholder nodes in the target pattern that are under the nodes NOT to-be-pruned
    '''

    def _hack_parent_is_stop(node: 'AbstractNode'):
      assert node is not None, 'Did not find the secret node'
      return node.has_parent() and node.get_parent().get_type() in ['"py.block"', '"js.statement_block"']

    # 1 find the secret node
    src_secret_node = self._rec_find_secret_node(self.src_root_node, secret_identifier)
    tar_secret_node = self._rec_find_secret_node(self.tar_root_node, secret_identifier)
    assert src_secret_node is not None, 'secret node in src pattern not found'
    assert tar_secret_node is not None, 'secret node in tar pattern not found'

    # 2 go up to the stop node (`py.block` or 'js.statement_block`)
    src_stop_node = src_secret_node
    while not _hack_parent_is_stop(src_stop_node):
      src_stop_node = src_stop_node.get_parent()
    src_stop_parent_node = src_stop_node.get_parent()

    tar_stop_node = tar_secret_node
    while not _hack_parent_is_stop(tar_stop_node):
      tar_stop_node = tar_stop_node.get_parent()
    tar_stop_parent_node = tar_stop_node.get_parent()

    # 3 determine siblings to the right
    src_siblings_right = src_stop_node.get_siblings_to_the_right()
    tar_siblings_right = tar_stop_node.get_siblings_to_the_right()

    # 4 identify placeholders SP, SP_bar, TP, TP_bar
    # need them to update placeholder mappings
    SP, TP = [], []
    for _node in [src_stop_node] + src_siblings_right:
      SP.extend(self._get_placeholders(_node))
    for _node in [tar_stop_node] + tar_siblings_right:
      TP.extend(self._get_placeholders(_node))
    SP_bar = [_node for _node in self.S if _node not in SP]
    TP_bar = [_node for _node in self.T if _node not in TP]

    # 5 assert precondition: all_mapped(SP, TP). Note that all_mapped(TP, SP) is not necessary
    # this check is needed to not prune placeholder nodes in SP that are used in TP_bar
    # TODO maybe raise an exception OR return null?
    for SP_i in SP:
      for T_i in self._get_mapping_of(SP_i):
        assert T_i in TP

    # 6 prune both source and target
    # NOTE we do the same way as in replace_secret_and_after_with_placeholder
    # since secret function call node is the only node (no previous nodes, so no need to worry about them)
    src_stop_node_idx_in_parent = src_stop_node.get_index_as_child()
    tar_stop_node_idx_in_parent = tar_stop_node.get_index_as_child()
    del src_stop_node.get_parent().get_children()[src_stop_node.get_index_as_child()]
    del tar_stop_node.get_parent().get_children()[tar_stop_node.get_index_as_child()]

    # 7 create a placeholder in both source and target and map them to each other
    # NOTE always replace with '*'
    src_placeholder_node = SourceDotStarPhNode('"*"', src_stop_parent_node, self.src_dot_star_next_phid)
    src_stop_parent_node.add_child_at(src_placeholder_node, src_stop_node_idx_in_parent)
    tar_placeholder_node = TargetDotStarPhNode(f'"*{self.src_dot_star_next_phid}"', tar_stop_parent_node, self.src_dot_star_next_phid)
    tar_stop_parent_node.add_child_at(tar_placeholder_node, tar_stop_node_idx_in_parent)

    # update placeholder mappings for newly created DotStarPhNode's
    self.STmap_dotstar[self.src_dot_star_next_phid] = [tar_placeholder_node]
    self.TSmap_dotstar[self.src_dot_star_next_phid] = src_placeholder_node
    self.src_dot_star_next_phid += 1

    # 8 remove mappings for nodes in pruned branches in both source and target
    for TP_i in TP:
      S_i = self._get_mapping_of(TP_i)
      if isinstance(TP_i, TargetValPhNode):
        self.STmap_val[S_i.get_phid()].remove(TP_i)  # may throw ValueError
        del self.TSmap_val[TP_i.get_phid()]
      if isinstance(TP_i, TargetStrPhNode):
        self.STmap_str[S_i.get_phid()].remove(TP_i)  # may throw ValueError
        del self.TSmap_str[TP_i.get_phid()]
      if isinstance(TP_i, TargetDotStarPhNode):
        self.STmap_dotstar[S_i.get_phid()].remove(TP_i)  # may throw ValueError
        del self.TSmap_dotstar[TP_i.get_phid()]

    # 9 pre-order source pattern, and update ph_id's incrementally
    self._recalculate_phids_and_remap(SP, TP)

    # 10
    self._update_placeholder_sets()

  def _rec_find_secret_node(self, start_node: AbstractNode, secret_keyword: str) -> Union[AbstractNode, None]:
    '''search for a node using pre-order traversal'''
    if start_node.get_type().strip('"') == secret_keyword:
      return start_node
    for child in start_node.get_children():
      child_res = self._rec_find_secret_node(child, secret_keyword)
      if child_res is not None:
        return child_res
    return None

  def _get_placeholders(self, start_node: AbstractNode) -> List[PhNode]:
    '''return a list of placeholder nodes under `start_node`'''
    ph_nodes = []
    def visit(node: AbstractNode):
      nonlocal ph_nodes
      if isinstance(node, PhNode):
        ph_nodes.append(node)
    self._pre_order(visit, start_node)
    return ph_nodes

  def _get_placeholder_mappings(self):
    '''
    return a mapping of placeholders SOURCE->TARGET and TARGET->SOURCE

    S - set of placeholders in source pattern
    T - set of placeholders in target pattern
    STmap_val, STmap_str, STmap_dotstar - mapping of placeholders from S to T (1 -> 0,1,2,...)
    TSmap_val, TSmap_str, TSmap_dotstar - mapping of placeholders from T to S (1 -> 1)
    '''
    def _get_S_i_from_T_i(T_i: TargetPhNode, S: List[SourcePhNode]):
      for S_i in S:
        if T_i.get_phid() == S_i.get_phid():
          return S_i
      raise ValueError('There has to be a matching placeholder in S for every placeholder in T.')

    STmap_val = dict()
    TSmap_val = dict()
    STmap_str = dict()
    TSmap_str = dict()
    STmap_dotstar = dict()
    TSmap_dotstar = dict()

    # iterate T, and find its pair in S
    for T_i in self.T:
      T_i_id = T_i.get_phid()
      if isinstance(T_i, TargetValPhNode):
        S_i = _get_S_i_from_T_i(T_i, self.Sfiltered_val)
        TSmap_val[T_i_id] = S_i
        STmap_val.setdefault(S_i.get_phid(), []).append(T_i)
      elif isinstance(T_i, TargetStrPhNode):
        S_i = _get_S_i_from_T_i(T_i, self.Sfiltered_str)
        TSmap_str[T_i_id] = S_i
        STmap_str.setdefault(S_i.get_phid(), []).append(T_i)
      elif isinstance(T_i, TargetDotStarPhNode):
        S_i = _get_S_i_from_T_i(T_i, self.Sfiltered_dotstar)
        TSmap_dotstar[T_i_id] = S_i
        STmap_dotstar.setdefault(S_i.get_phid(), []).append(T_i)

    return STmap_val, TSmap_val, STmap_str, TSmap_str, STmap_dotstar, TSmap_dotstar

  def _get_mapping_of(self, node: PhNode) -> Union[List[PhNode], PhNode]:
    '''given ANY PhNode, whether source or target, returns its mapping'''
    assert isinstance(node, PhNode)

    if isinstance(node, SourceValPhNode):
      return self.STmap_val.get(node.get_phid(), [])
    elif isinstance(node, SourceStrPhNode):
      return self.STmap_str.get(node.get_phid(), [])
    elif isinstance(node, SourceDotStarPhNode):
      return self.STmap_dotstar.get(node.get_phid(), [])
    elif isinstance(node, TargetValPhNode):
      assert node.get_phid() in self.TSmap_val
      return self.TSmap_val[node.get_phid()]
    elif isinstance(node, TargetStrPhNode):
      assert node.get_phid() in self.TSmap_str
      return self.TSmap_str[node.get_phid()]
    elif isinstance(node, TargetDotStarPhNode):
      assert node.get_phid() in self.TSmap_dotstar
      return self.TSmap_dotstar[node.get_phid()]

    raise RuntimeError('Sanity check: Should not reach this. Debugging needed.')

  def _recalculate_phids_and_remap(self, SP: List[SourcePhNode], TP: List[TargetPhNode]) -> None:
    '''
    recalculate placeholder ids and update mappings after source and target patterns are modified
    SP: list of placeholder nodes that were pruned in source pattern
    TP: list of placeholder nodes that were pruned in target pattern
    '''
    self.src_dot_star_next_phid = 1
    self.src_val_next_phid = 1
    self.src_str_next_phid = 1

    STmap_val_new = dict()
    TSmap_val_new = dict()
    STmap_str_new = dict()
    TSmap_str_new = dict()
    STmap_dotstar_new = dict()
    TSmap_dotstar_new = dict()

    def _visit_update_phid(S_i: AbstractNode):
      nonlocal STmap_val_new
      nonlocal TSmap_val_new
      nonlocal STmap_str_new
      nonlocal TSmap_str_new
      nonlocal STmap_dotstar_new
      nonlocal TSmap_dotstar_new
      nonlocal SP, TP
      if isinstance(S_i, SourceValPhNode):
        T_i_list = self._get_mapping_of(S_i)
        # update mappings S->T
        STmap_val_new[self.src_val_next_phid] = [T_i for T_i in T_i_list if T_i not in TP]
        # update phid S_i
        S_i.set_phid(self.src_val_next_phid)
        for T_i in T_i_list:
          # update mappings T -> S
          TSmap_val_new[self.src_val_next_phid] = S_i
          # update phid T_i
          self._update_phid_tar_phnode(T_i, self.src_val_next_phid)
        self.src_val_next_phid += 1
      elif isinstance(S_i, SourceStrPhNode):
        T_i_list = self._get_mapping_of(S_i)
        # update mappings S->T
        STmap_str_new[self.src_str_next_phid] = [T_i for T_i in T_i_list if T_i not in TP]
        # update phid S_i
        S_i.set_phid(self.src_str_next_phid)
        for T_i in T_i_list:
          # update mappings T -> S
          TSmap_str_new[self.src_str_next_phid] = S_i
          # update phid T_i
          self._update_phid_tar_phnode(T_i, self.src_str_next_phid)
        self.src_str_next_phid += 1
      elif isinstance(S_i, SourceDotStarPhNode):
        T_i_list = self._get_mapping_of(S_i)
        # update mappings S->T
        STmap_dotstar_new[self.src_dot_star_next_phid] = [T_i for T_i in T_i_list if T_i not in TP]
        # update phid S_i
        S_i.set_phid(self.src_dot_star_next_phid)
        for T_i in T_i_list:
          # update mappings T -> S
          TSmap_dotstar_new[self.src_dot_star_next_phid] = S_i
          # update phid T_i
          self._update_phid_tar_phnode(T_i, self.src_dot_star_next_phid)
        self.src_dot_star_next_phid += 1

    self._pre_order(_visit_update_phid, self.src_root_node)

    self.STmap_val = STmap_val_new
    self.TSmap_val = TSmap_val_new
    self.STmap_str = STmap_str_new
    self.TSmap_str = TSmap_str_new
    self.STmap_dotstar = STmap_dotstar_new
    self.TSmap_dotstar = TSmap_dotstar_new

  def _update_phid_tar_phnode(self, tar_phnode: TargetPhNode, new_phid: int) -> None:
    '''update placeholder id for target node'''
    assert isinstance(tar_phnode, TargetPhNode)

    tar_phnode.set_phid(new_phid)
    if isinstance(tar_phnode, TargetValPhNode):
      tar_phnode.set_type(f'"_val{new_phid}_"')
    elif isinstance(tar_phnode, TargetStrPhNode):
      tar_phnode.set_type(f'"_str{new_phid}_"')
    else:
      dot_star_match = self._re_tar_dot_star_ph.match(tar_phnode.get_type())
      assert dot_star_match
      dot_or_star = dot_star_match.group(1)
      tar_phnode.set_type(f'"{dot_or_star}{new_phid}"')

  def trim_context(
    self,
    context: dict
  ) -> Union[None, Tuple[list, list]]:
    '''
    Trim the given context from TranslationRule.
    This method is an API for server_trans.pirel_postprocess_translation_rule()

    POST: self is not mutated

    NOTE this method is a doppleganger of p_llm_val._context_exists()
    '''
    def _are_previous_siblings(node: NonTerminalNode, sibling_types: List[str]) -> bool:
      '''
      PRE: siblings are ordered naturally (as appeared in tree)

      IDEA
      Get all NT siblings to the left, make 1-1 comparison
      '''

      assert isinstance(node, NonTerminalNode)

      node_siblings = node.get_siblings_to_the_left()

      # we only need non-terminal nodes
      def __filter_sibling(sibling: NonTerminalNode) -> bool:
        if sibling.str_node_has_single_terminal_child():
          return False
        return True
      node_siblings = list(filter(__filter_sibling, node_siblings))

      # base case 2
      if len(node_siblings) != len(sibling_types):
        return False

      # TODO since templates can be simplified, it may ever so happen that previous sibling nodes
      # of problematic node get simplified. In this case, sibling node type changes from
      # the one in original template to a node type that replaces it. Thus,
      # the check below cannot find the right context for it.
      # Workaround is to check the number of previous siblings. In the future, the number of
      # siblings may depend on whether the matcher is '*' or '.'.
      # for node_sibling, sibling_type in zip(node_siblings, reversed(sibling_types)):
      #   if node_sibling.get_type().strip('"') != sibling_type.strip('"'):
      #     return False
      if len(node_siblings) != len(sibling_types):
        return False

      return True

    def _are_parents(node: NonTerminalNode, parent_types: List[str]) -> bool:
      '''
      PRE: siblings are ordered naturally (as appeared in tree)

      IDEA
      Starting from immediate parent, go up until reach root node OR
      exhaust parent_types, make 1-1 comparison
      '''

      assert isinstance(node, NonTerminalNode)

      cursor_node = node.get_parent()
      parent_type_idx = 0

      while True:

        # stop condition 1
        if cursor_node is None:
          break

        # stop condition 2
        if parent_type_idx == len(parent_types):
          break

        parent_type = parent_types[parent_type_idx]
        if cursor_node.get_type().strip('"') != parent_type.strip('"'):
          return False

        parent_type_idx += 1
        cursor_node = cursor_node.get_parent()

      # there is a parent_type that we did not check
      if parent_type_idx < len(parent_types):
        return False

      return True

    # NOTE siblings are checked ONLY for the problematic node
    def _rec_pre_order_find_problematic_node(
      node: AbstractNode,
      sibling_types: List[str],
      parent_types: List[str]
    ) -> List[Union[AbstractNode, None]]:
      '''
      We are interested only in Tree-sitter-like non-terminal nodes
      i.e. `js.expression_statement`, `py.identifier`, etc.
      not `val`, `str`, etc.
      '''

      if isinstance(node, TerminalNode):
        return [None]

      if node.str_node_has_single_terminal_child():
        return [None]

      is_siblings_ok = _are_previous_siblings(node, sibling_types)
      is_parents_ok = _are_parents(node, parent_types)
      if is_siblings_ok and is_parents_ok:
        return [node]

      # NOTE we may not need this check
      if node.has_single_terminal_child():
        return [None]

      children_result = []
      for child_node in node.get_children():
        child_result = _rec_pre_order_find_problematic_node(child_node, sibling_types, parent_types)
        children_result.extend(child_result)

      return children_result

    src_ctx = context['source_context']
    tar_ctx = context['target_context']

    src_problematic_nodes = _rec_pre_order_find_problematic_node(self.src_root_node, src_ctx['siblings'], src_ctx['parents'])
    src_problematic_nodes = list(filter(lambda x: x is not None, src_problematic_nodes))
    # context is not found
    if len(src_problematic_nodes) == 0:
      return None
    if len(src_problematic_nodes) > 1:
      print('WARNING: weak source context')

    tar_problematic_nodes = _rec_pre_order_find_problematic_node(self.tar_root_node, tar_ctx['siblings'], tar_ctx['parents'])
    tar_problematic_nodes = list(filter(lambda x: x is not None, tar_problematic_nodes))
    # context is not found
    if len(tar_problematic_nodes) == 0:
      return None
    if len(tar_problematic_nodes) > 1:
      print('WARNING: weak target context')

    # 1 get problematic node in source and target sides
    src_problematic_node = src_problematic_nodes[0]
    tar_problematic_node = tar_problematic_nodes[0]

    if src_problematic_node is None or tar_problematic_node is None:
      return None

    assert src_problematic_node is not None
    assert tar_problematic_node is not None

    # problematic node is 'fragment' if context is empty
    # TODO is there a better way to do this?
    is_src_context_empty = src_problematic_node.get_type() == 'fragment'
    is_tar_context_empty = tar_problematic_node.get_type() == 'fragment'

    # here we need to make src_problematic_node and tar_problematic_node
    # root nodes of their corresponding trees
    # 2 necessary condition for isolation is that
    # all placeholder nodes in tar are mapped under src
    src_ph_nodes = self._get_placeholders(src_problematic_node)
    tar_ph_nodes = self._get_placeholders(tar_problematic_node)
    tar_ph_nodes_mappings = [self._get_mapping_of(x) for x in tar_ph_nodes]
    for tar_ph_node_mapping in tar_ph_nodes_mappings:
      assert tar_ph_node_mapping in src_ph_nodes

    # 3 SP and TP are ph nodes under to-be-pruned trees
    all_src_ph_nodes = self._get_placeholders(self.src_root_node)
    all_tar_ph_nodes = self._get_placeholders(self.tar_root_node)
    SP = [phn for phn in all_src_ph_nodes if phn not in src_ph_nodes]
    TP = [phn for phn in all_tar_ph_nodes if phn not in tar_ph_nodes]

    # 4 make the problematic nodes roots
    # if context is empty, we don't need to modify the tree
    if not is_src_context_empty:
      self.src_root_node.set_children([src_problematic_node])
      src_problematic_node.set_parent(self.src_root_node)
    if not is_tar_context_empty:
      self.tar_root_node.set_children([tar_problematic_node])
      tar_problematic_node.set_parent(self.tar_root_node)

    # TODO when do we need to add ph node?
    if not is_src_context_empty and not is_tar_context_empty:
      # 5 add a star ph node
      src_placeholder_node = SourceDotStarPhNode('"*"', self.src_root_node, self.src_dot_star_next_phid)
      self.src_root_node.add_child(src_placeholder_node)
      tar_placeholder_node = TargetDotStarPhNode(f'"*{self.src_dot_star_next_phid}"', self.tar_root_node, self.src_dot_star_next_phid)
      self.tar_root_node.add_child(tar_placeholder_node)

      # 6 update placeholder mappings for newly created DotStarPhNode's
      self.STmap_dotstar[self.src_dot_star_next_phid] = [tar_placeholder_node]
      self.TSmap_dotstar[self.src_dot_star_next_phid] = src_placeholder_node
      self.src_dot_star_next_phid += 1

    # 7 remove mappings for nodes in pruned branches in both source and target
    for TP_i in TP:
      S_i = self._get_mapping_of(TP_i)
      if isinstance(TP_i, TargetValPhNode):
        self.STmap_val[S_i.get_phid()].remove(TP_i)  # may throw ValueError
        del self.TSmap_val[TP_i.get_phid()]
      if isinstance(TP_i, TargetStrPhNode):
        self.STmap_str[S_i.get_phid()].remove(TP_i)  # may throw ValueError
        del self.TSmap_str[TP_i.get_phid()]
      if isinstance(TP_i, TargetDotStarPhNode):
        self.STmap_dotstar[S_i.get_phid()].remove(TP_i)  # may throw ValueError
        del self.TSmap_dotstar[TP_i.get_phid()]

    # 8 do some final stuff
    self._recalculate_phids_and_remap(SP, TP)
    self._update_placeholder_sets()

    src_trimmed_pattern = self._rec_build_s_expression(self.src_root_node)
    tar_trimmed_pattern = self._rec_build_s_expression(self.tar_root_node)

    return src_trimmed_pattern, tar_trimmed_pattern

  def trim_context_v2(
    self,
    context: dict,
    templatized_node_ids: dict,
    templatized_nodes_replace_dws: list
  ) -> Union[None, Tuple[list, list]]:
    '''
    Trim the given context from TranslationRule.
    This method is an API for server_trans.pirel_postprocess_translation_rule()

    POST: self is not mutated

    NOTE this method is a doppleganger of p_llm_val._context_exists()
    '''
    def _are_previous_siblings(node: NonTerminalNode, sibling_types: List[str]) -> bool:
      '''
      PRE: siblings are ordered naturally (as appeared in tree)

      IDEA
      Get all NT siblings to the left, make 1-1 comparison
      '''

      assert isinstance(node, NonTerminalNode)

      node_siblings = node.get_siblings_to_the_left()

      # we only need non-terminal nodes
      def __filter_sibling(sibling: NonTerminalNode) -> bool:
        if sibling.str_node_has_single_terminal_child():
          return False
        return True
      node_siblings = list(filter(__filter_sibling, node_siblings))

      # base case 2
      if len(node_siblings) != len(sibling_types):
        return False

      # TODO since templates can be simplified, it may ever so happen that previous sibling nodes
      # of problematic node get simplified. In this case, sibling node type changes from
      # the one in original template to a node type that replaces it. Thus,
      # the check below cannot find the right context for it.
      # Workaround is to check the number of previous siblings. In the future, the number of
      # siblings may depend on whether the matcher is '*' or '.'.
      # for node_sibling, sibling_type in zip(node_siblings, reversed(sibling_types)):
      #   if node_sibling.get_type().strip('"') != sibling_type.strip('"'):
      #     return False
      if len(node_siblings) != len(sibling_types):
        return False

      return True

    def _are_parents(node: NonTerminalNode, parent_types: List[str]) -> bool:
      '''
      PRE: siblings are ordered naturally (as appeared in tree)

      IDEA
      Starting from immediate parent, go up until reach root node OR
      exhaust parent_types, make 1-1 comparison
      '''

      assert isinstance(node, NonTerminalNode)

      cursor_node = node.get_parent()
      parent_type_idx = 0

      while True:

        # stop condition 1
        if cursor_node is None:
          break

        # stop condition 2
        if parent_type_idx == len(parent_types):
          break

        parent_type = parent_types[parent_type_idx]
        if cursor_node.get_type().strip('"') != parent_type.strip('"'):
          return False

        parent_type_idx += 1
        cursor_node = cursor_node.get_parent()

      # there is a parent_type that we did not check
      if parent_type_idx < len(parent_types):
        return False

      return True

    # NOTE siblings are checked ONLY for the problematic node
    def _rec_pre_order_find_problematic_node(
      node: AbstractNode,
      sibling_types: List[str],
      parent_types: List[str]
    ) -> List[Union[AbstractNode, None]]:
      '''
      We are interested only in Tree-sitter-like non-terminal nodes
      i.e. `js.expression_statement`, `py.identifier`, etc.
      not `val`, `str`, etc.
      '''

      if isinstance(node, TerminalNode):
        return [None]

      if node.str_node_has_single_terminal_child():
        return [None]

      is_siblings_ok = _are_previous_siblings(node, sibling_types)
      is_parents_ok = _are_parents(node, parent_types)
      if is_siblings_ok and is_parents_ok:
        return [node]

      # NOTE we may not need this check
      if node.has_single_terminal_child():
        return [None]

      children_result = []
      for child_node in node.get_children():
        child_result = _rec_pre_order_find_problematic_node(child_node, sibling_types, parent_types)
        children_result.extend(child_result)

      return children_result

    def _flatten_list(S):
      if S == []:
          return S
      if isinstance(S[0], list):
          return _flatten_list(S[0]) + _flatten_list(S[1:])
      return S[:1] + _flatten_list(S[1:])

    def _replace_dws(templatized_node_ids: dict, templatized_nodes_replace_dws: list) -> None:
      ''''''
      assert len(templatized_node_ids) == len(templatized_nodes_replace_dws)
      for do_replace, templatized_node_path in zip(templatized_nodes_replace_dws, templatized_node_ids.values()):
        # NOTE isinstance(do_replace, (bool, list))
        # it can be a list, because we allow recursive unification check
        if isinstance(do_replace, bool) and not do_replace:
          continue
        if isinstance(do_replace, list) and not any(_flatten_list(do_replace)):
          continue
        templatized_node = self.src_root_node.get_children()[0].get_child_by_path(templatized_node_path)
        src_dotstar_ph_nodes = templatized_node.get_src_dotstar_ph_nodes_under()
        src_dot_ph_nodes = [node for node in src_dotstar_ph_nodes if node.get_type() == '"."']
        assert len(src_dot_ph_nodes) == 1, 'there should be ONLY ONE dot ph node under templatized node'
        src_dot_ph_node = src_dot_ph_nodes[0]
        src_dot_ph_node.set_type('"*"')
        for tar_dot_ph_node in self._get_mapping_of(src_dot_ph_node):
          old_ph = tar_dot_ph_node.get_type()
          new_ph = old_ph.replace('.', '*')
          tar_dot_ph_node.set_type(new_ph)

    # replace dot ph node with star ph node before removing context
    # TODO in some cases works incorrectly
    # _replace_dws(templatized_node_ids, templatized_nodes_replace_dws)

    src_ctx = context['source_context']
    tar_ctx = context['target_context']

    src_problematic_nodes = _rec_pre_order_find_problematic_node(self.src_root_node, src_ctx['siblings'], src_ctx['parents'])
    src_problematic_nodes = list(filter(lambda x: x is not None, src_problematic_nodes))
    # context is not found
    if len(src_problematic_nodes) == 0:
      return None
    if len(src_problematic_nodes) > 1:
      print('WARNING: weak source context')

    tar_problematic_nodes = _rec_pre_order_find_problematic_node(self.tar_root_node, tar_ctx['siblings'], tar_ctx['parents'])
    tar_problematic_nodes = list(filter(lambda x: x is not None, tar_problematic_nodes))
    # context is not found
    if len(tar_problematic_nodes) == 0:
      return None
    if len(tar_problematic_nodes) > 1:
      print('WARNING: weak target context')

    # 1 get problematic node in source and target sides
    src_problematic_node = src_problematic_nodes[0]
    tar_problematic_node = tar_problematic_nodes[0]

    if src_problematic_node is None or tar_problematic_node is None:
      return None

    assert src_problematic_node is not None
    assert tar_problematic_node is not None

    # problematic node is 'fragment' if context is empty
    # TODO is there a better way to do this?
    is_src_context_empty = src_problematic_node.get_type() == 'fragment'
    is_tar_context_empty = tar_problematic_node.get_type() == 'fragment'

    # here we need to make src_problematic_node and tar_problematic_node
    # root nodes of their corresponding trees
    # 2 necessary condition for isolation is that
    # all placeholder nodes in tar are mapped under src
    src_ph_nodes = self._get_placeholders(src_problematic_node)
    tar_ph_nodes = self._get_placeholders(tar_problematic_node)
    tar_ph_nodes_mappings = [self._get_mapping_of(x) for x in tar_ph_nodes]
    for tar_ph_node_mapping in tar_ph_nodes_mappings:
      assert tar_ph_node_mapping in src_ph_nodes

    # 3 SP and TP are ph nodes under to-be-pruned trees
    all_src_ph_nodes = self._get_placeholders(self.src_root_node)
    all_tar_ph_nodes = self._get_placeholders(self.tar_root_node)
    SP = [phn for phn in all_src_ph_nodes if phn not in src_ph_nodes]
    TP = [phn for phn in all_tar_ph_nodes if phn not in tar_ph_nodes]

    # 4 make the problematic nodes roots
    # if context is empty, we don't need to modify the tree
    if not is_src_context_empty:
      self.src_root_node.set_children([src_problematic_node])
      src_problematic_node.set_parent(self.src_root_node)
    if not is_tar_context_empty:
      self.tar_root_node.set_children([tar_problematic_node])
      tar_problematic_node.set_parent(self.tar_root_node)

    # TODO when do we need to add ph node?
    if not is_src_context_empty and not is_tar_context_empty:
      # 5 add a star ph node
      src_placeholder_node = SourceDotStarPhNode('"*"', self.src_root_node, self.src_dot_star_next_phid)
      self.src_root_node.add_child(src_placeholder_node)
      tar_placeholder_node = TargetDotStarPhNode(f'"*{self.src_dot_star_next_phid}"', self.tar_root_node, self.src_dot_star_next_phid)
      self.tar_root_node.add_child(tar_placeholder_node)

      # 6 update placeholder mappings for newly created DotStarPhNode's
      self.STmap_dotstar[self.src_dot_star_next_phid] = [tar_placeholder_node]
      self.TSmap_dotstar[self.src_dot_star_next_phid] = src_placeholder_node
      self.src_dot_star_next_phid += 1

    # 7 remove mappings for nodes in pruned branches in both source and target
    for TP_i in TP:
      S_i = self._get_mapping_of(TP_i)
      if isinstance(TP_i, TargetValPhNode):
        self.STmap_val[S_i.get_phid()].remove(TP_i)  # may throw ValueError
        del self.TSmap_val[TP_i.get_phid()]
      if isinstance(TP_i, TargetStrPhNode):
        self.STmap_str[S_i.get_phid()].remove(TP_i)  # may throw ValueError
        del self.TSmap_str[TP_i.get_phid()]
      if isinstance(TP_i, TargetDotStarPhNode):
        self.STmap_dotstar[S_i.get_phid()].remove(TP_i)  # may throw ValueError
        del self.TSmap_dotstar[TP_i.get_phid()]

    # 8 do some final stuff
    self._recalculate_phids_and_remap(SP, TP)
    self._update_placeholder_sets()

    src_trimmed_pattern = self._rec_build_s_expression(self.src_root_node)
    tar_trimmed_pattern = self._rec_build_s_expression(self.tar_root_node)

    return src_trimmed_pattern, tar_trimmed_pattern


def test_replace_secret_with_placeholder():
  with open('temporary_source-unified-pattern.json') as fin:
    srcpat = json.loads(fin.read())
  with open('temporary_target-unified-pattern.json') as fin:
    tarpat = json.loads(fin.read())

  # def foo(node: Node):
  #   nt = node.get_text()
  #   if '\n' in nt:
  #     print(node)
  #     print()
  #   for ch in node.children:
  #     foo(ch)

  tree = TranslationRule(srcpat, tarpat)
  tree.debug_print()

  with open('temporary_source_pattern_tree_back.json', 'w') as fout:
    res = tree.src_as_s_expression()
    fout.write(json.dumps(res))

  with open('temporary_target_pattern_tree_back.json', 'w') as fout:
    res = tree.tar_as_s_expression()
    fout.write(json.dumps(res))

  tree.replace_secret_with_placeholder('some_secret_fn_4071')
  with open('temporary_source_pattern_tree_reduced.json', 'w') as fout:
    res = tree.src_as_s_expression()
    fout.write(json.dumps(res))
  with open('temporary_target_pattern_tree_reduced.json', 'w') as fout:
    res = tree.tar_as_s_expression()
    fout.write(json.dumps(res))


def test_trim_context():
  with open('temporary_source-unified-pattern.json') as fin:
    srcpat = json.loads(fin.read())
  with open('temporary_target-unified-pattern.json') as fin:
    tarpat = json.loads(fin.read())
  with open('temporary_contexts.json') as fin:
    contexts = json.loads(fin.read())

  template_contexts = []
  for context in contexts:
    source_context = context['source_context']
    target_context = context['target_context']

    source_context_prev_siblings = source_context[0][1:]
    # source_context_parents = source_context[1:1+template_id]
    source_context_parents = list(map(lambda x: x[0], source_context[1:1+2]))
    target_context_prev_siblings = target_context[0][1:]
    # target_context_parents = target_context[1:1+template_id]
    target_context_parents = list(map(lambda x: x[0], target_context[1:1+2]))

    template_contexts.append({
      'source_context': {'siblings': source_context_prev_siblings, 'parents': source_context_parents},
      'target_context': {'siblings': target_context_prev_siblings, 'parents': target_context_parents},
    })

  tree = TranslationRule(srcpat, tarpat)
  newsrcpat, newtarpat = tree.trim_context(template_contexts)

  with open('temporary_source_pattern_tree_trimmed.json', 'w') as fout:
    fout.write(json.dumps(newsrcpat))
  with open('temporary_target_pattern_tree_trimmed.json', 'w') as fout:
    fout.write(json.dumps(newtarpat))


if __name__ == '__main__':
  test_trim_context()