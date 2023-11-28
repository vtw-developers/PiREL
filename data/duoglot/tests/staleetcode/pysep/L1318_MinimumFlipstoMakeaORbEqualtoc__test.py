from L1318_MinimumFlipstoMakeaORbEqualtoc import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2, 6, 5]
    # output: 3
    # EXPLANATION: After flips a = 1 , b = 4 , c = 5 such that (<code>a</code> OR <code>b</code> == <code>c</code>)
    ,
    # example 2
    [4, 2, 7]
    # output: 1
    ,
    # example 3
    [1, 2, 3]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
