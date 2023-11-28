from L0567_PermutationinString import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["ab", "eidbaooo"]
    # output: true
    # EXPLANATION:  s2 contains one permutation of s1 ("ba").
    ,
    # example 2
    ["ab", "eidboaoo"]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
