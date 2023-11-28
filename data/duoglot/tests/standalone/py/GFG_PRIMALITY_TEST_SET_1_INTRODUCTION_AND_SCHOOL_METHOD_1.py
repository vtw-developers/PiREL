def test():
  "--- test function ---"
  param =[(15,),(90,),(38,),(65,),(91,),(16,),(48,),(74,),(14,),(47,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  if(n <= 1): return False
  if(n <= 3): return True
  if(n % 2 == 0 or n % 3 == 0): return False
  i = 5
  while(i * i <= n):
    if(n % i == 0 or n %(i + 2)== 0): return False
    i = i + 6
  return True
"-----------------"
test()
