from L1888_MinimumNumberofFlipstoMaketheBinaryStringAlternating import f_gold

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
    # output: 2
    # EXPLANATION: : Use the first operation two times to make s = "100011". Then, use the second operation on the third and sixth elements to make s = "10<u>1</u>01<u>0</u>".
    ,
    # example 2
    ["010"]
    # output: 0
    # EXPLANATION: : The string is already alternating.
    ,
    # example 3
    ["1110"]
    # output: 1
    # EXPLANATION: : Use the second operation on the second element to make s = "1<u>0</u>10".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
