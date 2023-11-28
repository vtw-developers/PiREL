from L1160_FindWordsThatCanBeFormedbyCharacters import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["cat", "bt", "hat", "tree"], "atach"]
    # output: 6
    # EXPLANATION:  The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
    ,
    # example 2
    [["hello", "world", "leetcode"], "welldonehoneyr"]
    # output: 10
    # EXPLANATION:  The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
