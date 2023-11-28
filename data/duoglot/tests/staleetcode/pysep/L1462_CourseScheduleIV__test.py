from L1462_CourseScheduleIV import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2, [[1, 0]], [[0, 1], [1, 0]]]
    # output: [false,true]
    # EXPLANATION:  The pair [1, 0] indicates that you have to take course 1 before you can take course 0. Course 0 is not a prerequisite of course 1, but the opposite is true.
    ,
    # example 2
    [2, [], [[1, 0], [0, 1]]]
    # output: [false,false]
    # EXPLANATION:  There are no prerequisites, and each course is independent.
    ,
    # example 3
    [3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]]]
    # output: [true,true]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
