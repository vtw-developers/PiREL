from L2220_MinimumBitFlipstoConvertNumber import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [10, 7]
    # output: 3
    # EXPLANATION:  The binary representation of 10 and 7 are 1010 and 0111 respectively. We can convert 10 to 7 in 3 steps: - Flip the first bit from the right: 101<u>0</u> -> 101<u>1</u>. - Flip the third bit from the right: 1<u>0</u>11 -> 1<u>1</u>11. - Flip the fourth bit from the right: <u>1</u>111 -> <u>0</u>111. It can be shown we cannot convert 10 to 7 in less than 3 steps. Hence, we return 3.
    ,
    # example 2
    [3, 4]
    # output: 3
    # EXPLANATION:  The binary representation of 3 and 4 are 011 and 100 respectively. We can convert 3 to 4 in 3 steps: - Flip the first bit from the right: 01<u>1</u> -> 01<u>0</u>. - Flip the second bit from the right: 0<u>1</u>0 -> 0<u>0</u>0. - Flip the third bit from the right: <u>0</u>00 -> <u>1</u>00. It can be shown we cannot convert 3 to 4 in less than 3 steps. Hence, we return 3.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
