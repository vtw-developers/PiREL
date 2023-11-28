from L0503_NextGreaterElementII import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 1]]
    # output: [2,-1,2]
    # EXPLANATION:  The first 1's next greater number is 2;  The number 2 can't find next greater number.  The second 1's next greater number needs to search circularly, which is also 2.
    ,
    # example 2
    [[1, 2, 3, 4, 3]]
    # output: [2,3,4,-1,4]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
