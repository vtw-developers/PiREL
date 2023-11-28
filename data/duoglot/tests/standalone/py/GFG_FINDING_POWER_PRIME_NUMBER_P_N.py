def test():
  "--- test function ---"
  param =[(49, 30,),(80, 25,),(10, 9,),(81, 57,),(11, 4,),(45, 34,),(86, 90,),(27, 78,),(80, 60,),(97, 31,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n, p):
  ans = 0 ;
  temp = p ;
  while(temp <= n): ans += n / temp ; temp = temp * p ;
  return ans ;
"-----------------"
test()
