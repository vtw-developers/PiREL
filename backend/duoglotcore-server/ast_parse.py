import json
import consts
from tree_sitter import Parser, Language, Node, Tree
from typing import Tuple, Union
import p_consts


def _anno_func_py_string(ann, context: str):
  startpos = ann[0]
  endpos = ann[1]
  subs = context[startpos:endpos]
  stype = ""
  if subs.startswith("f"): stype = "f"
  elif subs.startswith("r"): stype = "r"
  elif subs.startswith("b"): stype = "b"
  else:
    if not (subs.startswith('"') or subs.startswith("'")):
      print("_anno_func_py_string UNEXPECTED:", subs)
      assert "parse_error" == 0 or (subs.startswith('"') or subs.startswith("'"))
  quote = None
  if subs.endswith('\"\"\"'): quote = '\"\"\"'
  elif subs.endswith("\'\'\'"): quote = "\'\'\'"
  elif subs.endswith('\"'): quote = '\"'
  elif subs.endswith("\'"): quote = "\'"
  else: assert 0 == "py.string does not endswith ' or \""
  return ["anno", ['"stype"', f'"{stype}"'], ['"quote"', f'{json.dumps(quote)}']]


_ANNO_FUNC_DICT = {
  "py.string": _anno_func_py_string
}


def parse_text_dbg(text: str, lang: str, keep_text=False) -> Tuple[list, dict]:
  '''
  text: text of source code to parse
  lang: 'py', 'js', etc.
  keep_text: save TreeSitter generated .text attribute
  '''
  parser = p_consts.PARSER_DICT[lang]
  tree = parser.parse(bytes(text, "utf8"))

  current_node_idx = 0
  ann_info = {}

  extra_root = []
  ast_scope_stack = [extra_root]

  # does nothing at the moment
  def _fn_before(node: Node):
    if node.is_named == False: return
    if consts.DEBUG_VERBOSE > 0: print("(", end="")

  # does nothing at the moment
  def _fn_before_child(child: Node):
    if consts.DEBUG_VERBOSE > 0: print(" ", end="")

  def _fn_after(node: Node):
    if node.is_named == False: return
    ast_scope_stack.pop()
    if consts.DEBUG_VERBOSE > 0: print(")", end="")

  def _fn_visit(node: Node):
    def __add_id():
      nonlocal current_node_idx
      if consts.DEBUG_VERBOSE > 0: print(f" {current_node_idx}", end="")
      ann_info[current_node_idx] = [node.start_byte, node.end_byte, node.start_point, node.end_point]
      current_node_idx += 1
      return current_node_idx - 1

    if node.is_named:
      sub_ast_list = []
      ast_scope_stack[-1].append(sub_ast_list)
      ast_scope_stack.append(sub_ast_list)

      node_type = f'{lang}.{node.type}'  # pirel-style node type
      elem = [node_type, node.text.decode('utf-8')] if keep_text else node_type

      if consts.DEBUG_VERBOSE > 0: print(elem, end="")
      sub_ast_list.append(elem)

      new_id = __add_id()
      sub_ast_list.append(new_id)

      if node_type in _ANNO_FUNC_DICT:
        anno_func = _ANNO_FUNC_DICT[node_type]
        anno = anno_func(ann_info[new_id], text)
        if anno is not None:
          sub_ast_list.append(anno)

      if len(node.children) == 0:
        # named (typed), but no children. Should be an external symbol
        elem = json.dumps(text[node.start_byte:node.end_byte])
        if consts.DEBUG_VERBOSE > 0: print("", elem, end="")
        sub_ast_list.append(elem)
    else:
      # not named
      elem = json.dumps(node.type)
      if consts.DEBUG_VERBOSE > 0: print(elem, end="")
      ast_scope_stack[-1].append(elem)

  def _traverse(tree: Tree, fn_before, fn_visit, fn_before_child, fn_after):
    def __traverse_rec(node):
      fn_before(node)
      fn_visit(node)
      for child in node.children:
        fn_before_child(child)
        __traverse_rec(child)
      fn_after(node)
    __traverse_rec(tree.root_node)

  _traverse(tree, _fn_before, _fn_visit, _fn_before_child, _fn_after)

  assert len(ast_scope_stack) == 1
  assert len(extra_root) == 1
  return extra_root[0], ann_info


def ast_to_dotgraph(text: str, lang: str) -> None:
  '''easy AST visualizer with https://dreampuf.github.io/GraphvizOnline'''
  def _parse_node(astnode: list):
    '''PRE: astnode is non-terminal'''
    assert isinstance(astnode, list)
    node_type, node_id, children = astnode[0], astnode[1], astnode[2:]
    return node_type, node_id, children
  def _isnt(astnode: Union[list, str]):
    return isinstance(astnode, list)
  def _ist(astnode: Union[list, str]):
    return isinstance(astnode, str)

  def _pre_order(node: list, depth=0):
    ''''''
    assert _isnt(node)
    nonlocal ntnldict, tnldict, edge_template

    ntype, nid, children = _parse_node(node)
    grnname = f'{ntype.split(".")[1]}{nid}'
    grnlabel = f'{ntype.split(".")[1]}'
    ntnldict[grnname] = grnlabel

    for chidx, child in enumerate(children):
      if _isnt(child):
        chtype, chid, chchildren = _parse_node(child)
        chgrnname = f'{chtype.split(".")[1]}{chid}'
        chgrnlabel = f'{chtype.split(".")[1]}'
        ntnldict[chgrnname] = chgrnlabel
        print(depth*indentsize*' ', edge_template.format(grnname, chgrnname), sep='')
        _pre_order(child, depth+1)
      elif _ist(child):
        chgrnname = f'term{nid}_{chidx}'
        chgrnlabel = child.strip('"')
        tnldict[chgrnname] = chgrnlabel
        print(depth*indentsize*' ', edge_template.format(grnname, chgrnname), sep='')

  edge_template = '{} -> {};'
  nt_template = '{} [label="{}"]'
  t_template = '{} [label="{}", shape=square, color=red]'
  indentsize = 4

  ntnldict = {}
  tnldict = {}
  ast, ann = parse_text_dbg(text, lang)

  _pre_order(ast)
  for k, v in ntnldict.items():
    print(nt_template.format(k, v))
  for k, v in tnldict.items():
    print(t_template.format(k, v))
