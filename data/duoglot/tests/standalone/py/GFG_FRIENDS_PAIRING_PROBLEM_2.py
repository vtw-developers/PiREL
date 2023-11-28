def test():
  "--- test function ---"
  param =[(24,),(1,),(91,),(90,),(89,),(29,),(3,),(60,),(75,),(14,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  a, b, c = 1, 2, 0 ;
  if(n <= 2): return n ;
  for i in range(3, n + 1): c = b +(i - 1)* a ; a = b ; b = c ;
  return c ;
"-----------------"
test()
