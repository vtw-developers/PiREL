(match_expand

  (fragment
    ("py.expression_statement"
      ("py.assignment"
        ("py.identifier"
          val "midVal1"
        )
        str "="
        ("py.conditional_expression"
          "."
          str "if"
          "."
          str "else"
          "."
        )
      )
    )
    "*"
  )

  (fragment
    ("js.lexical_declaration"
      str "let"
      ("js.variable_declarator"
        ("js.identifier"
          val "midVal1"
        )
        str "="
        ("js.ternary_expression"
          ".2"
          str "?"
          ".1"
          str ":"
          ".3"
        )
      )
      str ";"
    )
    "*4"
  )

)

(match_expand
  (fragment ("py.expression_statement" ("py.assignment" ("py.identifier" (val "midVal1")) (str "=") ("py.conditional_expression" "." (str "if") "." (str "else") "."))) "*")
  (fragment ("js.lexical_declaration" (str "let") ("js.variable_declarator" ("js.identifier" (val "midVal1")) (str "=") ("js.ternary_expression" ".2" (str "?") ".1" (str ":") ".3")) (str ";")) "*4")
)


this is including context
after removing context:

(match_expand

  (fragment
    ("py.conditional_expression"
      "."
      str "if"
      "."
      str "else"
      "."
    )
    "*"
  )

  (fragment
    ("js.ternary_expression"
      ".2"
      str "?"
      ".1"
      str ":"
      ".3"
    )
    "*4"
  )

)


(match_expand
  (fragment ("py.conditional_expression" "." (str "if") "." (str "else") ".") "*")
  (fragment ("js.ternary_expression" ".2" (str "?") ".1" (str ":") ".3") "*1")
)