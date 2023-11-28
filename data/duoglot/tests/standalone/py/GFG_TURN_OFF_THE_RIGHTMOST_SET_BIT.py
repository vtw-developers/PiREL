def test():
  "--- test function ---"
  param =[(9,),(54,),(60,),(32,),(41,),(64,),(4,),(51,),(57,),(92,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n): return n &(n - 1)
"-----------------"
test()
