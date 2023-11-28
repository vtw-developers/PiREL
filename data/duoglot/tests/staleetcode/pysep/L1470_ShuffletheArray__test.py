from L1470_ShuffletheArray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 5, 1, 3, 4, 7], 3]
    # output: [2,3,5,4,1,7]
    # EXPLANATION:  Since x<sub>1</sub>=2, x<sub>2</sub>=5, x<sub>3</sub>=1, y<sub>1</sub>=3, y<sub>2</sub>=4, y<sub>3</sub>=7 then the answer is [2,3,5,4,1,7].
    ,
    # example 2
    [[1, 2, 3, 4, 4, 3, 2, 1], 4]
    # output: [1,4,2,3,3,2,4,1]
    ,
    # example 3
    [[1, 1, 2, 2], 2]
    # output: [1,2,1,2]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
