```
(match_expand 
  (fragment ("py.module" "*"))
  (fragment ("js.program" "*1")))

(match_expand
  (fragment ("py.expression_statement" "*") "*")
  (fragment ("js.lexical_declaration" "*1") "*2"))

(match_expand
  (fragment ("py.assignment" "*") "*")
  (fragment ("js.variable_declarator" "*1") "*2"))

(match_expand
  (fragment ("py.identifier" "_val_") "*")
  (fragment ("js.identifier" "_val1_") "*1"))

(match_expand
  (fragment ("py.integer" "_val_") "*")
  (fragment ("js.number" "_val1_") "*1"))

(match_expand
  (fragment ("py.expression_statement" "*") "*")
  (fragment ("js.lexical_declaration" "*1") "*2"))

(match_expand
  (fragment ("py.assignment" "*") "*")
  (fragment ("js.variable_declarator" "*1") "*2"))

(match_expand
  (fragment ("py.identifier" "_val_") "*")
  (fragment ("js.identifier" "_val1_") "*1"))

(match_expand
  (fragment ("py.integer" "_val_") "*")
  (fragment ("js.number" "_val1_") "*1"))

(match_expand
  (fragment ("py.expression_statement" "*") "*")
  (fragment ("js.lexical_declaration" "*1") "*2"))

(match_expand
  (fragment ("py.assignment" "*") "*")
  (fragment ("js.variable_declarator" "*1") "*2"))

(match_expand
  (fragment ("py.identifier" "_val_") "*")
  (fragment ("js.identifier" "_val1_") "*1"))

(match_expand
  (fragment ("py.binary_operator" "." "_str_" ".") "*")
  (fragment ("js.parenthesized_expression" (str "(") ("js.binary_expression" ".1" "_str1_" ".2") (str ")")) "*3"))

(match_expand
  (fragment ("py.parenthesized_expression" "*") "*")
  (fragment ("js.parenthesized_expression" "*1") "*2"))

(match_expand
  (fragment ("py.binary_operator" "." "_str_" ".") "*")
  (fragment ("js.parenthesized_expression" (str "(") ("js.binary_expression" ".1" "_str1_" ".2") (str ")")) "*3"))

(match_expand
  (fragment ("py.identifier" "_val_") "*")
  (fragment ("js.identifier" "_val1_") "*1"))

(match_expand
  (fragment ("py.identifier" "_val_") "*")
  (fragment ("js.identifier" "_val1_") "*1"))

(match_expand
  (fragment ("py.identifier" "_val_") "*")
  (fragment ("js.identifier" "_val1_") "*1"))

(match_expand
  (fragment ("py.if_statement" ("py.parenthesized_expression" ".") "*") "*")
  (fragment ("js.if_statement" ("js.parenthesized_expression" ".1") "*2") "*3"))

(match_expand
  (fragment ("py.comparison_operator" "." (str "==") ".") "*")
  (fragment ("js.binary_expression" ".1" (str "===") ".2") "*3"))

(match_expand
  (fragment ("py.identifier" "_val_") "*")
  (fragment ("js.identifier" "_val1_") "*1"))

(match_expand
  (fragment ("py.integer" "_val_") "*")
  (fragment ("js.number" "_val1_") "*1"))

(match_expand
  (fragment ("py.block" "*") "*")
  (fragment ("js.statement_block" "*1") "*2"))

(match_expand
  (fragment ("py.expression_statement" "*") "*")
  (fragment ("js.lexical_declaration" "*1") "*2"))

(match_expand
  (fragment ("py.assignment" "*") "*")
  (fragment ("js.variable_declarator" "*1") "*2"))

(match_expand
  (fragment ("py.identifier" "_val_") "*")
  (fragment ("js.identifier" "_val1_") "*1"))

(match_expand
  (fragment ("py.binary_operator" "." "_str_" ".") "*")
  (fragment ("js.parenthesized_expression" (str "(") ("js.binary_expression" ".1" "_str1_" ".2") (str ")")) "*3"))

(match_expand
  (fragment ("py.identifier" "_val_") "*")
  (fragment ("js.identifier" "_val1_") "*1"))

(match_expand
  (fragment ("py.identifier" "_val_") "*")
  (fragment ("js.identifier" "_val1_") "*1"))
```