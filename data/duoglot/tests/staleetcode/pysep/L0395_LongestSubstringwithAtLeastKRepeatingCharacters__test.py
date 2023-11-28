from L0395_LongestSubstringwithAtLeastKRepeatingCharacters import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["aaabb", 3]
    # output: 3
    # EXPLANATION:  The longest substring is "aaa", as 'a' is repeated 3 times.
    ,
    # example 2
    ["ababbc", 2]
    # output: 5
    # EXPLANATION:  The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
