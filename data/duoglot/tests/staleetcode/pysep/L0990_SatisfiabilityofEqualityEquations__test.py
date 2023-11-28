from L0990_SatisfiabilityofEqualityEquations import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["a==b", "b!=a"]]
    # output: false
    # EXPLANATION:  If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second. There is no way to assign the variables to satisfy both equations.
    ,
    # example 2
    [["b==a", "a==b"]]
    # output: true
    # EXPLANATION:  We could assign a = 1 and b = 1 to satisfy both equations.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
