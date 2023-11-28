def test():
  "--- test function ---"
  param =[(90,),(95,),(22,),(29,),(62,),(40,),(52,),(21,),(33,),(11,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n): return(n * n)+(n * n * n)
"-----------------"
test()
