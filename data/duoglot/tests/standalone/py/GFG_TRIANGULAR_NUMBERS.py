def test():
  "--- test function ---"
  param =[(97,),(97,),(32,),(40,),(18,),(14,),(90,),(39,),(1,),(57,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(num):
  if(num < 0): return False
  sum, n = 0, 1
  while(sum <= num):
    sum = sum + n
    if(sum == num): return True
    n += 1
  return False
"-----------------"
test()
