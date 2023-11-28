from L2168_UniqueSubstringsWithEqualDigitFrequency import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["1212"]
    # output: 5
    # EXPLANATION:  The substrings that meet the requirements are "1", "2", "12", "21", "1212". Note that although the substring "12" appears twice, it is only counted once.
    ,
    # example 2
    ["12321"]
    # output: 9
    # EXPLANATION:  The substrings that meet the requirements are "1", "2", "3", "12", "23", "32", "21", "123", "321".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
