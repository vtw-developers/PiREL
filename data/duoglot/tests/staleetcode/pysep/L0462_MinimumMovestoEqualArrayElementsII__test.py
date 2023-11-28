from L0462_MinimumMovestoEqualArrayElementsII import f_gold

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
    # output: 2
    # EXPLANATION:  Only two moves are needed (remember each move increments or decrements one element): [<u>1</u>,2,3]  =>  [2,2,<u>3</u>]  =>  [2,2,2]
    ,
    # example 2
    [[1, 10, 2, 9]]
    # output: 16
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
