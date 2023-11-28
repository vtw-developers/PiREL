def test():
  "--- test function ---"
  param =[(88,),(24,),(3,),(22,),(53,),(2,),(88,),(30,),(38,),(2,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  res = 1 ;
  for i in range(n, - 1, - 2):
    if(i == 0 or i == 1): return res ;
    else: res *= i ;
"-----------------"
test()
