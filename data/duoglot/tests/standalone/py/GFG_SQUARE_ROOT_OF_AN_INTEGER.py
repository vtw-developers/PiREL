def test():
  "--- test function ---"
  param =[(89,),(11,),(14,),(92,),(76,),(63,),(51,),(16,),(83,),(66,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(x):
  if(x == 0 or x == 1): return x
  i = 1 ;
  result = 1
  while(result <= x):
    i += 1
    result = i * i
  return i - 1
"-----------------"
test()
