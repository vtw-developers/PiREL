from L1446_ConsecutiveCharacters import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["leetcode"]
    # output: 2
    # EXPLANATION:  The substring "ee" is of length 2 with the character 'e' only.
    ,
    # example 2
    ["abbcccddddeeeeedcba"]
    # output: 5
    # EXPLANATION:  The substring "eeeee" is of length 5 with the character 'e' only.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
