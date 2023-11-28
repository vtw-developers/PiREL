from L1001_GridIllumination import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [5, [[0, 0], [4, 4]], [[1, 1], [1, 0]]]
    # output: [1,0]
    # EXPLANATION:  We have the initial grid with all lamps turned off. In the above picture we see the grid after turning on the lamp at grid[0][0] then turning on the lamp at grid[4][4]. The 0<sup>th</sup> query asks if the lamp at grid[1][1] is illuminated or not (the blue square). It is illuminated, so set ans[0] = 1. Then, we turn off all lamps in the red square. <img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1000-1099/1001.Grid%20Illumination/images/illu_step1.jpg" style="width: 500px; height: 218px;" /> The 1<sup>st</sup> query asks if the lamp at grid[1][0] is illuminated or not (the blue square). It is not illuminated, so set ans[1] = 0. Then, we turn off all lamps in the red rectangle. <img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1000-1099/1001.Grid%20Illumination/images/illu_step2.jpg" style="width: 500px; height: 219px;" />
    ,
    # example 2
    [5, [[0, 0], [4, 4]], [[1, 1], [1, 1]]]
    # output: [1,1]
    ,
    # example 3
    [5, [[0, 0], [0, 4]], [[0, 4], [0, 1], [1, 4]]]
    # output: [1,1,0]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
