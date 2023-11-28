from L0898_BitwiseORsofSubarrays import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[0]]
    # output: 1
    # EXPLANATION:  There is only one possible result: 0.
    ,
    # example 2
    [[1, 1, 2]]
    # output: 3
    # EXPLANATION:  The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2]. These yield the results 1, 1, 2, 1, 3, 3. There are 3 unique values, so the answer is 3.
    ,
    # example 3
    [[1, 2, 4]]
    # output: 6
    # EXPLANATION:  The possible results are 1, 2, 3, 4, 6, and 7.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
