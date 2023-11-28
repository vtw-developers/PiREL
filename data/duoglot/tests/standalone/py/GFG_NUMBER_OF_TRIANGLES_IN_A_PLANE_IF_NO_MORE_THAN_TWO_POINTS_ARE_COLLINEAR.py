def test():
  "--- test function ---"
  param =[(67,),(58,),(67,),(60,),(4,),(97,),(9,),(16,),(83,),(87,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n): return(n *(n - 1)*(n - 2)// 6)
"-----------------"
test()
