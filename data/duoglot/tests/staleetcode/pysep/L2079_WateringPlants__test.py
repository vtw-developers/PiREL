from L2079_WateringPlants import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 2, 3, 3], 5]
    # output: 14
    # EXPLANATION:  Start at the river with a full watering can: - Walk to plant 0 (1 step) and water it. Watering can has 3 units of water. - Walk to plant 1 (1 step) and water it. Watering can has 1 unit of water. - Since you cannot completely water plant 2, walk back to the river to refill (2 steps). - Walk to plant 2 (3 steps) and water it. Watering can has 2 units of water. - Since you cannot completely water plant 3, walk back to the river to refill (3 steps). - Walk to plant 3 (4 steps) and water it. Steps needed = 1 + 1 + 2 + 3 + 3 + 4 = 14.
    ,
    # example 2
    [[1, 1, 1, 4, 2, 3], 4]
    # output: 30
    # EXPLANATION:  Start at the river with a full watering can: - Water plants 0, 1, and 2 (3 steps). Return to river (3 steps). - Water plant 3 (4 steps). Return to river (4 steps). - Water plant 4 (5 steps). Return to river (5 steps). - Water plant 5 (6 steps). Steps needed = 3 + 3 + 4 + 4 + 5 + 5 + 6 = 30.
    ,
    # example 3
    [[7, 7, 7, 7, 7, 7, 7], 8]
    # output: 49
    # EXPLANATION:  You have to refill before watering each plant. Steps needed = 1 + 1 + 2 + 2 + 3 + 3 + 4 + 4 + 5 + 5 + 6 + 6 + 7 = 49.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
