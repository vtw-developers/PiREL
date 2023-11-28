from L1765_MapofHighestPeak import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 1], [0, 0]]]
    # output: [[1,0],[2,1]]
    # EXPLANATION:  The image shows the assigned heights of each cell. The blue cell is the water cell, and the green cells are the land cells.
    ,
    # example 2
    [[[0, 0, 1], [1, 0, 0], [0, 0, 0]]]
    # output: [[1,1,0],[0,1,1],[1,2,2]]
    # EXPLANATION:  A height of 2 is the maximum possible height of any assignment. Any height assignment that has a maximum height of 2 while still meeting the rules will also be accepted.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
