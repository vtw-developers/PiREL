from L2202_MaximizetheTopmostElementAfterKMoves import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[5, 2, 2, 4, 0, 6], 4]
    # output: 5
    # EXPLANATION:  One of the ways we can end with 5 at the top of the pile after 4 moves is as follows: - Step 1: Remove the topmost element = 5. The pile becomes [2,2,4,0,6]. - Step 2: Remove the topmost element = 2. The pile becomes [2,4,0,6]. - Step 3: Remove the topmost element = 2. The pile becomes [4,0,6]. - Step 4: Add 5 back onto the pile. The pile becomes [5,4,0,6]. Note that this is not the only way to end with 5 at the top of the pile. It can be shown that 5 is the largest answer possible after 4 moves.
    ,
    # example 2
    [[2], 1]
    # output: -1
    # EXPLANATION:   In the first move, our only option is to pop the topmost element of the pile. Since it is not possible to obtain a non-empty pile after one move, we return -1.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
