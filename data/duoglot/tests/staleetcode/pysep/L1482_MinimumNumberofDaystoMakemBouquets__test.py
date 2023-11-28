from L1482_MinimumNumberofDaystoMakemBouquets import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 10, 3, 10, 2], 3, 1]
    # output: 3
    # EXPLANATION:  Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden. We need 3 bouquets each should contain 1 flower. After day 1: [x, _, _, _, _]   // we can only make one bouquet. After day 2: [x, _, _, _, x]   // we can only make two bouquets. After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.
    ,
    # example 2
    [[1, 10, 3, 10, 2], 3, 2]
    # output: -1
    # EXPLANATION:  We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.
    ,
    # example 3
    [[7, 7, 7, 7, 12, 7, 7], 2, 3]
    # output: 12
    # EXPLANATION:  We need 2 bouquets each should have 3 flowers. Here is the garden after the 7 and 12 days: After day 7: [x, x, x, x, _, x, x] We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent. After day 12: [x, x, x, x, x, x, x] It is obvious that we can make two bouquets in different ways.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
