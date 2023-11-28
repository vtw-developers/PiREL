from L2273_FindResultantArrayAfterRemovingAnagrams import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["abba", "baba", "bbaa", "cd", "cd"]]
    # output: ["abba","cd"]
    # EXPLANATION:  One of the ways we can obtain the resultant array is by using the following operations: - Since words[2] = "bbaa" and words[1] = "baba" are anagrams, we choose index 2 and delete words[2].   Now words = ["abba","baba","cd","cd"]. - Since words[1] = "baba" and words[0] = "abba" are anagrams, we choose index 1 and delete words[1].   Now words = ["abba","cd","cd"]. - Since words[2] = "cd" and words[1] = "cd" are anagrams, we choose index 2 and delete words[2].   Now words = ["abba","cd"]. We can no longer perform any operations, so ["abba","cd"] is the final answer.
    ,
    # example 2
    [["a", "b", "c", "d", "e"]]
    # output: ["a","b","c","d","e"]
    # EXPLANATION:  No two adjacent strings in words are anagrams of each other, so no operations are performed.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
