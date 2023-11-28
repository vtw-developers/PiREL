from L1805_NumberofDifferentIntegersinaString import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["a123bc34d8ef34"]
    # output: 3
    # EXPLANATION: The three different integers are "123", "34", and "8". Notice that "34" is only counted once.
    ,
    # example 2
    ["leet1234code234"]
    # output: 2
    ,
    # example 3
    ["a1b01c001"]
    # output: 1
    # EXPLANATION: The three integers "1", "01", and "001" all represent the same integer because the leading zeros are ignored when comparing their decimal values.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
