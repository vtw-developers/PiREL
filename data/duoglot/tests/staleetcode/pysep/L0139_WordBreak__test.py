from L0139_WordBreak import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["leetcode", ["leet", "code"]]
    # output: true
    # EXPLANATION:  Return true because "leetcode" can be segmented as "leet code".
    ,
    # example 2
    ["applepenapple", ["apple", "pen"]]
    # output: true
    # EXPLANATION:  Return true because "applepenapple" can be segmented as "apple pen apple". Note that you are allowed to reuse a dictionary word.
    ,
    # example 3
    ["catsandog", ["cats", "dog", "sand", "and", "cat"]]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
