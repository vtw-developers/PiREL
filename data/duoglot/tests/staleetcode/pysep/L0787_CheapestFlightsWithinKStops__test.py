from L0787_CheapestFlightsWithinKStops import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1]
    # output: 700
    # EXPLANATION:  The graph is shown above. The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700. Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
    ,
    # example 2
    [3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1]
    # output: 200
    # EXPLANATION:  The graph is shown above. The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
    ,
    # example 3
    [3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0]
    # output: 500
    # EXPLANATION:  The graph is shown above. The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
