from L0841_KeysandRooms import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1], [2], [3], []]]
    # output: true
    # EXPLANATION:   We visit room 0 and pick up key 1. We then visit room 1 and pick up key 2. We then visit room 2 and pick up key 3. We then visit room 3. Since we were able to visit every room, we return true.
    ,
    # example 2
    [[[1, 3], [3, 0, 1], [2], [0]]]
    # output: false
    # EXPLANATION:  We can not enter room number 2 since the only key that unlocks it is in that room.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
