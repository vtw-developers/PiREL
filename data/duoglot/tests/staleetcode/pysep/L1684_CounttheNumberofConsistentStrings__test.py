from L1684_CounttheNumberofConsistentStrings import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["ab", ["ad", "bd", "aaab", "baa", "badab"]]
    # output: 2
    # EXPLANATION:  Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
    ,
    # example 2
    ["abc", ["a", "b", "c", "ab", "ac", "bc", "abc"]]
    # output: 7
    # EXPLANATION:  All strings are consistent.
    ,
    # example 3
    ["cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]]
    # output: 4
    # EXPLANATION:  Strings "cc", "acd", "ac", and "d" are consistent.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
