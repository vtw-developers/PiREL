from L1903_LargestOddNumberinString import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["52"]
    # output: "5"
    # EXPLANATION:  The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
    ,
    # example 2
    ["4206"]
    # output: ""
    # EXPLANATION:  There are no odd numbers in "4206".
    ,
    # example 3
    ["35427"]
    # output: "35427"
    # EXPLANATION:  "35427" is already an odd number.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
