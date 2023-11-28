from L2212_MaximumPointsinanArcheryCompetition import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [9, [1, 1, 0, 1, 0, 0, 2, 1, 0, 1, 2, 0]]
    # output: [0,0,0,0,1,1,0,0,1,2,3,1]
    # EXPLANATION:  The table above shows how the competition is scored.  Bob earns a total point of 4 + 5 + 8 + 9 + 10 + 11 = 47. It can be shown that Bob cannot obtain a score higher than 47 points.
    ,
    # example 2
    [3, [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2]]
    # output: [0,0,0,0,0,0,0,0,1,1,1,0]
    # EXPLANATION:  The table above shows how the competition is scored. Bob earns a total point of 8 + 9 + 10 = 27. It can be shown that Bob cannot obtain a score higher than 27 points.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
