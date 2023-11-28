from L0930_BinarySubarraysWithSum import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 0, 1, 0, 1], 2]
    # output: 4
    # EXPLANATION:  The 4 subarrays are bolded and underlined below:  [<u><strong>1,0,1</strong></u>,0,1]  [<u><strong>1,0,1,0</strong></u>,1]  [1,<u><strong>0,1,0,1</strong></u>]  [1,0,<u><strong>1,0,1</strong></u>]
    ,
    # example 2
    [[0, 0, 0, 0, 0], 0]
    # output: 15
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
