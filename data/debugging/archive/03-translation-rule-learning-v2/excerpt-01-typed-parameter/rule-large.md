```
(match_expand

  (fragment
    ("py.function_definition"
      str "def"
      ("py.identifier"
        val "f_gold"
      )
      ("py.parameters"
        str "("
        ("py.typed_parameter"
          "py.identifier" "_val_"
          str ":"
          ("py.type"
            ("py.subscript"
              ("py.identifier"
                val "List"
              )
              str "["
              ("py.identifier"
                val "int"
              )
              str "]"
            )
          )
        )
        str ","
        ("py.typed_parameter"
          ("py.identifier"
            val "nums2"
          )
          str ":"
          ("py.type"
            ("py.subscript"
              ("py.identifier"
                val "List"
              )
              str "["
              ("py.identifier"
                val "int"
              )
              str "]"
            )
          )
        )
        str ")"
      )
      str "->"
      ("py.type"
        ("py.identifier"
          val "float"
        )
      )
      str ":"
      ("py.block"
        ("py.expression_statement"
          ("py.call"
            ("py.identifier"
              val "some_secret_fn_4071"
            )
            ("py.argument_list"
              str "("
              str ")"
            )
          )
        )
      )
    )
    "*"
  )

  (fragment
    ("js.function_declaration"
      str "function"
      ("js.identifier"
        val "f_gold"
      )
      ("js.formal_parameters"
        str "("
        "js.identifier" "_val1_"
        str ","
        ("js.identifier"
          val "nums2"
        )
        str ")"
      )
      ("js.statement_block"
        str "{"
        ("js.expression_statement"
          ("js.call_expression"
            ("js.identifier"
              val "some_secret_fn_4071"
            )
            ("js.arguments"
              str "("
              str ")"
            )
          )
          str ";"
        )
        str "}"
      )
    )
    "*1"
  )

)
```