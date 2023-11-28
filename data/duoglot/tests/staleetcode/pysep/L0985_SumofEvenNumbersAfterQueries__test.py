from L0985_SumofEvenNumbersAfterQueries import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]]]
    # output: [8,6,2,4]
    # EXPLANATION:  At the beginning, the array is [1,2,3,4]. After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8. After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6. After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2. After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.
    ,
    # example 2
    [[1], [[4, 0]]]
    # output: [0]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
