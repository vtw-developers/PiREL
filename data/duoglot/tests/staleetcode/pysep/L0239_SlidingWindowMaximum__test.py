from L0239_SlidingWindowMaximum import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 3, -1, -3, 5, 3, 6, 7], 3]
    # output: [3,3,5,5,6,7]
    # EXPLANATION:   Window position                Max ---------------               ----- [1  3  -1] -3  5  3  6  7       <strong>3</strong>  1 [3  -1  -3] 5  3  6  7       <strong>3</strong>  1  3 [-1  -3  5] 3  6  7      <strong> 5</strong>  1  3  -1 [-3  5  3] 6  7       <strong>5</strong>  1  3  -1  -3 [5  3  6] 7       <strong>6</strong>  1  3  -1  -3  5 [3  6  7]      <strong>7</strong>
    ,
    # example 2
    [[1], 1]
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
