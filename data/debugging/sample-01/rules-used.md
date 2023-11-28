```
(match_expand 
  (fragment ("py.module" "*"))
  (fragment ("js.program" "*1")))

(match_expand
  (fragment ("py.expression_statement" "*") "*")
  (fragment ("js.expression_statement" "*1") "*2"))

(match_expand
  (fragment ("py.call" ("py.identifier" (val "print")) ".") "*")
  (fragment ("js.call_expression" ("js.member_expression" ("js.identifier" (val "console"))  ("js.property_identifier" (val "log"))) ".1") "*2"))

(match_expand
  (fragment ("py.argument_list" "*") "*")
  (fragment ("js.arguments" "*1") "*2"))

(match_expand
  (fragment ("py.string" "*") "*")
  (fragment ("js.string" "*1") "*2"))

(match_expand
  (fragment ("py.string_content" "_val_") "*")
  (fragment ("js.string_fragment" "_val1_") "*1"))
```