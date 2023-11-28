from L0693_BinaryNumberwithAlternatingBits import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [5]
    # output: true
    # EXPLANATION:  The binary representation of 5 is: 101
    ,
    # example 2
    [7]
    # output: false
    # EXPLANATION:  The binary representation of 7 is: 111.
    ,
    # example 3
    [11]
    # output: false
    # EXPLANATION:  The binary representation of 11 is: 1011.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
