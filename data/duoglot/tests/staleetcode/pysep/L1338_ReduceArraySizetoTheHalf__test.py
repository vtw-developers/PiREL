from L1338_ReduceArraySizetoTheHalf import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 3, 3, 3, 5, 5, 5, 2, 2, 7]]
    # output: 2
    # EXPLANATION:  Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array). Possible sets of size 2 are {3,5},{3,2},{5,2}. Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.
    ,
    # example 2
    [[7, 7, 7, 7, 7, 7]]
    # output: 1
    # EXPLANATION:  The only possible set you can choose is {7}. This will make the new array empty.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
