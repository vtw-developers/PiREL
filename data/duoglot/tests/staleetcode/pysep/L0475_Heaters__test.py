from L0475_Heaters import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3], [2]]
    # output: 1
    # EXPLANATION:  The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
    ,
    # example 2
    [[1, 2, 3, 4], [1, 4]]
    # output: 1
    # EXPLANATION:  The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
    ,
    # example 3
    [[1, 5], [2]]
    # output: 3
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
