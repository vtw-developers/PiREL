def test():
  "--- test function ---"
  param =[(57,),(96,),(14,),(64,),(24,),(74,),(85,),(27,),(78,),(1,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(k): return k * k * k
"-----------------"
test()
