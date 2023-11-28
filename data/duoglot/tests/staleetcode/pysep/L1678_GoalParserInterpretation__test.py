from L1678_GoalParserInterpretation import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["G()(al)"]
    # output: "Goal"
    # EXPLANATION:  The Goal Parser interprets the command as follows: G -> G () -> o (al) -> al The final concatenated result is "Goal".
    ,
    # example 2
    ["G()()()()(al)"]
    # output: "Gooooal"
    ,
    # example 3
    ["(al)G(al)()()G"]
    # output: "alGalooG"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
