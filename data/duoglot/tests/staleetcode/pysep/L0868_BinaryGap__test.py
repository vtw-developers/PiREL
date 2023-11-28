from L0868_BinaryGap import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [22]
    # output: 2
    # EXPLANATION:  22 in binary is "10110". The first adjacent pair of 1's is "<u>1</u>0<u>1</u>10" with a distance of 2. The second adjacent pair of 1's is "10<u>11</u>0" with a distance of 1. The answer is the largest of these two distances, which is 2. Note that "<u>1</u>01<u>1</u>0" is not a valid pair since there is a 1 separating the two 1's underlined.
    ,
    # example 2
    [8]
    # output: 0
    # EXPLANATION:  8 in binary is "1000". There are not any adjacent pairs of 1's in the binary representation of 8, so we return 0.
    ,
    # example 3
    [5]
    # output: 2
    # EXPLANATION:  5 in binary is "101".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
