
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[3, 50], [7, 10], [12, 25]], 10]
    # output: 2.65000
    # EXPLANATION:  Based on your income, you have 3 dollars in the 1<sup>st</sup> tax bracket, 4 dollars in the 2<sup>nd</sup> tax bracket, and 3 dollars in the 3<sup>rd</sup> tax bracket. The tax rate for the three tax brackets is 50%, 10%, and 25%, respectively. In total, you pay $3 * 50% + $4 * 10% + $3 * 25% = $2.65 in taxes.
    ,
    # example 2
    [[[1, 0], [4, 25], [5, 50]], 2]
    # output: 0.25000
    # EXPLANATION:  Based on your income, you have 1 dollar in the 1<sup>st</sup> tax bracket and 1 dollar in the 2<sup>nd</sup> tax bracket. The tax rate for the two tax brackets is 0% and 25%, respectively. In total, you pay $1 * 0% + $1 * 25% = $0.25 in taxes.
    ,
    # example 3
    [[[2, 50]], 0]
    # output: 0.00000
    # EXPLANATION:  You have no income to tax, so you have to pay a total of $0 in taxes.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### calculateTax 
from typing import *
def f_gold(brackets: List[List[int]], income: int) -> float:
    ans = idx = 0
    prev = 0
    while income:
        a, b = brackets[idx]
        d = a - prev
        ans += min(d, income) * b / 100
        if income <= d:
            break
        income -= d
        idx += 1
        prev = a
    return ans
"-----------------"
test()

