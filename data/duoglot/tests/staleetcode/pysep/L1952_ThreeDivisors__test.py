from L1952_ThreeDivisors import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2]
    # output: false<strong>Explantion:</strong> 2 has only two divisors: 1 and 2.
    ,
    # example 2
    [4]
    # output: true<strong>Explantion:</strong> 4 has three divisors: 1, 2, and 4.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
