from L2191_SorttheJumbledNumbers import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[8, 9, 4, 0, 2, 1, 3, 5, 7, 6], [991, 338, 38]]
    # output: [338,38,991]
    # EXPLANATION:   Map the number 991 as follows: 1. mapping[9] = 6, so all occurrences of the digit 9 will become 6. 2. mapping[1] = 9, so all occurrences of the digit 1 will become 9. Therefore, the mapped value of 991 is 669. 338 maps to 007, or 7 after removing the leading zeros. 38 maps to 07, which is also 7 after removing leading zeros. Since 338 and 38 share the same mapped value, they should remain in the same relative order, so 338 comes before 38. Thus, the sorted array is [338,38,991].
    ,
    # example 2
    [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [789, 456, 123]]
    # output: [123,456,789]
    # EXPLANATION:  789 maps to 789, 456 maps to 456, and 123 maps to 123. Thus, the sorted array is [123,456,789].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
