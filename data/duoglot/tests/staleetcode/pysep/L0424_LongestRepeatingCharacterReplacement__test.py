from L0424_LongestRepeatingCharacterReplacement import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["ABAB", 2]
    # output: 4
    # EXPLANATION:  Replace the two 'A's with two 'B's or vice versa.
    ,
    # example 2
    ["AABABBA", 1]
    # output: 4
    # EXPLANATION:  Replace the one 'A' in the middle with 'B' and form "AABBBBA". The substring "BBBB" has the longest repeating letters, which is 4.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
