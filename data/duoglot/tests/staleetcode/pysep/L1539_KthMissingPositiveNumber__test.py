from L1539_KthMissingPositiveNumber import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 3, 4, 7, 11], 5]
    # output: 9
    # EXPLANATION: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5<sup>th</sup> missing positive integer is 9.
    ,
    # example 2
    [[1, 2, 3, 4], 2]
    # output: 6
    # EXPLANATION: The missing positive integers are [5,6,7,...]. The 2<sup>nd</sup> missing positive integer is 6.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
