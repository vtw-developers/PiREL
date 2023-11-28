# function definition
```
(match_expand
  (fragment ("py.function_definition" (str "def") ("py.identifier" (val "f_gold")) ("py.parameters" (str "(") ("py.typed_parameter" ("py.identifier" (val "nums1")) (str ":") ("py.type" ("py.subscript" ("py.identifier" (val "List")) (str "[") ("py.identifier" "_val_") (str "]")))) (str ",") ("py.typed_parameter" ("py.identifier" (val "nums2")) (str ":") ("py.type" ("py.subscript" ("py.identifier" (val "List")) (str "[") ("py.identifier" (val "int")) (str "]")))) (str ")")) (str "->") ("py.type" ("py.identifier" (val "float"))) (str ":") ("py.block" "*")) "*")
  (fragment ("js.function_declaration" (str "function") ("js.identifier" (val "f_gold")) ("js.formal_parameters" (str "(") ("js.identifier" (val "nums1")) (str ",") ("js.identifier" (val "nums2")) (str ")")) ("js.statement_block" (str "{") "*1" (str "}"))) "*2")
)
```

# rule for list comprehension (works - whole assignment_statement)
```
(match_expand
  (fragment ("py.expression_statement" ("py.assignment" ("py.identifier" (val "midVal1")) (str "=") ("py.conditional_expression" ("py.subscript" ("py.identifier" "_val_") (str "[") ("py.binary_operator" ("py.binary_operator" ("py.identifier" (val "i")) (str "+") ("py.binary_operator" ("py.identifier" (val "k")) (str "//") ("py.integer" (val "2")))) (str "-") ("py.integer" (val "1"))) (str "]")) (str "if") ("py.comparison_operator" ("py.binary_operator" ("py.binary_operator" ("py.identifier" (val "i")) (str "+") ("py.binary_operator" ("py.identifier" (val "k")) (str "//") ("py.integer" (val "2")))) (str "-") ("py.integer" (val "1"))) (str "<") ("py.identifier" (val "m"))) (str "else") ("py.call" ("py.identifier" (val "float")) ("py.argument_list" (str "(") ("py.string" (str "\"") ("py.string_content" (val "inf")) (str "\"")) (str ")")))))) "*")
  (fragment ("js.expression_statement" ("js.assignment_expression" ("js.identifier" (val "midVal1")) (str "=") ("js.ternary_expression" ("js.binary_expression" ("js.subscript_expression" ("js.identifier" "_val1_") (str "[") ("js.binary_expression" ("js.binary_expression" ("js.identifier" (val "i")) (str "+") ("js.call_expression" ("js.member_expression" ("js.identifier" (val "Math")) (str ".") ("js.property_identifier" (val "floor"))) ("js.arguments" (str "(") ("js.binary_expression" ("js.identifier" (val "k")) (str "/") ("js.number" (val "2"))) (str ")")))) (str "-") ("js.number" (val "1"))) (str "]")) (str "<") ("js.identifier" (val "m"))) (str "?") ("js.subscript_expression" ("js.identifier" "_val1_") (str "[") ("js.binary_expression" ("js.binary_expression" ("js.identifier" (val "i")) (str "+") ("js.call_expression" ("js.member_expression" ("js.identifier" (val "Math")) (str ".") ("js.property_identifier" (val "floor"))) ("js.arguments" (str "(") ("js.binary_expression" ("js.identifier" (val "k")) (str "/") ("js.number" (val "2"))) (str ")")))) (str "-") ("js.number" (val "1"))) (str "]")) (str ":") ("js.identifier" (val "Infinity")))) (str ";")) "*1")
)
```

# rule for list comprehension (works - ternary_expression)
```
(match_expand
  (fragment ("py.conditional_expression" ("py.subscript" ("py.identifier" "_val_") (str "[") ("py.binary_operator" ("py.binary_operator" ("py.identifier" (val "i")) (str "+") ("py.binary_operator" ("py.identifier" (val "k")) (str "//") ("py.integer" (val "2")))) (str "-") ("py.integer" (val "1"))) (str "]")) (str "if") ("py.comparison_operator" ("py.binary_operator" ("py.binary_operator" ("py.identifier" (val "i")) (str "+") ("py.binary_operator" ("py.identifier" (val "k")) (str "//") ("py.integer" (val "2")))) (str "-") ("py.integer" (val "1"))) (str "<") ("py.identifier" (val "m"))) (str "else") ("py.call" ("py.identifier" (val "float")) ("py.argument_list" (str "(") ("py.string" (str "\"") ("py.string_content" (val "inf")) (str "\"")) (str ")")))) "*")
  (fragment ("js.ternary_expression" ("js.binary_expression" ("js.subscript_expression" ("js.identifier" "_val1_") (str "[") ("js.binary_expression" ("js.binary_expression" ("js.identifier" (val "i")) (str "+") ("js.call_expression" ("js.member_expression" ("js.identifier" (val "Math")) (str ".") ("js.property_identifier" (val "floor"))) ("js.arguments" (str "(") ("js.binary_expression" ("js.identifier" (val "k")) (str "/") ("js.number" (val "2"))) (str ")")))) (str "-") ("js.number" (val "1"))) (str "]")) (str "<") ("js.identifier" (val "m"))) (str "?") ("js.subscript_expression" ("js.identifier" "_val1_") (str "[") ("js.binary_expression" ("js.binary_expression" ("js.identifier" (val "i")) (str "+") ("js.call_expression" ("js.member_expression" ("js.identifier" (val "Math")) (str ".") ("js.property_identifier" (val "floor"))) ("js.arguments" (str "(") ("js.binary_expression" ("js.identifier" (val "k")) (str "/") ("js.number" (val "2"))) (str ")")))) (str "-") ("js.number" (val "1"))) (str "]")) (str ":") ("js.identifier" (val "Infinity"))) "*1")
)
```

# rule for list comprehesion (fails - node mismatch source-target)
```
(match_expand
  (fragment ("py.conditional_expression" ("py.subscript" ("py.identifier" "_val_") (str "[") ("py.binary_operator" ("py.binary_operator" ("py.identifier" (val "i")) (str "+") ("py.binary_operator" ("py.identifier" (val "k")) (str "//") ("py.integer" (val "2")))) (str "-") ("py.integer" (val "1"))) (str "]")) (str "if") ("py.comparison_operator" ("py.binary_operator" ("py.binary_operator" ("py.identifier" (val "i")) (str "+") ("py.binary_operator" ("py.identifier" (val "k")) (str "//") ("py.integer" (val "2")))) (str "-") ("py.integer" (val "1"))) (str "<") ("py.identifier" (val "m"))) (str "else") ("py.call" ("py.identifier" (val "float")) ("py.argument_list" (str "(") ("py.string" (str "\"") ("py.string_content" (val "inf")) (str "\"")) (str ")")))) "*")
  (fragment ("js.expression_statement" ("js.ternary_expression" ("js.binary_expression" ("js.subscript_expression" ("js.identifier" "_val1_") (str "[") ("js.binary_expression" ("js.binary_expression" ("js.identifier" (val "i")) (str "+") ("js.call_expression" ("js.member_expression" ("js.identifier" (val "Math")) (str ".") ("js.property_identifier" (val "floor"))) ("js.arguments" (str "(") ("js.binary_expression" ("js.identifier" (val "k")) (str "/") ("js.number" (val "2"))) (str ")")))) (str "-") ("js.number" (val "1"))) (str "]")) (str "<") ("js.identifier" (val "m"))) (str "?") ("js.subscript_expression" ("js.identifier" "_val1_") (str "[") ("js.binary_expression" ("js.binary_expression" ("js.identifier" (val "i")) (str "+") ("js.call_expression" ("js.member_expression" ("js.identifier" (val "Math")) (str ".") ("js.property_identifier" (val "floor"))) ("js.arguments" (str "(") ("js.binary_expression" ("js.identifier" (val "k")) (str "/") ("js.number" (val "2"))) (str ")")))) (str "-") ("js.number" (val "1"))) (str "]")) (str ":") ("js.identifier" (val "Infinity"))) (str ";")) "*1")
)
```

# other rules
are from base_upd_L0004