def test():
  "--- test function ---"
  param =[(24,),(46,),(47,),(41,),(98,),(69,),(83,),(2,),(12,),(11,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n): return 1 if(n == 1 or n == 0)else n * f_gold(n - 1)
"-----------------"
test()
