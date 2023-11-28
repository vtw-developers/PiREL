from L2259_RemoveDigitFromNumbertoMaximizeResult import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["123", "3"]
    # output: "12"
    # EXPLANATION:  There is only one '3' in "123". After removing '3', the result is "12".
    ,
    # example 2
    ["1231", "1"]
    # output: "231"
    # EXPLANATION:  We can remove the first '1' to get "231" or remove the second '1' to get "123". Since 231 > 123, we return "231".
    ,
    # example 3
    ["551", "5"]
    # output: "51"
    # EXPLANATION:  We can remove either the first or second '5' from "551". Both result in the string "51".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
