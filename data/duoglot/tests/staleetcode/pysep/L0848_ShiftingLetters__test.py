from L0848_ShiftingLetters import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abc", [3, 5, 9]]
    # output: "rpl"
    # EXPLANATION:  We start with "abc". After shifting the first 1 letters of s by 3, we have "dbc". After shifting the first 2 letters of s by 5, we have "igc". After shifting the first 3 letters of s by 9, we have "rpl", the answer.
    ,
    # example 2
    ["aaa", [1, 2, 3]]
    # output: "gfd"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
