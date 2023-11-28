from L0305_NumberofIslandsII import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]]]
    # output: [1,1,2,3]
    # EXPLANATION:  Initially, the 2d grid is filled with water. - Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land. We have 1 island. - Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land. We still have 1 island. - Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land. We have 2 islands. - Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land. We have 3 islands.
    ,
    # example 2
    [1, 1, [[0, 0]]]
    # output: [1]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
