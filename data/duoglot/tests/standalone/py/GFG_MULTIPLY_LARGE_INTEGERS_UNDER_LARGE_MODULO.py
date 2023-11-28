def test():
  "--- test function ---"
  param =[(60, 24, 58,),(46, 43, 29,),(4, 50, 71,),(67, 1, 66,),(93, 35, 73,),(89, 97, 8,),(8, 78, 55,),(53, 73, 22,),(96, 92, 83,),(38, 64, 83,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(a, b, mod):
  res = 0 ;
  a = a % mod ;
  while(b):
    if(b & 1): res =(res + a)% mod ;
    a =(2 * a)% mod ;
    b >>= 1 ;
  return res ;
"-----------------"
test()
