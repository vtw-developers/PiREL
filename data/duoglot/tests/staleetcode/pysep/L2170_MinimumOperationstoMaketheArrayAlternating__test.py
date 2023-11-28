from L2170_MinimumOperationstoMaketheArrayAlternating import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 1, 3, 2, 4, 3]]
    # output: 3
    # EXPLANATION:  One way to make the array alternating is by converting it to [3,1,3,<u><strong>1</strong></u>,<u><strong>3</strong></u>,<u><strong>1</strong></u>]. The number of operations required in this case is 3. It can be proven that it is not possible to make the array alternating in less than 3 operations.
    ,
    # example 2
    [[1, 2, 2, 2, 2]]
    # output: 2
    # EXPLANATION:  One way to make the array alternating is by converting it to [1,2,<u><strong>1</strong></u>,2,<u><strong>1</strong></u>]. The number of operations required in this case is 2. Note that the array cannot be converted to [<u><strong>2</strong></u>,2,2,2,2] because in this case nums[0] == nums[1] which violates the conditions of an alternating array.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
