def test():
  "--- test function ---"
  param =[(2,),(39,),(31,),(45,),(35,),(94,),(67,),(50,),(4,),(63,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  sum = 0 ;
  while(n > 0): sum +=(n % 10); n //= 10 ;
  if(sum == 1): return 10 ;
  return sum ;
"-----------------"
test()
