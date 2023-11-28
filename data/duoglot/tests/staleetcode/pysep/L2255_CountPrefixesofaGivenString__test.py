from L2255_CountPrefixesofaGivenString import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["a", "b", "c", "ab", "bc", "abc"], "abc"]
    # output: 3
    # EXPLANATION:  The strings in words which are a prefix of s = "abc" are: "a", "ab", and "abc". Thus the number of strings in words which are a prefix of s is 3.
    ,
    # example 2
    [["a", "a"], "aa"]
    # output: 2
    # EXPLANATION: Both of the strings are a prefix of s.  Note that the same string can occur multiple times in words, and it should be counted each time.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
