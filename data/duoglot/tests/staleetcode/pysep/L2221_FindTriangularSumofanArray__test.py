from L2221_FindTriangularSumofanArray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4, 5]]
    # output: 8
    # EXPLANATION:  The above diagram depicts the process from which we obtain the triangular sum of the array.
    ,
    # example 2
    [[5]]
    # output: 5
    # EXPLANATION:  Since there is only one element in nums, the triangular sum is the value of that element itself.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
