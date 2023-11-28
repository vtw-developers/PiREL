from L0269_AlienDictionary import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["wrt", "wrf", "er", "ett", "rftt"]]
    # output: "wertf"
    ,
    # example 2
    [["z", "x"]]
    # output: "zx"
    ,
    # example 3
    [["z", "x", "z"]]
    # output: ""
    # EXPLANATION:  The order is invalid, so return <code>""</code>.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
