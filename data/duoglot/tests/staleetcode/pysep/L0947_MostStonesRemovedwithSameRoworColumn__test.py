from L0947_MostStonesRemovedwithSameRoworColumn import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]]
    # output: 5
    # EXPLANATION:  One way to remove 5 stones is as follows: 1. Remove stone [2,2] because it shares the same row as [2,1]. 2. Remove stone [2,1] because it shares the same column as [0,1]. 3. Remove stone [1,2] because it shares the same row as [1,0]. 4. Remove stone [1,0] because it shares the same column as [0,0]. 5. Remove stone [0,1] because it shares the same row as [0,0]. Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
    ,
    # example 2
    [[[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]]
    # output: 3
    # EXPLANATION:  One way to make 3 moves is as follows: 1. Remove stone [2,2] because it shares the same row as [2,0]. 2. Remove stone [2,0] because it shares the same column as [0,0]. 3. Remove stone [0,2] because it shares the same row as [0,0]. Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.
    ,
    # example 3
    [[[0, 0]]]
    # output: 0
    # EXPLANATION:  [0,0] is the only stone on the plane, so you cannot remove it.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
