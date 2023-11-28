from L0003_LongestSubstringWithoutRepeatingCharacters import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abcabcbb"]
    # output: 3
    # EXPLANATION:  The answer is "abc", with the length of 3.
    ,
    # example 2
    ["bbbbb"]
    # output: 1
    # EXPLANATION:  The answer is "b", with the length of 1.
    ,
    # example 3
    ["pwwkew"]
    # output: 3
    # EXPLANATION:  The answer is "wke", with the length of 3. Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
