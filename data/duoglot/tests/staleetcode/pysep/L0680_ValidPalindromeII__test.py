from L0680_ValidPalindromeII import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["aba"]
    # output: true
    ,
    # example 2
    ["abca"]
    # output: true
    # EXPLANATION:  You could delete the character 'c'.
    ,
    # example 3
    ["abc"]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
