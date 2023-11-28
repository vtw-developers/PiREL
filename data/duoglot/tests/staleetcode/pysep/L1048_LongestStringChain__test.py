from L1048_LongestStringChain import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["a", "b", "ba", "bca", "bda", "bdca"]]
    # output: 4
    # EXPLANATION: : One of the longest word chains is ["a","<u>b</u>a","b<u>d</u>a","bd<u>c</u>a"].
    ,
    # example 2
    [["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]]
    # output: 5
    # EXPLANATION:  All the words can be put in a word chain ["xb", "xb<u>c</u>", "<u>c</u>xbc", "<u>p</u>cxbc", "pcxbc<u>f</u>"].
    ,
    # example 3
    [["abcd", "dbqca"]]
    # output: 1
    # EXPLANATION:  The trivial word chain ["abcd"] is one of the longest word chains. ["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
