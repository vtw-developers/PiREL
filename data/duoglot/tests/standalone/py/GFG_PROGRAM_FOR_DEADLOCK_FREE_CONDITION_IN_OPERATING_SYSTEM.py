def test():
  "--- test function ---"
  param =[(38, 37,),(82, 3,),(2, 26,),(38, 72,),(31, 85,),(80, 73,),(11, 9,),(2, 31,),(26, 59,),(37, 67,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(process, need):
  minResources = 0
  minResources = process *(need - 1)+ 1
  return minResources
"-----------------"
test()
