from L1760_MinimumLimitofBallsinaBag import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[9], 2]
    # output: 3
    # EXPLANATION:   - Divide the bag with 9 balls into two bags of sizes 6 and 3. [<strong><u>9</u></strong>] -> [6,3]. - Divide the bag with 6 balls into two bags of sizes 3 and 3. [<strong><u>6</u></strong>,3] -> [3,3,3]. The bag with the most number of balls has 3 balls, so your penalty is 3 and you should return 3.
    ,
    # example 2
    [[2, 4, 8, 2], 4]
    # output: 2
    # EXPLANATION:  - Divide the bag with 8 balls into two bags of sizes 4 and 4. [2,4,<strong><u>8</u></strong>,2] -> [2,4,4,4,2]. - Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,<strong><u>4</u></strong>,4,4,2] -> [2,2,2,4,4,2]. - Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,<strong><u>4</u></strong>,4,2] -> [2,2,2,2,2,4,2]. - Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,2,2,<strong><u>4</u></strong>,2] -> [2,2,2,2,2,2,2,2]. The bag with the most number of balls has 2 balls, so your penalty is 2 an you should return 2.
    ,
    # example 3
    [[7, 17], 2]
    # output: 7
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
