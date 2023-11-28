from L1376_TimeNeededtoInformAllEmployees import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1, 0, [-1], [0]]
    # output: 0
    # EXPLANATION:  The head of the company is the only employee in the company.
    ,
    # example 2
    [6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0]]
    # output: 1
    # EXPLANATION:  The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all. The tree structure of the employees in the company is shown.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
