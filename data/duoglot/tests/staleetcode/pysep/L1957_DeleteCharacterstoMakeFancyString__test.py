from L1957_DeleteCharacterstoMakeFancyString import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["leeetcode"]
    # output: "leetcode"
    # EXPLANATION:  Remove an 'e' from the first group of 'e's to create "leetcode". No three consecutive characters are equal, so return "leetcode".
    ,
    # example 2
    ["aaabaaaa"]
    # output: "aabaa"
    # EXPLANATION:  Remove an 'a' from the first group of 'a's to create "aabaaaa". Remove two 'a's from the second group of 'a's to create "aabaa". No three consecutive characters are equal, so return "aabaa".
    ,
    # example 3
    ["aab"]
    # output: "aab"
    # EXPLANATION:  No three consecutive characters are equal, so return "aab".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
