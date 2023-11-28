from L1723_FindMinimumTimetoFinishAllJobs import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 2, 3], 3]
    # output: 3
    # EXPLANATION:  By assigning each person one job, the maximum time is 3.
    ,
    # example 2
    [[1, 2, 4, 7, 8], 2]
    # output: 11
    # EXPLANATION:  Assign the jobs the following way: Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11) Worker 2: 4, 7 (working time = 4 + 7 = 11) The maximum working time is 11.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
