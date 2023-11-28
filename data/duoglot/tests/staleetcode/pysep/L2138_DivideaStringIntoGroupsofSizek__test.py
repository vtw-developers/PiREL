from L2138_DivideaStringIntoGroupsofSizek import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abcdefghi", 3, "x"]
    # output: ["abc","def","ghi"]
    # EXPLANATION:  The first 3 characters "abc" form the first group. The next 3 characters "def" form the second group. The last 3 characters "ghi" form the third group. Since all groups can be completely filled by characters from the string, we do not need to use fill. Thus, the groups formed are "abc", "def", and "ghi".
    ,
    # example 2
    ["abcdefghij", 3, "x"]
    # output: ["abc","def","ghi","jxx"]
    # EXPLANATION:  Similar to the previous example, we are forming the first three groups "abc", "def", and "ghi". For the last group, we can only use the character 'j' from the string. To complete this group, we add 'x' twice. Thus, the 4 groups formed are "abc", "def", "ghi", and "jxx".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
