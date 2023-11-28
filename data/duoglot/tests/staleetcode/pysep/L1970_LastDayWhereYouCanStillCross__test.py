from L1970_LastDayWhereYouCanStillCross import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2, 2, [[1, 1], [2, 1], [1, 2], [2, 2]]]
    # output: 2
    # EXPLANATION:  The above image depicts how the matrix changes each day starting from day 0. The last day where it is possible to cross from top to bottom is on day 2.
    ,
    # example 2
    [2, 2, [[1, 1], [1, 2], [2, 1], [2, 2]]]
    # output: 1
    # EXPLANATION:  The above image depicts how the matrix changes each day starting from day 0. The last day where it is possible to cross from top to bottom is on day 1.
    ,
    # example 3
    [3, 3, [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]]
    # output: 3
    # EXPLANATION:  The above image depicts how the matrix changes each day starting from day 0. The last day where it is possible to cross from top to bottom is on day 3.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
