from L0207_CourseSchedule import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2, [[1, 0]]]
    # output: true
    # EXPLANATION:  There are a total of 2 courses to take.  To take course 1 you should have finished course 0. So it is possible.
    ,
    # example 2
    [2, [[1, 0], [0, 1]]]
    # output: false
    # EXPLANATION:  There are a total of 2 courses to take.  To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
