from L1167_MinimumCosttoConnectSticks import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 4, 3]]
    # output: 14
    # EXPLANATION:  You start with sticks = [2,4,3]. 1. Combine sticks 2 and 3 for a cost of 2 + 3 = 5. Now you have sticks = [5,4]. 2. Combine sticks 5 and 4 for a cost of 5 + 4 = 9. Now you have sticks = [9]. There is only one stick left, so you are done. The total cost is 5 + 9 = 14.
    ,
    # example 2
    [[1, 8, 3, 5]]
    # output: 30
    # EXPLANATION:  You start with sticks = [1,8,3,5]. 1. Combine sticks 1 and 3 for a cost of 1 + 3 = 4. Now you have sticks = [4,8,5]. 2. Combine sticks 4 and 5 for a cost of 4 + 5 = 9. Now you have sticks = [9,8]. 3. Combine sticks 9 and 8 for a cost of 9 + 8 = 17. Now you have sticks = [17]. There is only one stick left, so you are done. The total cost is 4 + 9 + 17 = 30.
    ,
    # example 3
    [[5]]
    # output: 0
    # EXPLANATION:  There is only one stick, so you don't need to do anything. The total cost is 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
