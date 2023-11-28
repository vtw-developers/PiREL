from L0264_UglyNumberII import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [10]
    # output: 12
    # EXPLANATION:  [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
    ,
    # example 2
    [1]
    # output: 1
    # EXPLANATION:  1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
