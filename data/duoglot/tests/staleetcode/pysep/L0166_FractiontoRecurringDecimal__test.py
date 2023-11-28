from L0166_FractiontoRecurringDecimal import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1, 2]
    # output: "0.5"
    ,
    # example 2
    [2, 1]
    # output: "2"
    ,
    # example 3
    [4, 333]
    # output: "0.(012)"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
