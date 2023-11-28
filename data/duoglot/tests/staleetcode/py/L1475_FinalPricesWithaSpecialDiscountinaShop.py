
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[8, 4, 6, 2, 3]]
    # output: [4,2,4,2,3]
    # EXPLANATION:   For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.  For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.  For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.  For items 3 and 4 you will not receive any discount at all.
    ,
    # example 2
    [[1, 2, 3, 4, 5]]
    # output: [1,2,3,4,5]
    # EXPLANATION:  In this case, for all items, you will not receive any discount at all.
    ,
    # example 3
    [[10, 1, 1, 6]]
    # output: [9,0,1,6]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### finalPrices 
from typing import *
def f_gold(prices: List[int]) -> List[int]:
    stk = []
    ans = prices[:]
    for i, v in enumerate(prices):
        while stk and prices[stk[-1]] >= v:
            ans[stk.pop()] -= v
        stk.append(i)
    return ans
"-----------------"
test()

