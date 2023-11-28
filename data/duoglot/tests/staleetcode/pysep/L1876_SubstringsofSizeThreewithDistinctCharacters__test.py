from L1876_SubstringsofSizeThreewithDistinctCharacters import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["xyzzaz"]
    # output: 1
    # EXPLANATION:  There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz".  The only good substring of length 3 is "xyz".
    ,
    # example 2
    ["aababcabc"]
    # output: 4
    # EXPLANATION:  There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc". The good substrings are "abc", "bca", "cab", and "abc".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
