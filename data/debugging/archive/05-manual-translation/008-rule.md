(match_expand
  (fragment ("py.expression_statement" ("py.assignment" ("py.identifier" "_val_") (str "=") ".")) "*")
  (fragment ("js.lexical_declaration" (str "let") ("js.variable_declarator" ("js.identifier" "_val1_") (str "=") ".1") (str ";")) "*2")
)