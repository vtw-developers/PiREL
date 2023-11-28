def test():
  "--- test function ---"
  param =[(45,),(16,),(15,),(91,),(82,),(18,),(31,),(6,),(93,),(35,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  if(n == 0): return False
  while(n != 1):
    if(n % 4 != 0): return False
    n = n // 4
  return True
"-----------------"
test()
