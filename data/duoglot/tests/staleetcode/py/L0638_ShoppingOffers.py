
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 5], [[3, 0, 5], [1, 2, 10]], [3, 2]]
    # output: 14
    # EXPLANATION:  There are two kinds of items, A and B. Their prices are $2 and $5 respectively.  In special offer 1, you can pay $5 for 3A and 0B In special offer 2, you can pay $10 for 1A and 2B.  You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.
    ,
    # example 2
    [[2, 3, 4], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 2, 1]]
    # output: 11
    # EXPLANATION:  The price of A is $2, and $3 for B, $4 for C.  You may pay $4 for 1A and 1B, and $9 for 2A ,2B and 1C.  You need to buy 1A ,2B and 1C, so you may pay $4 for 1A and 1B (special offer #1), and $3 for 1B, $4 for 1C.  You cannot add more items, though only $9 for 2A ,2B and 1C.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### shoppingOffers 
from typing import *
def f_gold(price: List[int], special: List[List[int]], needs: List[int]
) -> int:
    def total(price, needs):
        return sum(price[i] * needs[i] for i in range(len(needs)))
    ans = total(price, needs)
    t = []
    for offer in special:
        t.clear()
        for j in range(len(needs)):
            if offer[j] > needs[j]:
                t.clear()
                break
            t.append(needs[j] - offer[j])
        if t:
            ans = min(ans, offer[-1] + f_gold(price, special, t))
    return ans
"-----------------"
test()

