def test():
  "--- test function ---"
  param =[(29,),(0,),(65,),(1419,),(54,),(7,),(44,),(34,),(1160,),(292929002929,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  while(int(n / 100)):
    last_digit = int(n % 10)
    n = int(n / 10)
    n += last_digit * 3
  return(n % 29 == 0)
"-----------------"
test()
