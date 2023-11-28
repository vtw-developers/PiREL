from L0014_LongestCommonPrefix import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["flower", "flow", "flight"]]
    # output: "fl"
    ,
    # example 2
    [["dog", "racecar", "car"]]
    # output: ""
    # EXPLANATION:  There is no common prefix among the input strings.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
