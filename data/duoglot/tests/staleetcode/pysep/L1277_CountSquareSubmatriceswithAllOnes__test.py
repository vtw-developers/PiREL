from L1277_CountSquareSubmatriceswithAllOnes import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]]
    # output: 15
    # EXPLANATION:   There are <strong>10</strong> squares of side 1. There are <strong>4</strong> squares of side 2. There is  <strong>1</strong> square of side 3. Total number of squares = 10 + 4 + 1 = <strong>15</strong>.
    ,
    # example 2
    [[[1, 0, 1], [1, 1, 0], [1, 1, 0]]]
    # output: 7
    # EXPLANATION:   There are <b>6</b> squares of side 1.   There is <strong>1</strong> square of side 2.  Total number of squares = 6 + 1 = <b>7</b>.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
