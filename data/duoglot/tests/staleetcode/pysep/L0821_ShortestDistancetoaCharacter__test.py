from L0821_ShortestDistancetoaCharacter import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["loveleetcode", "e"]
    # output: [3,2,1,0,1,0,0,1,2,2,1,0]
    # EXPLANATION:  The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed). The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3. The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 2. For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1. The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.
    ,
    # example 2
    ["aaab", "b"]
    # output: [3,2,1,0]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
