def test():
  "--- test function ---"
  param =[(48,),(42,),(15,),(75,),(23,),(41,),(46,),(99,),(36,),(53,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n): return(1 << n);
"-----------------"
test()
