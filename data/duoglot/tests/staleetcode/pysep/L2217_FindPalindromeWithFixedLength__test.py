from L2217_FindPalindromeWithFixedLength import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4, 5, 90], 3]
    # output: [101,111,121,131,141,999]
    # EXPLANATION:  The first few palindromes of length 3 are: 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, ... The 90<sup>th</sup> palindrome of length 3 is 999.
    ,
    # example 2
    [[2, 4, 6], 4]
    # output: [1111,1331,1551]
    # EXPLANATION:  The first six palindromes of length 4 are: 1001, 1111, 1221, 1331, 1441, and 1551.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
