# on its own
```py
array[i + k // 2 - 1] if i + k // 2 - 1 < m else float('inf')
```

```
module [0, 0] - [1, 0]
  expression_statement [0, 0] - [0, 61]
    conditional_expression [0, 0] - [0, 61]
      subscript [0, 0] - [0, 21]
        value: identifier [0, 0] - [0, 5]
        subscript: binary_operator [0, 6] - [0, 20]
          left: binary_operator [0, 6] - [0, 16]
            left: identifier [0, 6] - [0, 7]
            right: binary_operator [0, 10] - [0, 16]
              left: identifier [0, 10] - [0, 11]
              right: integer [0, 15] - [0, 16]
          right: integer [0, 19] - [0, 20]
      comparison_operator [0, 25] - [0, 43]
        binary_operator [0, 25] - [0, 39]
          left: binary_operator [0, 25] - [0, 35]
            left: identifier [0, 25] - [0, 26]
            right: binary_operator [0, 29] - [0, 35]
              left: identifier [0, 29] - [0, 30]
              right: integer [0, 34] - [0, 35]
          right: integer [0, 38] - [0, 39]
        identifier [0, 42] - [0, 43]
      call [0, 49] - [0, 61]
        function: identifier [0, 49] - [0, 54]
        arguments: argument_list [0, 54] - [0, 61]
          string [0, 55] - [0, 60]
```


# as part of the whole program
```py
### findMedianSortedArrays 
import math
from math import inf
from typing import *
def f_gold(nums1: List[int], nums2: List[int]) -> float:
    def findKth(i, j, k):
        if i >= m:
            return nums2[j + k - 1]
        if j >= n:
            return nums1[i + k - 1]
        if k == 1:
            return min(nums1[i], nums2[j])
        midVal1 = nums1[i + k // 2 - 1] if i + k // 2 - 1 < m else float('inf')
        midVal2 = nums2[j + k // 2 - 1] if j + k // 2 - 1 < n else float('inf')
        if midVal1 < midVal2:
            return findKth(i + k // 2, j, k - k // 2)
        return findKth(i, j + k // 2, k - k // 2)
    m, n = len(nums1), len(nums2)
    left, right = (m + n + 1) // 2, (m + n + 2) // 2
    return (findKth(0, 0, left) + findKth(0, 0, right)) / 2
```

```
          expression_statement [12, 8] - [12, 79]
            assignment [12, 8] - [12, 79]
              left: identifier [12, 8] - [12, 15]
              right: conditional_expression [12, 18] - [12, 79]
                subscript [12, 18] - [12, 39]
                  value: identifier [12, 18] - [12, 23]
                  subscript: binary_operator [12, 24] - [12, 38]
                    left: binary_operator [12, 24] - [12, 34]
                      left: identifier [12, 24] - [12, 25]
                      right: binary_operator [12, 28] - [12, 34]
                        left: identifier [12, 28] - [12, 29]
                        right: integer [12, 33] - [12, 34]
                    right: integer [12, 37] - [12, 38]
                comparison_operator [12, 43] - [12, 61]
                  binary_operator [12, 43] - [12, 57]
                    left: binary_operator [12, 43] - [12, 53]
                      left: identifier [12, 43] - [12, 44]
                      right: binary_operator [12, 47] - [12, 53]
                        left: identifier [12, 47] - [12, 48]
                        right: integer [12, 52] - [12, 53]
                    right: integer [12, 56] - [12, 57]
                  identifier [12, 60] - [12, 61]
                call [12, 67] - [12, 79]
                  function: identifier [12, 67] - [12, 72]
                  arguments: argument_list [12, 72] - [12, 79]
                    string [12, 73] - [12, 78]
```

# rule - largest node
```
(match_expand

  (fragment
    ("py.expression_statement"
      ("py.conditional_expression"
        ("py.subscript"
          "py.identifier" "_val_"
          str "["
          ("py.binary_operator"
            ("py.binary_operator"
              ("py.identifier"
                val "i"
              )
              str "+"
              ("py.binary_operator"
                ("py.identifier"
                  val "k"
                )
                str "//"
                ("py.integer"
                  val "2"
                )
              )
            )
            str "-"
            ("py.integer"
              val "1"
            )
          )
          str "]"
        )
        str "if"
        ("py.comparison_operator"
          ("py.binary_operator"
            ("py.binary_operator"
              ("py.identifier"
                val "i"
              )
              str "+"
              ("py.binary_operator"
                ("py.identifier"
                  val "k"
                )
                str "//"
                ("py.integer"
                  val "2"
                )
              )
            )
            str "-"
            ("py.integer"
              val "1"
            )
          )
          str "<"
          ("py.identifier"
            val "m"
          )
        )
        str "else"
        ("py.call"
          ("py.identifier"
            val "float"
          )
          ("py.argument_list"
            str "("
            ("py.string"
              (ERROR_NT_OR_FRAGMENT_EXPECTED
              )
              str "\""
              ("py.string_content"
                val "inf"
              )
              str "\""
            )
            str ")"
          )
        )
      )
    )
    "*"
  )

  (fragment
    ("js.expression_statement"
      ("js.ternary_expression"
        ("js.binary_expression"
          ("js.subscript_expression"
            "js.identifier" "_val1_"
            str "["
            ("js.binary_expression"
              ("js.binary_expression"
                ("js.identifier"
                  val "i"
                )
                str "+"
                ("js.call_expression"
                  ("js.member_expression"
                    ("js.identifier"
                      val "Math"
                    )
                    str "."
                    ("js.property_identifier"
                      val "floor"
                    )
                  )
                  ("js.arguments"
                    str "("
                    ("js.binary_expression"
                      ("js.identifier"
                        val "k"
                      )
                      str "/"
                      ("js.number"
                        val "2"
                      )
                    )
                    str ")"
                  )
                )
              )
              str "-"
              ("js.number"
                val "1"
              )
            )
            str "]"
          )
          str "<"
          ("js.identifier"
            val "m"
          )
        )
        str "?"
        ("js.subscript_expression"
          "js.identifier" "_val1_"
          str "["
          ("js.binary_expression"
            ("js.binary_expression"
              ("js.identifier"
                val "i"
              )
              str "+"
              ("js.call_expression"
                ("js.member_expression"
                  ("js.identifier"
                    val "Math"
                  )
                  str "."
                  ("js.property_identifier"
                    val "floor"
                  )
                )
                ("js.arguments"
                  str "("
                  ("js.binary_expression"
                    ("js.identifier"
                      val "k"
                    )
                    str "/"
                    ("js.number"
                      val "2"
                    )
                  )
                  str ")"
                )
              )
            )
            str "-"
            ("js.number"
              val "1"
            )
          )
          str "]"
        )
        str ":"
        ("js.identifier"
          val "Infinity"
        )
      )
    )
    "*1"
  )

)
```

# rule - smallest node
```
(match_expand

  (fragment
    ("py.conditional_expression"
      ("py.subscript"
        "py.identifier" "_val_"
        str "["
        ("py.binary_operator"
          ("py.binary_operator"
            ("py.identifier"
              val "i"
            )
            str "+"
            ("py.binary_operator"
              ("py.identifier"
                val "k"
              )
              str "//"
              ("py.integer"
                val "2"
              )
            )
          )
          str "-"
          ("py.integer"
            val "1"
          )
        )
        str "]"
      )
      str "if"
      ("py.comparison_operator"
        ("py.binary_operator"
          ("py.binary_operator"
            ("py.identifier"
              val "i"
            )
            str "+"
            ("py.binary_operator"
              ("py.identifier"
                val "k"
              )
              str "//"
              ("py.integer"
                val "2"
              )
            )
          )
          str "-"
          ("py.integer"
            val "1"
          )
        )
        str "<"
        ("py.identifier"
          val "m"
        )
      )
      str "else"
      ("py.call"
        ("py.identifier"
          val "float"
        )
        ("py.argument_list"
          str "("
          ("py.string"
            (ERROR_NT_OR_FRAGMENT_EXPECTED
            )
            str "\""
            ("py.string_content"
              val "inf"
            )
            str "\""
          )
          str ")"
        )
      )
    )
    "*"
  )

  (fragment
    ("js.ternary_expression"
      ("js.binary_expression"
        ("js.subscript_expression"
          "js.identifier" "_val1_"
          str "["
          ("js.binary_expression"
            ("js.binary_expression"
              ("js.identifier"
                val "i"
              )
              str "+"
              ("js.call_expression"
                ("js.member_expression"
                  ("js.identifier"
                    val "Math"
                  )
                  str "."
                  ("js.property_identifier"
                    val "floor"
                  )
                )
                ("js.arguments"
                  str "("
                  ("js.binary_expression"
                    ("js.identifier"
                      val "k"
                    )
                    str "/"
                    ("js.number"
                      val "2"
                    )
                  )
                  str ")"
                )
              )
            )
            str "-"
            ("js.number"
              val "1"
            )
          )
          str "]"
        )
        str "<"
        ("js.identifier"
          val "m"
        )
      )
      str "?"
      ("js.subscript_expression"
        "js.identifier" "_val1_"
        str "["
        ("js.binary_expression"
          ("js.binary_expression"
            ("js.identifier"
              val "i"
            )
            str "+"
            ("js.call_expression"
              ("js.member_expression"
                ("js.identifier"
                  val "Math"
                )
                str "."
                ("js.property_identifier"
                  val "floor"
                )
              )
              ("js.arguments"
                str "("
                ("js.binary_expression"
                  ("js.identifier"
                    val "k"
                  )
                  str "/"
                  ("js.number"
                    val "2"
                  )
                )
                str ")"
              )
            )
          )
          str "-"
          ("js.number"
            val "1"
          )
        )
        str "]"
      )
      str ":"
      ("js.identifier"
        val "Infinity"
      )
    )
    "*1"
  )

)
```