from tree_sitter import Language, Parser

language_paths = [
  "./tree-sitter-util/tree-sitter-javascript",
  "./tree-sitter-util/tree-sitter-python",
]

Language.build_library("build/my-languages.so", language_paths)

PY_LANGUAGE = Language("build/my-languages.so", "python")
JS_LANGUAGE = Language("build/my-languages.so", "javascript")

language_dict = {
  'py': PY_LANGUAGE,
  'js': JS_LANGUAGE
}


def has_parse_error(content: str, parser=None, lang=None):
  '''
  As name suggests, use a Tree-sitter parser to parse `content`.
  Return True if there are no parse errors, False otherwise.

  PARAMS
  Pass either `parser` or `lang`.
  '''

  if parser is None:
    assert lang in language_dict
    parser = Parser()
    parser.set_language(language_dict[lang])

  assert parser is not None

  tree = parser.parse(bytes(content, 'utf8'))
  root_node = tree.root_node
  return root_node.has_error


def get_tree_sitter_ast(parser: Parser, content: str):
  '''
  Given a Parser and some `content` to parse,
  parse the `content` and return a root node of the AST.
  '''
  tree = parser.parse(bytes(content, 'utf8'))
  root_node = tree.root_node
  return root_node
