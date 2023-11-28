def test():
  "--- test function ---"
  param =[(96,),(93,),(15,),(8,),(21,),(14,),(11,),(79,),(24,),(94,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n): return(3 * n * n - n)/ 2
"-----------------"
test()
