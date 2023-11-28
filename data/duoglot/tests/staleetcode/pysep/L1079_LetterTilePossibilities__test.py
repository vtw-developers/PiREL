from L1079_LetterTilePossibilities import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["AAB"]
    # output: 8
    # EXPLANATION: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
    ,
    # example 2
    ["AAABBC"]
    # output: 188
    ,
    # example 3
    ["V"]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
