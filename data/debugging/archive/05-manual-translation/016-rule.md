(match_expand
  (fragment ("py.expression_statement" ("py.assignment" ("py.identifier" (val "midVal1")) (str "=") ("py.conditional_expression" ("py.subscript" ("py.identifier" (val "nums1")) (str "[") ("py.binary_operator" ("py.binary_operator" ("py.identifier" (val "i")) (str "+") ("py.binary_operator" ("py.identifier" (val "k")) (str "//") ("py.integer" (val "2")))) (str "-") ("py.integer" (val "1"))) (str "]")) (str "if") ("py.comparison_operator" "." (str "<") ".") (str "else") ("py.call" ("py.identifier" (val "float")) ("py.argument_list" (str "(") ("py.string" (str "\"") ("py.string_content" (val "inf")) (str "\"")) (str ")")))))) "*")
  (fragment ("js.lexical_declaration" (str "let") ("js.variable_declarator" ("js.identifier" (val "midVal1")) (str "=") ("js.ternary_expression" ("js.binary_expression" ".1" (str "<") ".2") (str "?") ("js.subscript_expression" ("js.identifier" (val "nums1")) (str "[") ("js.binary_expression" ("js.binary_expression" ("js.identifier" (val "i")) (str "+") ("js.call_expression" ("js.member_expression" ("js.identifier" (val "Math")) (str ".") ("js.property_identifier" (val "floor"))) ("js.arguments" (str "(") ("js.binary_expression" ("js.identifier" (val "k")) (str "/") ("js.number" (val "2"))) (str ")")))) (str "-") ("js.number" (val "1"))) (str "]")) (str ":") ".1")) (str ";")) "*3")
)






(match_expand
  (fragment ("py.comparison_operator" "." (str "<") ".") "*")
  (fragment ("js.binary_expression" ".1" (str "<") ".2") "*1")
)