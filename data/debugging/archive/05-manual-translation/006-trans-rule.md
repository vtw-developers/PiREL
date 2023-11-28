(match_expand

  (fragment
    ("py.expression_statement"
      ("py.assignment"
        "py.identifier" "_val_"
        str "="
        "."
      )
    )
    "*"
  )

  (fragment
    ("js.lexical_declaration"
      str "let"
      ("js.variable_declarator"
        "js.identifier" "_val1_"
        str "="
        "js.number" "_val1_"
      )
      str ";"
    )
    "*2"
  )

)




this is not a rule that we want to learn...

int and float in python
are number in js