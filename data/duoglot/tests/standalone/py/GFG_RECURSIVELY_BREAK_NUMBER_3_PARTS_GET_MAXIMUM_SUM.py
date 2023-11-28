def test():
  "--- test function ---"
  param =[(39,),(79,),(7,),(76,),(48,),(18,),(58,),(17,),(36,),(5,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  if(n == 0 or n == 1): return n
  return max((f_gold(n // 2)+ f_gold(n // 3)+ f_gold(n // 4)), n)
"-----------------"
test()
