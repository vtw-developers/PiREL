from L1864_MinimumNumberofSwapstoMaketheBinaryStringAlternating import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["111000"]
    # output: 1
    # EXPLANATION:  Swap positions 1 and 4: "1<u>1</u>10<u>0</u>0" -> "1<u>0</u>10<u>1</u>0" The string is now alternating.
    ,
    # example 2
    ["010"]
    # output: 0
    # EXPLANATION:  The string is already alternating, no swaps are needed.
    ,
    # example 3
    ["1110"]
    # output: -1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
