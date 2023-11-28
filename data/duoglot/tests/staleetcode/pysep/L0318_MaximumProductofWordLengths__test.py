from L0318_MaximumProductofWordLengths import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]]
    # output: 16
    # EXPLANATION:  The two words can be "abcw", "xtfn".
    ,
    # example 2
    [["a", "ab", "abc", "d", "cd", "bcd", "abcd"]]
    # output: 4
    # EXPLANATION:  The two words can be "ab", "cd".
    ,
    # example 3
    [["a", "aa", "aaa", "aaaa"]]
    # output: 0
    # EXPLANATION:  No such pair of words.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
