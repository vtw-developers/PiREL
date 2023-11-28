from L1942_TheNumberoftheSmallestUnoccupiedChair import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 4], [2, 3], [4, 6]], 1]
    # output: 1
    # EXPLANATION:   - Friend 0 arrives at time 1 and sits on chair 0. - Friend 1 arrives at time 2 and sits on chair 1. - Friend 1 leaves at time 3 and chair 1 becomes empty. - Friend 0 leaves at time 4 and chair 0 becomes empty. - Friend 2 arrives at time 4 and sits on chair 0. Since friend 1 sat on chair 1, we return 1.
    ,
    # example 2
    [[[3, 10], [1, 5], [2, 6]], 0]
    # output: 2
    # EXPLANATION:   - Friend 1 arrives at time 1 and sits on chair 0. - Friend 2 arrives at time 2 and sits on chair 1. - Friend 0 arrives at time 3 and sits on chair 2. - Friend 1 leaves at time 5 and chair 0 becomes empty. - Friend 2 leaves at time 6 and chair 1 becomes empty. - Friend 0 leaves at time 10 and chair 2 becomes empty. Since friend 0 sat on chair 2, we return 2.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
