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
```