from L1257_SmallestCommonRegion import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[["Earth", "North America", "South America"], ["North America", "United States", "Canada"], ["United States", "New York", "Boston"], ["Canada", "Ontario", "Quebec"], ["South America", "Brazil"]], "Quebec", "New York"]
    # output: "North America"
    ,
    # example 2
    [[["Earth", "North America", "South America"], ["North America", "United States", "Canada"], ["United States", "New York", "Boston"], ["Canada", "Ontario", "Quebec"], ["South America", "Brazil"]], "Canada", "South America"]
    # output: "Earth"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
