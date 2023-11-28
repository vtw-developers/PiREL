from L2085_CountCommonWordsWithOneOccurrence import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["leetcode", "is", "amazing", "as", "is"], ["amazing", "leetcode", "is"]]
    # output: 2
    # EXPLANATION:  - "leetcode" appears exactly once in each of the two arrays. We count this string. - "amazing" appears exactly once in each of the two arrays. We count this string. - "is" appears in each of the two arrays, but there are 2 occurrences of it in words1. We do not count this string. - "as" appears once in words1, but does not appear in words2. We do not count this string. Thus, there are 2 strings that appear exactly once in each of the two arrays.
    ,
    # example 2
    [["b", "bb", "bbb"], ["a", "aa", "aaa"]]
    # output: 0
    # EXPLANATION:  There are no strings that appear in each of the two arrays.
    ,
    # example 3
    [["a", "ab"], ["a", "a", "a", "ab"]]
    # output: 1
    # EXPLANATION:  The only string that appears exactly once in each of the two arrays is "ab".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
