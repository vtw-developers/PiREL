from L2320_CountNumberofWaystoPlaceHouses import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1]
    # output: 4
    # EXPLANATION:   Possible arrangements: 1. All plots are empty. 2. A house is placed on one side of the street. 3. A house is placed on the other side of the street. 4. Two houses are placed, one on each side of the street.
    ,
    # example 2
    [2]
    # output: 9
    # EXPLANATION:  The 9 possible arrangements are shown in the diagram above.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
