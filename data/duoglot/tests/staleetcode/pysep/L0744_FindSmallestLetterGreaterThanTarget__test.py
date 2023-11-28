from L0744_FindSmallestLetterGreaterThanTarget import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["c", "f", "j"], "a"]
    # output: "c"
    ,
    # example 2
    [["c", "f", "j"], "c"]
    # output: "f"
    ,
    # example 3
    [["c", "f", "j"], "d"]
    # output: "f"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
