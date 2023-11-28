from L0925_LongPressedName import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["alex", "aaleex"]
    # output: true
    # EXPLANATION: 'a' and 'e' in 'alex' were long pressed.
    ,
    # example 2
    ["saeed", "ssaaedd"]
    # output: false
    # EXPLANATION: 'e' must have been pressed twice, but it was not in the typed output.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
