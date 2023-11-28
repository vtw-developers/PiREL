def test():
  "--- test function ---"
  param =[(41,),(42,),(62,),(4,),(31,),(75,),(5,),(75,),(85,),(19,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n): return((n << 3)- n)
"-----------------"
test()
