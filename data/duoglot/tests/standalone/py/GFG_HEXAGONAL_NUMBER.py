def test():
  "--- test function ---"
  param =[(38,),(44,),(58,),(10,),(31,),(53,),(94,),(64,),(71,),(59,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n): return n *(2 * n - 1)
"-----------------"
test()
