from L0132_PalindromePartitioningII import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["aab"]
    # output: 1
    # EXPLANATION:  The palindrome partitioning ["aa","b"] could be produced using 1 cut.
    ,
    # example 2
    ["a"]
    # output: 0
    ,
    # example 3
    ["ab"]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
