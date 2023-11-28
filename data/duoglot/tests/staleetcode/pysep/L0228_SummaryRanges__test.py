from L0228_SummaryRanges import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[0, 1, 2, 4, 5, 7]]
    # output: ["0->2","4->5","7"]
    # EXPLANATION:  The ranges are: [0,2] --> "0->2" [4,5] --> "4->5" [7,7] --> "7"
    ,
    # example 2
    [[0, 2, 3, 4, 6, 8, 9]]
    # output: ["0","2->4","6","8->9"]
    # EXPLANATION:  The ranges are: [0,0] --> "0" [2,4] --> "2->4" [6,6] --> "6" [8,9] --> "8->9"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
