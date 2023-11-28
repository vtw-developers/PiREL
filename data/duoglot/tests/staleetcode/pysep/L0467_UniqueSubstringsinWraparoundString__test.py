from L0467_UniqueSubstringsinWraparoundString import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["a"]
    # output: 1
    # EXPLANATION:  Only the substring "a" of p is in s.
    ,
    # example 2
    ["cac"]
    # output: 2
    # EXPLANATION:  There are two substrings ("a", "c") of p in s.
    ,
    # example 3
    ["zab"]
    # output: 6
    # EXPLANATION:  There are six substrings ("z", "a", "b", "za", "ab", and "zab") of p in s.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
