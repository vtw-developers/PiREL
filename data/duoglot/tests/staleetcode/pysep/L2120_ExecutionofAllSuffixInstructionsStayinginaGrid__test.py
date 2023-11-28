from L2120_ExecutionofAllSuffixInstructionsStayinginaGrid import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3, [0, 1], "RRDDLU"]
    # output: [1,5,4,3,1,0]
    # EXPLANATION:  Starting from startPos and beginning execution from the i<sup>th</sup> instruction: - 0<sup>th</sup>: "<u><strong>R</strong></u>RDDLU". Only one instruction "R" can be executed before it moves off the grid. - 1<sup>st</sup>:  "<u><strong>RDDLU</strong></u>". All five instructions can be executed while it stays in the grid and ends at (1, 1). - 2<sup>nd</sup>:   "<u><strong>DDLU</strong></u>". All four instructions can be executed while it stays in the grid and ends at (1, 0). - 3<sup>rd</sup>:    "<u><strong>DLU</strong></u>". All three instructions can be executed while it stays in the grid and ends at (0, 0). - 4<sup>th</sup>:     "<u><strong>L</strong></u>U". Only one instruction "L" can be executed before it moves off the grid. - 5<sup>th</sup>:      "U". If moving up, it would move off the grid.
    ,
    # example 2
    [2, [1, 1], "LURD"]
    # output: [4,1,0,0]
    # EXPLANATION:  - 0<sup>th</sup>: "<u><strong>LURD</strong></u>". - 1<sup>st</sup>:  "<u><strong>U</strong></u>RD". - 2<sup>nd</sup>:   "RD". - 3<sup>rd</sup>:    "D".
    ,
    # example 3
    [1, [0, 0], "LRUD"]
    # output: [0,0,0,0]
    # EXPLANATION:  No matter which instruction the robot begins execution from, it would move off the grid.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
