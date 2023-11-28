from L0551_StudentAttendanceRecordI import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["PPALLP"]
    # output: true
    # EXPLANATION:  The student has fewer than 2 absences and was never late 3 or more consecutive days.
    ,
    # example 2
    ["PPALLL"]
    # output: false
    # EXPLANATION:  The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
