from L2311_LongestBinarySubsequenceLessThanorEqualtoK import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["1001010", 5]
    # output: 5
    # EXPLANATION:  The longest subsequence of s that makes up a binary number less than or equal to 5 is "00010", as this number is equal to 2 in decimal. Note that "00100" and "00101" are also possible, which are equal to 4 and 5 in decimal, respectively. The length of this subsequence is 5, so 5 is returned.
    ,
    # example 2
    ["00101001", 1]
    # output: 6
    # EXPLANATION:  "000001" is the longest subsequence of s that makes up a binary number less than or equal to 1, as this number is equal to 1 in decimal. The length of this subsequence is 6, so 6 is returned.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
