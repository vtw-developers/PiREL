def test():
  "--- test function ---"
  param =[(96,),(85,),(54,),(14,),(47,),(11,),(49,),(99,),(28,),(82,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  if(n == 0 or n == 9): return True
  if(n < 9): return False
  return f_gold((int)(n >> 3)-(int)(n & 7))
"-----------------"
test()
