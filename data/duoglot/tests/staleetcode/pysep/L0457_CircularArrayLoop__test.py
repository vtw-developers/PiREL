from L0457_CircularArrayLoop import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, -1, 1, 2, 2]]
    # output: true
    # EXPLANATION:  There is a cycle from index 0 -> 2 -> 3 -> 0 -> ... The cycle's length is 3.
    ,
    # example 2
    [[-1, 2]]
    # output: false
    # EXPLANATION:  The sequence from index 1 -> 1 -> 1 -> ... is not a cycle because the sequence's length is 1. By definition the sequence's length must be strictly greater than 1 to be a cycle.
    ,
    # example 3
    [[-2, 1, -1, -2, -2]]
    # output: false
    # EXPLANATION:  The sequence from index 1 -> 2 -> 1 -> ... is not a cycle because nums[1] is positive, but nums[2] is negative. Every nums[seq[j]] must be either all positive or all negative.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
