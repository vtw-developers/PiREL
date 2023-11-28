from L1891_CuttingRibbons import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[9, 7, 5], 3]
    # output: 5
    # EXPLANATION:  - Cut the first ribbon to two ribbons, one of length 5 and one of length 4. - Cut the second ribbon to two ribbons, one of length 5 and one of length 2. - Keep the third ribbon as it is. Now you have 3 ribbons of length 5.
    ,
    # example 2
    [[7, 5, 9], 4]
    # output: 4
    # EXPLANATION:  - Cut the first ribbon to two ribbons, one of length 4 and one of length 3. - Cut the second ribbon to two ribbons, one of length 4 and one of length 1. - Cut the third ribbon to three ribbons, two of length 4 and one of length 1. Now you have 4 ribbons of length 4.
    ,
    # example 3
    [[5, 7, 9], 22]
    # output: 0
    # EXPLANATION:  You cannot obtain k ribbons of the same positive integer length.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
