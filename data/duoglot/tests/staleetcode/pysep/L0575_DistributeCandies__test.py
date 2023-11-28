from L0575_DistributeCandies import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 1, 2, 2, 3, 3]]
    # output: 3
    # EXPLANATION:  Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.
    ,
    # example 2
    [[1, 1, 2, 3]]
    # output: 2
    # EXPLANATION:  Alice can only eat 4 / 2 = 2 candies. Whether she eats types [1,2], [1,3], or [2,3], she still can only eat 2 different types.
    ,
    # example 3
    [[6, 6, 6, 6]]
    # output: 1
    # EXPLANATION:  Alice can only eat 4 / 2 = 2 candies. Even though she can eat 2 candies, she only has 1 type.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
