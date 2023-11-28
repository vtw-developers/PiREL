from L0066_PlusOne import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3]]
    # output: [1,2,4]
    # EXPLANATION:  The array represents the integer 123. Incrementing by one gives 123 + 1 = 124. Thus, the result should be [1,2,4].
    ,
    # example 2
    [[4, 3, 2, 1]]
    # output: [4,3,2,2]
    # EXPLANATION:  The array represents the integer 4321. Incrementing by one gives 4321 + 1 = 4322. Thus, the result should be [4,3,2,2].
    ,
    # example 3
    [[9]]
    # output: [1,0]
    # EXPLANATION:  The array represents the integer 9. Incrementing by one gives 9 + 1 = 10. Thus, the result should be [1,0].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
