
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[5, 5, 5, 10, 20]]
    # output: true
    # EXPLANATION:   From the first 3 customers, we collect three $5 bills in order. From the fourth customer, we collect a $10 bill and give back a $5. From the fifth customer, we give a $10 bill and a $5 bill. Since all customers got correct change, we output true.
    ,
    # example 2
    [[5, 5, 10, 10, 20]]
    # output: false
    # EXPLANATION:   From the first two customers in order, we collect two $5 bills. For the next two customers in order, we collect a $10 bill and give back a $5 bill. For the last customer, we can not give the change of $15 back because we only have two $10 bills. Since not every customer received the correct change, the answer is false.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### lemonadeChange 
from typing import *
def f_gold(bills: List[int]) -> bool:
    five, ten = 0, 0
    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            ten += 1
            five -= 1
        elif bill == 20:
            if ten > 0:
                ten -= 1
                five -= 1
            else:
                five -= 3
        if five < 0:
            return False
    return True
"-----------------"
test()

