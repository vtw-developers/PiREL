from L1736_LatestTimebyReplacingHiddenDigits import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["2?:?0"]
    # output: "23:50"
    # EXPLANATION:  The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.
    ,
    # example 2
    ["0?:3?"]
    # output: "09:39"
    ,
    # example 3
    ["1?:22"]
    # output: "19:22"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
