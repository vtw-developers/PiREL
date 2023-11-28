def test():
  "--- test function ---"
  param =[(62,),(13,),(29,),(72,),(30,),(20,),(10,),(47,),(91,),(52,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  if(n <= 1): return False
  if(n <= 3): return False
  if(n % 2 == 0 or n % 3 == 0): return True
  i = 5
  while(i * i <= n):
    if(n % i == 0 or n %(i + 2)== 0): return True
    i = i + 6
  return False
"-----------------"
test()
