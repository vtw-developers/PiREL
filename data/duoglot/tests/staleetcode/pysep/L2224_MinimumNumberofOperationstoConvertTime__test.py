from L2224_MinimumNumberofOperationstoConvertTime import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["02:30", "04:35"]
    # output: 3
    # EXPLANATION: We can convert current to correct in 3 operations as follows: - Add 60 minutes to current. current becomes "03:30". - Add 60 minutes to current. current becomes "04:30". - Add 5 minutes to current. current becomes "04:35". It can be proven that it is not possible to convert current to correct in fewer than 3 operations.
    ,
    # example 2
    ["11:00", "11:01"]
    # output: 1
    # EXPLANATION:  We only have to add one minute to current, so the minimum number of operations needed is 1.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
