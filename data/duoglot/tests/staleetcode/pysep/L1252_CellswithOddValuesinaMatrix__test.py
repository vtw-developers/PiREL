from L1252_CellswithOddValuesinaMatrix import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2, 3, [[0, 1], [1, 1]]]
    # output: 6
    # EXPLANATION:  Initial matrix = [[0,0,0],[0,0,0]]. After applying first increment it becomes [[1,2,1],[0,1,0]]. The final matrix is [[1,3,1],[1,3,1]], which contains 6 odd numbers.
    ,
    # example 2
    [2, 2, [[1, 1], [0, 0]]]
    # output: 0
    # EXPLANATION:  Final matrix = [[2,2],[2,2]]. There are no odd numbers in the final matrix.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
