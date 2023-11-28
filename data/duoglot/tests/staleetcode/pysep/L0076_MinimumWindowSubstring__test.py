from L0076_MinimumWindowSubstring import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["ADOBECODEBANC", "ABC"]
    # output: "BANC"
    # EXPLANATION:  The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
    ,
    # example 2
    ["a", "a"]
    # output: "a"
    # EXPLANATION:  The entire string s is the minimum window.
    ,
    # example 3
    ["a", "aa"]
    # output: ""
    # EXPLANATION:  Both 'a's from t must be included in the window. Since the largest window of s only has one 'a', return empty string.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
