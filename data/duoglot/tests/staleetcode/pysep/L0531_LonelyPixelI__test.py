from L0531_LonelyPixelI import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[["W", "W", "B"], ["W", "B", "W"], ["B", "W", "W"]]]
    # output: 3
    # EXPLANATION:  All the three 'B's are black lonely pixels.
    ,
    # example 2
    [[["B", "B", "B"], ["B", "B", "W"], ["B", "B", "B"]]]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
