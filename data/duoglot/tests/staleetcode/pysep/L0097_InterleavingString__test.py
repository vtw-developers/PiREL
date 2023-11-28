from L0097_InterleavingString import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["aabcc", "dbbca", "aadbbcbcac"]
    # output: true
    ,
    # example 2
    ["aabcc", "dbbca", "aadbbbaccc"]
    # output: false
    ,
    # example 3
    ["", "", ""]
    # output: true
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
