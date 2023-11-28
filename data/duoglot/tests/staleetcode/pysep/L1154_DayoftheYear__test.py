from L1154_DayoftheYear import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["2019-01-09"]
    # output: 9
    # EXPLANATION:  Given date is the 9th day of the year in 2019.
    ,
    # example 2
    ["2019-02-10"]
    # output: 41
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
