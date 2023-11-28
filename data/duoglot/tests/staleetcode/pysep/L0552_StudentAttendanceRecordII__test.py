from L0552_StudentAttendanceRecordII import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2]
    # output: 8
    # EXPLANATION:  There are 8 records with length 2 that are eligible for an award: "PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL" Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).
    ,
    # example 2
    [1]
    # output: 3
    ,
    # example 3
    [10101]
    # output: 183236316
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
