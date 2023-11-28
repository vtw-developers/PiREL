def test():
  "--- test function ---"
  param =[(18,),(81,),(77,),(84,),(87,),(14,),(15,),(3,),(21,),(60,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n): return(int)(0.6172 *(pow(10, n)- 1)- 0.55 * n)
"-----------------"
test()
