from L1180_CountSubstringswithOnlyOneDistinctLetter import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["aaaba"]
    # output: 8
    # EXPLANATION: The substrings with one distinct letter are "aaa", "aa", "a", "b". "aaa" occurs 1 time. "aa" occurs 2 times. "a" occurs 4 times. "b" occurs 1 time. So the answer is 1 + 2 + 4 + 1 = 8.
    ,
    # example 2
    ["aaaaaaaaaa"]
    # output: 55
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
