from L1002_FindCommonCharacters import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["bella", "label", "roller"]]
    # output: ["e","l","l"]
    ,
    # example 2
    [["cool", "lock", "cook"]]
    # output: ["c","o"]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
