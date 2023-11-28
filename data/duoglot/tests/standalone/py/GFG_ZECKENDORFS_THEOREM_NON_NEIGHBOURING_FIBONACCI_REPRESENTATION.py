def test():
  "--- test function ---"
  param =[(54,),(71,),(64,),(71,),(96,),(43,),(70,),(94,),(95,),(69,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  if(n == 0 or n == 1): return n
  f1, f2, f3 = 0, 1, 1
  while(f3 <= n): f1 = f2 ; f2 = f3 ; f3 = f1 + f2 ;
  return f2 ;
"-----------------"
test()
