def test():
  "--- test function ---"
  param =[(94,),(94,),(79,),(39,),(16,),(90,),(64,),(76,),(83,),(47,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  odd_count = 0
  even_count = 0
  if(n < 0): n = - n
  if(n == 0): return 1
  if(n == 1): return 0
  while(n):
    if(n & 1): odd_count += 1
    if(n & 2): even_count += 1
    n = n >> 2
  return f_gold(abs(odd_count - even_count))
"-----------------"
test()
