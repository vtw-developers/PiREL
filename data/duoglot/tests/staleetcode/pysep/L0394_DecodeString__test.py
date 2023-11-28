from L0394_DecodeString import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["3[a]2[bc]"]
    # output: "aaabcbc"
    ,
    # example 2
    ["3[a2[c]]"]
    # output: "accaccacc"
    ,
    # example 3
    ["2[abc]3[cd]ef"]
    # output: "abcabccdcdcdef"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
