from L0089_GrayCode import f_gold

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
    # output: [0,1,3,2]
    # EXPLANATION:  The binary representation of [0,1,3,2] is [00,01,11,10]. - 0<u>0</u> and 0<u>1</u> differ by one bit - <u>0</u>1 and <u>1</u>1 differ by one bit - 1<u>1</u> and 1<u>0</u> differ by one bit - <u>1</u>0 and <u>0</u>0 differ by one bit [0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01]. - <u>0</u>0 and <u>1</u>0 differ by one bit - 1<u>0</u> and 1<u>1</u> differ by one bit - <u>1</u>1 and <u>0</u>1 differ by one bit - 0<u>1</u> and 0<u>0</u> differ by one bit
    ,
    # example 2
    [1]
    # output: [0,1]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
