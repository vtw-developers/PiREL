from L0243_ShortestWordDistance import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"]
    # output: 3
    ,
    # example 2
    [["practice", "makes", "perfect", "coding", "makes"], "makes", "coding"]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
