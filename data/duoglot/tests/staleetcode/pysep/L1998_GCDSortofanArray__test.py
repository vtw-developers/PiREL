from L1998_GCDSortofanArray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[7, 21, 3]]
    # output: true
    # EXPLANATION:  We can sort [7,21,3] by performing the following operations: - Swap 7 and 21 because gcd(7,21) = 7. nums = [<u><strong>21</strong></u>,<u><strong>7</strong></u>,3] - Swap 21 and 3 because gcd(21,3) = 3. nums = [<u><strong>3</strong></u>,7,<u><strong>21</strong></u>]
    ,
    # example 2
    [[5, 2, 6, 2]]
    # output: false
    # EXPLANATION:  It is impossible to sort the array because 5 cannot be swapped with any other element.
    ,
    # example 3
    [[10, 5, 9, 3, 15]]
    # output: trueWe can sort [10,5,9,3,15] by performing the following operations:- Swap 10 and 15 because gcd(10,15) = 5. nums = [<u><strong>15</strong></u>,5,9,3,<u><strong>10</strong></u>]- Swap 15 and 3 because gcd(15,3) = 3. nums = [<u><strong>3</strong></u>,5,9,<u><strong>15</strong></u>,10]- Swap 10 and 15 because gcd(10,15) = 5. nums = [3,5,9,<u><strong>10</strong></u>,<u><strong>15</strong></u>]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
