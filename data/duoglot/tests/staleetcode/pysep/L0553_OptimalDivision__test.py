from L0553_OptimalDivision import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1000, 100, 10, 2]]
    # output: "1000/(100/10/2)"
    # EXPLANATION:  1000/(100/10/2) = 1000/((100/10)/2) = 200 However, the bold parenthesis in "1000/((100/10)/2)" are redundant, since they don't influence the operation priority. So you should return "1000/(100/10/2)". Other cases: 1000/(100/10)/2 = 50 1000/(100/(10/2)) = 50 1000/100/10/2 = 0.5 1000/100/(10/2) = 2
    ,
    # example 2
    [[2, 3, 4]]
    # output: "2/(3/4)"
    ,
    # example 3
    [[2]]
    # output: "2"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
