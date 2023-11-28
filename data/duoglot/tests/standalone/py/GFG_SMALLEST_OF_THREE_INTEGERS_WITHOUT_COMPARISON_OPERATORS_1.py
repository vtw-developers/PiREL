def test():
  "--- test function ---"
  param =[(48, 63, 56,),(11, 55, 84,),(50, 89, 96,),(21, 71, 74,),(94, 39, 42,),(22, 44, 86,),(3, 41, 68,),(67, 62, 94,),(59, 2, 83,),(50, 11, 1,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(x, y, z):
  if(not(y / x)): return y if(not(y / z))else z
  return x if(not(x / z))else z
"-----------------"
test()
