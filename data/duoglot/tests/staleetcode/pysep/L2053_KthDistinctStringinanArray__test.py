from L2053_KthDistinctStringinanArray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["d", "b", "c", "b", "c", "a"], 2]
    # output: "a"
    # EXPLANATION:  The only distinct strings in arr are "d" and "a". "d" appears 1<sup>st</sup>, so it is the 1<sup>st</sup> distinct string. "a" appears 2<sup>nd</sup>, so it is the 2<sup>nd</sup> distinct string. Since k == 2, "a" is returned.
    ,
    # example 2
    [["aaa", "aa", "a"], 1]
    # output: "aaa"
    # EXPLANATION:  All strings in arr are distinct, so the 1<sup>st</sup> string "aaa" is returned.
    ,
    # example 3
    [["a", "b", "a"], 3]
    # output: ""
    # EXPLANATION:  The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
