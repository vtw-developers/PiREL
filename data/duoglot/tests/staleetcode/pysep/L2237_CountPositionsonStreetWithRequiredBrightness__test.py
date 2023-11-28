from L2237_CountPositionsonStreetWithRequiredBrightness import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [5, [[0, 1], [2, 1], [3, 2]], [0, 2, 1, 4, 1]]
    # output: 4
    # EXPLANATION:  - The first street lamp lights up the area from [max(0, 0 - 1), min(n - 1, 0 + 1)] = [0, 1] (inclusive). - The second street lamp lights up the area from [max(0, 2 - 1), min(n - 1, 2 + 1)] = [1, 3] (inclusive). - The third street lamp lights up the area from [max(0, 3 - 2), min(n - 1, 3 + 2)] = [1, 4] (inclusive).  -   Position 0 is covered by the first street lamp. It is covered by 1 street lamp which is greater than requirement[0]. -   Position 1 is covered by the first, second, and third street lamps. It is covered by 3 street lamps which is greater than requirement[1]. -   Position 2 is covered by the second and third street lamps. It is covered by 2 street lamps which is greater than requirement[2]. -   Position 3 is covered by the second and third street lamps. It is covered by 2 street lamps which is less than requirement[3]. -   Position 4 is covered by the third street lamp. It is covered by 1 street lamp which is equal to requirement[4].  Positions 0, 1, 2, and 4 meet the requirement so we return 4.
    ,
    # example 2
    [1, [[0, 1]], [2]]
    # output: 0
    # EXPLANATION:  - The first street lamp lights up the area from [max(0, 0 - 1), min(n - 1, 0 + 1)] = [0, 0] (inclusive). - Position 0 is covered by the first street lamp. It is covered by 1 street lamp which is less than requirement[0]. - We return 0 because no position meets their brightness requirement.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
