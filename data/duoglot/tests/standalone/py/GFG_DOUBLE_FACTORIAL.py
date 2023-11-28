def test():
  "--- test function ---"
  param =[(52,),(93,),(15,),(72,),(61,),(21,),(83,),(87,),(75,),(75,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  if(n == 0 or n == 1): return 1 ;
  return n * f_gold(n - 2);
"-----------------"
test()
