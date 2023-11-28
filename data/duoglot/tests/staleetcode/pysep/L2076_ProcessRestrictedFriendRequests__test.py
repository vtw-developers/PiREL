from L2076_ProcessRestrictedFriendRequests import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3, [[0, 1]], [[0, 2], [2, 1]]]
    # output: [true,false]
    # EXPLANATION: Request 0: Person 0 and person 2 can be friends, so they become direct friends.  Request 1: Person 2 and person 1 cannot be friends since person 0 and person 1 would be indirect friends (1--2--0).
    ,
    # example 2
    [3, [[0, 1]], [[1, 2], [0, 2]]]
    # output: [true,false]
    # EXPLANATION: Request 0: Person 1 and person 2 can be friends, so they become direct friends. Request 1: Person 0 and person 2 cannot be friends since person 0 and person 1 would be indirect friends (0--2--1).
    ,
    # example 3
    [5, [[0, 1], [1, 2], [2, 3]], [[0, 4], [1, 2], [3, 1], [3, 4]]]
    # output: [true,false,true,false]
    # EXPLANATION: Request 0: Person 0 and person 4 can be friends, so they become direct friends. Request 1: Person 1 and person 2 cannot be friends since they are directly restricted. Request 2: Person 3 and person 1 can be friends, so they become direct friends. Request 3: Person 3 and person 4 cannot be friends since person 0 and person 1 would be indirect friends (0--4--3--1).
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
