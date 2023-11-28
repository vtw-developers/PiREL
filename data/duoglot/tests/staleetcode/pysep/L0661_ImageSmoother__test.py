from L0661_ImageSmoother import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 1, 1], [1, 0, 1], [1, 1, 1]]]
    # output: [[0,0,0],[0,0,0],[0,0,0]]
    # EXPLANATION:  For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0 For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0 For the point (1,1): floor(8/9) = floor(0.88888889) = 0
    ,
    # example 2
    [[[100, 200, 100], [200, 50, 200], [100, 200, 100]]]
    # output: [[137,141,137],[141,138,141],[137,141,137]]
    # EXPLANATION:  For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137 For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141 For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
