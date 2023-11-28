from L2092_FindAllPeopleWithSecret import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [6, [[1, 2, 5], [2, 3, 8], [1, 5, 10]], 1]
    # output: [0,1,2,3,5]
    # EXPLANATION: At time 0, person 0 shares the secret with person 1. At time 5, person 1 shares the secret with person 2. At time 8, person 2 shares the secret with person 3. At time 10, person 1 shares the secret with person 5.     Thus, people 0, 1, 2, 3, and 5 know the secret after all the meetings.
    ,
    # example 2
    [4, [[3, 1, 3], [1, 2, 2], [0, 3, 3]], 3]
    # output: [0,1,3]
    # EXPLANATION:  At time 0, person 0 shares the secret with person 3. At time 2, neither person 1 nor person 2 know the secret. At time 3, person 3 shares the secret with person 0 and person 1. Thus, people 0, 1, and 3 know the secret after all the meetings.
    ,
    # example 3
    [5, [[3, 4, 2], [1, 2, 1], [2, 3, 1]], 1]
    # output: [0,1,2,3,4]
    # EXPLANATION:  At time 0, person 0 shares the secret with person 1. At time 1, person 1 shares the secret with person 2, and person 2 shares the secret with person 3. Note that person 2 can share the secret at the same time as receiving it. At time 2, person 3 shares the secret with person 4. Thus, people 0, 1, 2, 3, and 4 know the secret after all the meetings.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
