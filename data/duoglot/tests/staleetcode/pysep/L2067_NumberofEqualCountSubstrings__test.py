from L2067_NumberofEqualCountSubstrings import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["aaabcbbcc", 3]
    # output: 3
    # EXPLANATION:  The substring that starts at index 0 and ends at index 2 is "aaa". The letter 'a' in the substring appears exactly 3 times. The substring that starts at index 3 and ends at index 8 is "bcbbcc". The letters 'b' and 'c' in the substring appear exactly 3 times. The substring that starts at index 0 and ends at index 8 is "aaabcbbcc". The letters 'a', 'b', and 'c' in the substring appear exactly 3 times.
    ,
    # example 2
    ["abcd", 2]
    # output: 0
    # EXPLANATION:  The number of times each letter appears in s is less than count. Therefore, no substrings in s are equal count substrings, so return 0.
    ,
    # example 3
    ["a", 5]
    # output: 0
    # EXPLANATION:  The number of times each letter appears in s is less than count. Therefore, no substrings in s are equal count substrings, so return 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
