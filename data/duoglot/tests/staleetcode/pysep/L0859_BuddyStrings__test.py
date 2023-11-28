from L0859_BuddyStrings import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["ab", "ba"]
    # output: true
    # EXPLANATION:  You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
    ,
    # example 2
    ["ab", "ab"]
    # output: false
    # EXPLANATION:  The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
    ,
    # example 3
    ["aa", "aa"]
    # output: true
    # EXPLANATION:  You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
