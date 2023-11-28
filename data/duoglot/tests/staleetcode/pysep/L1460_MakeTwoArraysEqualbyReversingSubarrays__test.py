from L1460_MakeTwoArraysEqualbyReversingSubarrays import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4], [2, 4, 1, 3]]
    # output: true
    # EXPLANATION:  You can follow the next steps to convert arr to target: 1- Reverse sub-array [2,4,1], arr becomes [1,4,2,3] 2- Reverse sub-array [4,2], arr becomes [1,2,4,3] 3- Reverse sub-array [4,3], arr becomes [1,2,3,4] There are multiple ways to convert arr to target, this is not the only way to do so.
    ,
    # example 2
    [[7], [7]]
    # output: true
    # EXPLANATION:  arr is equal to target without any reverses.
    ,
    # example 3
    [[3, 7, 9], [3, 7, 11]]
    # output: false
    # EXPLANATION:  arr does not have value 9 and it can never be converted to target.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
