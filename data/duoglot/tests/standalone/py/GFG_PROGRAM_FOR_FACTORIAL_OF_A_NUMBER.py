def test():
  "--- test function ---"
  param =[(79,),(95,),(84,),(12,),(72,),(67,),(82,),(14,),(2,),(69,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n): return 1 if(n == 1 or n == 0)else n * f_gold(n - 1);
"-----------------"
test()
