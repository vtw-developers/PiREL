from L1181_BeforeandAfterPuzzle import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["writing code", "code rocks"]]
    # output: ["writing code rocks"]
    ,
    # example 2
    [["mission statement", "a quick bite to eat", "a chip off the old block", "chocolate bar", "mission impossible", "a man on a mission", "block party", "eat my words", "bar of soap"]]
    # output: ["a chip off the old block party",         "a man on a mission impossible",         "a man on a mission statement",         "a quick bite to eat my words",         "chocolate bar of soap"]
    ,
    # example 3
    [["a", "b", "a"]]
    # output: ["a"]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
