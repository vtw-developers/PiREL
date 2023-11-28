from L2169_CountOperationstoObtainZero import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2, 3]
    # output: 3
    # EXPLANATION:   - Operation 1: num1 = 2, num2 = 3. Since num1 < num2, we subtract num1 from num2 and get num1 = 2, num2 = 3 - 2 = 1. - Operation 2: num1 = 2, num2 = 1. Since num1 > num2, we subtract num2 from num1. - Operation 3: num1 = 1, num2 = 1. Since num1 == num2, we subtract num2 from num1. Now num1 = 0 and num2 = 1. Since num1 == 0, we do not need to perform any further operations. So the total number of operations required is 3.
    ,
    # example 2
    [10, 10]
    # output: 1
    # EXPLANATION:   - Operation 1: num1 = 10, num2 = 10. Since num1 == num2, we subtract num2 from num1 and get num1 = 10 - 10 = 0. Now num1 = 0 and num2 = 10. Since num1 == 0, we are done. So the total number of operations required is 1.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
