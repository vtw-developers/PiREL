from L0803_BricksFallingWhenHit import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 0, 0, 0], [1, 1, 1, 0]], [[1, 0]]]
    # output: [2]
    # EXPLANATION: Starting with the grid: [[1,0,0,0],  [<u>1</u>,1,1,0]] We erase the underlined brick at (1,0), resulting in the grid: [[1,0,0,0],  [0,<u>1</u>,<u>1</u>,0]] The two underlined bricks are no longer stable as they are no longer connected to the top nor adjacent to another stable brick, so they will fall. The resulting grid is: [[1,0,0,0],  [0,0,0,0]] Hence the result is [2].
    ,
    # example 2
    [[[1, 0, 0, 0], [1, 1, 0, 0]], [[1, 1], [1, 0]]]
    # output: [0,0]
    # EXPLANATION: Starting with the grid: [[1,0,0,0],  [1,<u>1</u>,0,0]] We erase the underlined brick at (1,1), resulting in the grid: [[1,0,0,0],  [1,0,0,0]] All remaining bricks are still stable, so no bricks fall. The grid remains the same: [[1,0,0,0],  [<u>1</u>,0,0,0]] Next, we erase the underlined brick at (1,0), resulting in the grid: [[1,0,0,0],  [0,0,0,0]] Once again, all remaining bricks are still stable, so no bricks fall. Hence the result is [0,0].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
