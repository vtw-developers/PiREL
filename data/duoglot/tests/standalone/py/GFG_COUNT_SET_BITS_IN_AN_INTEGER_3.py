def test():
  "--- test function ---"
  param =[(6,),(58,),(90,),(69,),(15,),(54,),(60,),(51,),(46,),(91,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  if(n == 0): return 0
  else: return 1 + f_gold(n &(n - 1))
"-----------------"
test()
