def test():
  "--- test function ---"
  param =[(57,),(28,),(23,),(79,),(52,),(42,),(79,),(77,),(99,),(70,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n): return 1 if(n == 1 or n == 0)else n * f_gold(n - 1);
"-----------------"
test()
