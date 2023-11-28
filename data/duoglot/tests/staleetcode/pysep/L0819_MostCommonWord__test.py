from L0819_MostCommonWord import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]]
    # output: "ball"
    # EXPLANATION:   "hit" occurs 3 times, but it is a banned word. "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.  Note that words in the paragraph are not case sensitive, that punctuation is ignored (even if adjacent to words, such as "ball,"),  and that "hit" isn't the answer even though it occurs more because it is banned.
    ,
    # example 2
    ["a.", []]
    # output: "a"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
