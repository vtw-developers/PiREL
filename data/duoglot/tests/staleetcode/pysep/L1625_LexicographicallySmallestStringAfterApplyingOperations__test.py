from L1625_LexicographicallySmallestStringAfterApplyingOperations import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["5525", 9, 2]
    # output: "2050"
    # EXPLANATION:  We can apply the following operations: Start:  "5525" Rotate: "2555" Add:    "2454" Add:    "2353" Rotate: "5323" Add:    "5222" Add:    "5121" Rotate: "2151"        Add:    "2050"             There is no way to obtain a string that is lexicographically smaller then "2050".
    ,
    # example 2
    ["74", 5, 1]
    # output: "24"
    # EXPLANATION:  We can apply the following operations: Start:  "74" Rotate: "47"        Add:    "42"        Rotate: "24"             There is no way to obtain a string that is lexicographically smaller then "24".
    ,
    # example 3
    ["0011", 4, 2]
    # output: "0011"
    # EXPLANATION:  There are no sequence of operations that will give us a lexicographically smaller string than "0011".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
