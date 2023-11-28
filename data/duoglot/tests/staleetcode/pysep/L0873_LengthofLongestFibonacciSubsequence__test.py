from L0873_LengthofLongestFibonacciSubsequence import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4, 5, 6, 7, 8]]
    # output: 5
    # EXPLANATION:  The longest subsequence that is fibonacci-like: [1,2,3,5,8].
    ,
    # example 2
    [[1, 3, 7, 11, 12, 14, 18]]
    # output: 3
    # EXPLANATION: :<strong> </strong>The longest subsequence that is fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
