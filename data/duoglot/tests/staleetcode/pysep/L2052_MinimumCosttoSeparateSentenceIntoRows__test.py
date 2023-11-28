from L2052_MinimumCosttoSeparateSentenceIntoRows import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["i love leetcode", 12]
    # output: 36
    # EXPLANATION:  Separating sentence into "i", "love", and "leetcode" has a cost of (12 - 1)<sup>2</sup> + (12 - 4)<sup>2</sup> = 185. Separating sentence into "i love", and "leetcode" has a cost of (12 - 6)<sup>2</sup> = 36. Separating sentence into "i", "love leetcode" is not possible because "love leetcode" has length 13. 36 is the minimum possible total cost so return it.
    ,
    # example 2
    ["apples and bananas taste great", 7]
    # output: 21
    # EXPLANATION:  Separating sentence into "apples", "and", "bananas", "taste", and "great" has a cost of (7 - 6)<sup>2</sup> + (7 - 3)<sup>2</sup> + (7 - 7)<sup>2</sup> + (7 - 5)<sup>2 </sup>= 21. 21 is the minimum possible total cost so return it.
    ,
    # example 3
    ["a", 5]
    # output: 0
    # EXPLANATION:  The cost of the last row is not included in the total cost, and since there is only one row, return 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
