from L2288_ApplyDiscounttoPrices import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["there are $1 $2 and 5$ candies in the shop", 50]
    # output: "there are $0.50 $1.00 and 5$ candies in the shop"
    # EXPLANATION:   The words which represent prices are "$1" and "$2".  - A 50% discount on "$1" yields "$0.50", so "$1" is replaced by "$0.50". - A 50% discount on "$2" yields "$1". Since we need to have exactly 2 decimal places after a price, we replace "$2" with "$1.00".
    ,
    # example 2
    ["1 2 $3 4 $5 $6 7 8$ $9 $10$", 100]
    # output: "1 2 $0.00 4 $0.00 $0.00 7 8$ $0.00 $10$"
    # EXPLANATION:   Applying a 100% discount on any price will result in 0. The words representing prices are "$3", "$5", "$6", and "$9". Each of them is replaced by "$0.00".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
