def test():
  "--- test function ---"
  param =[(99, 75, 40,),(11, 4, 41,),(51, 37, 23,),(49, 51, 88,),(9, 34, 30,),(90, 85, 55,),(19, 96, 41,),(17, 96, 37,),(54, 3, 51,),(5, 69, 60,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(a, b, mod):
  res = 0 ;
  a = a % mod ;
  while(b > 0):
    if(b % 2 == 1): res =(res + a)% mod ;
    a =(a * 2)% mod ;
    b //= 2 ;
  return res % mod ;
"-----------------"
test()
