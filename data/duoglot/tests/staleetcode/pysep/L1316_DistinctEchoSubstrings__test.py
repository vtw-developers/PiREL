from L1316_DistinctEchoSubstrings import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abcabcabc"]
    # output: 3
    # EXPLANATION: The 3 substrings are "abcabc", "bcabca" and "cabcab".
    ,
    # example 2
    ["leetcodeleetcode"]
    # output: 2
    # EXPLANATION: The 2 substrings are "ee" and "leetcodeleetcode".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
