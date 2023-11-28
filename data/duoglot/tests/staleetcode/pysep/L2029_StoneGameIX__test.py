from L2029_StoneGameIX import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 1]]
    # output: true
    # EXPLANATION:  The game will be played as follows: - Turn 1: Alice can remove either stone. - Turn 2: Bob removes the remaining stone.  The sum of the removed stones is 1 + 2 = 3 and is divisible by 3. Therefore, Bob loses and Alice wins the game.
    ,
    # example 2
    [[2]]
    # output: false
    # EXPLANATION:  Alice will remove the only stone, and the sum of the values on the removed stones is 2.  Since all the stones are removed and the sum of values is not divisible by 3, Bob wins the game.
    ,
    # example 3
    [[5, 1, 2, 4, 3]]
    # output: false
    # EXPLANATION:  Bob will always win. One possible way for Bob to win is shown below: - Turn 1: Alice can remove the second stone with value 1. Sum of removed stones = 1. - Turn 2: Bob removes the fifth stone with value 3. Sum of removed stones = 1 + 3 = 4. - Turn 3: Alices removes the fourth stone with value 4. Sum of removed stones = 1 + 3 + 4 = 8. - Turn 4: Bob removes the third stone with value 2. Sum of removed stones = 1 + 3 + 4 + 2 = 10. - Turn 5: Alice removes the first stone with value 5. Sum of removed stones = 1 + 3 + 4 + 2 + 5 = 15. Alice loses the game because the sum of the removed stones (15) is divisible by 3. Bob wins the game.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
