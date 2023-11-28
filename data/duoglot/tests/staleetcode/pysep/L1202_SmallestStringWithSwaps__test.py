from L1202_SmallestStringWithSwaps import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["dcab", [[0, 3], [1, 2]]]
    # output: "bacd"<strong>Explaination:</strong> Swap s[0] and s[3], s = "bcad"Swap s[1] and s[2], s = "bacd"
    ,
    # example 2
    ["dcab", [[0, 3], [1, 2], [0, 2]]]
    # output: "abcd"<strong>Explaination: </strong>Swap s[0] and s[3], s = "bcad"Swap s[0] and s[2], s = "acbd"Swap s[1] and s[2], s = "abcd"
    ,
    # example 3
    ["cba", [[0, 1], [1, 2]]]
    # output: "abc"<strong>Explaination: </strong>Swap s[0] and s[1], s = "bca"Swap s[1] and s[2], s = "bac"Swap s[0] and s[1], s = "abc"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
