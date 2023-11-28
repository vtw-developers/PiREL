def test():
  "--- test function ---"
  param =[(58,),(42,),(76,),(16,),(49,),(60,),(99,),(45,),(6,),(70,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n): return 1 if(n == 1 or n == 0)else n * f_gold(n - 1);
"-----------------"
test()
