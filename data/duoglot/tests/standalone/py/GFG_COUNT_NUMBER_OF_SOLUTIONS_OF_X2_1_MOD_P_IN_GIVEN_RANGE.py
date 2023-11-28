def test():
  "--- test function ---"
  param =[(94, 36,),(11, 79,),(88, 63,),(85, 43,),(74, 89,),(96, 33,),(49, 51,),(50, 24,),(21, 26,),(81, 19,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n, p):
  ans = 0 ;
  for x in range(1, p):
    if((x * x)% p == 1):
      last = x + p *(n / p);
      if(last > n): last -= p ;
      ans +=((last - x)/ p + 1);
  return int(ans);
"-----------------"
test()
