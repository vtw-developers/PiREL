from L2289_StepstoMakeArrayNondecreasing import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]]
    # output: 3
    # EXPLANATION:  The following are the steps performed: - Step 1: [5,<strong><u>3</u></strong>,4,4,7,<u><strong>3</strong></u>,6,11,<u><strong>8</strong></u>,<u><strong>5</strong></u>,11] becomes [5,4,4,7,6,11,11] - Step 2: [5,<u><strong>4</strong></u>,4,7,<u><strong>6</strong></u>,11,11] becomes [5,4,7,11,11] - Step 3: [5,<u><strong>4</strong></u>,7,11,11] becomes [5,7,11,11] [5,7,11,11] is a non-decreasing array. Therefore, we return 3.
    ,
    # example 2
    [[4, 5, 7, 7, 13]]
    # output: 0
    # EXPLANATION:  nums is already a non-decreasing array. Therefore, we return 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
