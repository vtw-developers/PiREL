from L1944_NumberofVisiblePeopleinaQueue import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[10, 6, 8, 5, 11, 9]]
    # output: [3,1,2,1,1,0]
    # EXPLANATION:  Person 0 can see person 1, 2, and 4. Person 1 can see person 2. Person 2 can see person 3 and 4. Person 3 can see person 4. Person 4 can see person 5. Person 5 can see no one since nobody is to the right of them.
    ,
    # example 2
    [[5, 1, 2, 3, 10]]
    # output: [4,1,1,1,0]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
