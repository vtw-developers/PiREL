from L1689_PartitioningIntoMinimumNumberOfDeciBinaryNumbers import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["32"]
    # output: 3
    # EXPLANATION:  10 + 11 + 11 = 32
    ,
    # example 2
    ["82734"]
    # output: 8
    ,
    # example 3
    ["27346209830709182346"]
    # output: 9
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
