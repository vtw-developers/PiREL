def test():
  "--- test function ---"
  param =[(1,),(2,),(8,),(1024,),(24,),(7,),(46,),(61,),(73,),(66,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  if(n == 0): return False
  while(n != 1):
    if(n % 2 != 0): return False
    n = n // 2
  return True
"-----------------"
test()
