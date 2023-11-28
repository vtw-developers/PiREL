from L0499_TheMazeIII import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]], [4, 3], [0, 1]]
    # output: "lul"
    # EXPLANATION:  There are two shortest ways for the ball to drop into the hole. The first way is left -> up -> left, represented by "lul". The second way is up -> left, represented by 'ul'. Both ways have shortest distance 6, but the first way is lexicographically smaller because 'l' < 'u'. So the output is "lul".
    ,
    # example 2
    [[[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]], [4, 3], [3, 0]]
    # output: "impossible"
    # EXPLANATION:  The ball cannot reach the hole.
    ,
    # example 3
    [[[0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1]], [0, 4], [3, 5]]
    # output: "dldr"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
