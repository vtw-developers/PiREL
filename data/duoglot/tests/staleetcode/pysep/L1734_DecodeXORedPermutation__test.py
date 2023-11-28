from L1734_DecodeXORedPermutation import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 1]]
    # output: [1,2,3]
    # EXPLANATION:  If perm = [1,2,3], then encoded = [1 XOR 2,2 XOR 3] = [3,1]
    ,
    # example 2
    [[6, 5, 4, 6]]
    # output: [2,4,1,5,3]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
