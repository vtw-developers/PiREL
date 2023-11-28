from L0241_DifferentWaystoAddParentheses import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["2-1-1"]
    # output: [0,2]
    # EXPLANATION:  ((2-1)-1) = 0  (2-(1-1)) = 2
    ,
    # example 2
    ["2*3-4*5"]
    # output: [-34,-14,-10,-10,10]
    # EXPLANATION:  (2*(3-(4*5))) = -34  ((2*3)-(4*5)) = -14  ((2*(3-4))*5) = -10  (2*((3-4)*5)) = -10  (((2*3)-4)*5) = 10
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
