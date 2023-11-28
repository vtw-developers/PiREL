def test():
  "--- test function ---"
  param =[(84,),(41,),(5,),(38,),(79,),(80,),(64,),(62,),(24,),(12,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n): return 1 if(n == 1 or n == 0)else n * f_gold(n - 1);
"-----------------"
test()
