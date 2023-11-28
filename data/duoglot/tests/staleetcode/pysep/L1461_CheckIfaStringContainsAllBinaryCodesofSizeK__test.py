from L1461_CheckIfaStringContainsAllBinaryCodesofSizeK import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["00110110", 2]
    # output: true
    # EXPLANATION:  The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
    ,
    # example 2
    ["0110", 1]
    # output: true
    # EXPLANATION:  The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring.
    ,
    # example 3
    ["0110", 2]
    # output: false
    # EXPLANATION:  The binary code "00" is of length 2 and does not exist in the array.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
