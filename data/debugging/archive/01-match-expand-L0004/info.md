# source
```
print('hi')
```

# 6 rules
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

# 3 rules
```
(match_expand 
  (fragment ("py.module" "*"))
  (fragment ("js.program" "*1")))

(match_expand
  (fragment ("py.expression_statement" "*") "*")
  (fragment ("js.expression_statement" "*1") "*2"))

(match_expand 
  (fragment ("py.call" ("py.identifier" (val "print")) ("py.argument_list" (str "(") ("py.string" (str "\"") ("py.string_content" "_val_") (str "\"")) (str ")"))) "*")
  (fragment ("js.call_expression" ("js.member_expression" ("js.identifier" (val "console")) (str ".") ("js.property_identifier" (val "log"))) ("js.arguments" (str "(") ("js.string" (str "'") ("js.string_fragment" "_val1_") (str "'")) (str ")"))) (str ";") "*1")
)
```