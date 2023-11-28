def test():
  "--- test function ---"
  param =[(46,),(5,),(44,),(15,),(72,),(2,),(86,),(17,),(30,),(42,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n): return(3.0 * n)/(4.0 *(n * n)- 1)
"-----------------"
test()
