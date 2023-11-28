from L0453_MinimumMovestoEqualArrayElements import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3]]
    # output: 3
    # EXPLANATION:  Only three moves are needed (remember each move increments two elements): [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
    ,
    # example 2
    [[1, 1, 1]]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
