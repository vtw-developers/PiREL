from L1559_DetectCyclesin2DGrid import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[["a", "a", "a", "a"], ["a", "b", "b", "a"], ["a", "b", "b", "a"], ["a", "a", "a", "a"]]]
    # output: true
    # EXPLANATION: There are two valid cycles shown in different colors in the image below: <img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1500-1599/1559.Detect%20Cycles%20in%202D%20Grid/images/11.png" style="width: 225px; height: 163px;" />
    ,
    # example 2
    [[["c", "c", "c", "a"], ["c", "d", "c", "c"], ["c", "c", "e", "c"], ["f", "c", "c", "c"]]]
    # output: true
    # EXPLANATION: There is only one valid cycle highlighted in the image below: <img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1500-1599/1559.Detect%20Cycles%20in%202D%20Grid/images/2.png" style="width: 229px; height: 157px;" />
    ,
    # example 3
    [[["a", "b", "b"], ["b", "z", "b"], ["b", "b", "a"]]]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
