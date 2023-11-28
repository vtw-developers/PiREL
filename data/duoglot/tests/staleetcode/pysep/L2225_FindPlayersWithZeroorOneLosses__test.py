from L2225_FindPlayersWithZeroorOneLosses import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]]
    # output: [[1,2,10],[4,5,7,8]]
    # EXPLANATION:  Players 1, 2, and 10 have not lost any matches. Players 4, 5, 7, and 8 each have lost one match. Players 3, 6, and 9 each have lost two matches. Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
    ,
    # example 2
    [[[2, 3], [1, 3], [5, 4], [6, 4]]]
    # output: [[1,2,5,6],[]]
    # EXPLANATION:  Players 1, 2, 5, and 6 have not lost any matches. Players 3 and 4 each have lost two matches. Thus, answer[0] = [1,2,5,6] and answer[1] = [].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
