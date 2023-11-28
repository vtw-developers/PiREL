from L1414_FindtheMinimumNumberofFibonacciNumbersWhoseSumIsK import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [7]
    # output: 2
    # EXPLANATION:  The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ...  For k = 7 we can use 2 + 5 = 7.
    ,
    # example 2
    [10]
    # output: 2
    # EXPLANATION:  For k = 10 we can use 2 + 8 = 10.
    ,
    # example 3
    [19]
    # output: 3
    # EXPLANATION:  For k = 19 we can use 1 + 5 + 13 = 19.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
