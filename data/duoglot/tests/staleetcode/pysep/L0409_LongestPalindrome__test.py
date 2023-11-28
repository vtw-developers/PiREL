from L0409_LongestPalindrome import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abccccdd"]
    # output: 7
    # EXPLANATION:  One longest palindrome that can be built is "dccaccd", whose length is 7.
    ,
    # example 2
    ["a"]
    # output: 1
    # EXPLANATION:  The longest palindrome that can be built is "a", whose length is 1.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
