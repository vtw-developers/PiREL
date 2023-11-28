from L2044_CountNumberofMaximumBitwiseORSubsets import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 1]]
    # output: 2
    # EXPLANATION:  The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3: - [3] - [3,1]
    ,
    # example 2
    [[2, 2, 2]]
    # output: 7
    # EXPLANATION:  All non-empty subsets of [2,2,2] have a bitwise OR of 2. There are 2<sup>3</sup> - 1 = 7 total subsets.
    ,
    # example 3
    [[3, 2, 1, 5]]
    # output: 6
    # EXPLANATION:  The maximum possible bitwise OR of a subset is 7. There are 6 subsets with a bitwise OR of 7: - [3,5] - [3,1,5] - [3,2,5] - [3,2,1,5] - [2,5] - [2,1,5]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
