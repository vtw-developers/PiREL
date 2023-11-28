from L0583_DeleteOperationforTwoStrings import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["sea", "eat"]
    # output: 2
    # EXPLANATION:  You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
    ,
    # example 2
    ["leetcode", "etco"]
    # output: 4
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
