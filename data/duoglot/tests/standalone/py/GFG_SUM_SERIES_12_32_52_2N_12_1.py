def test():
  "--- test function ---"
  param =[(84,),(74,),(91,),(34,),(36,),(28,),(70,),(7,),(24,),(47,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n): return int((n *(2 * n - 1)*(2 * n + 1))/ 3)
"-----------------"
test()
