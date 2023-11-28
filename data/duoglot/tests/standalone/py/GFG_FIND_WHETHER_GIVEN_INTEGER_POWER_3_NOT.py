def test():
  "--- test function ---"
  param =[(1,),(3,),(27,),(9,),(- 9,),(11,),(57,),(21,),(60,),(44,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n): return 1162261467 % n == 0
"-----------------"
test()
