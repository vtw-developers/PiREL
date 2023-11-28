from L0389_FindtheDifference import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abcd", "abcde"]
    # output: "e"
    # EXPLANATION:  'e' is the letter that was added.
    ,
    # example 2
    ["", "y"]
    # output: "y"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
