def test():
  "--- test function ---"
  param =[(72,),(28,),(45,),(41,),(94,),(97,),(97,),(36,),(91,),(84,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  if n == 1: return 2
  return 2 * f_gold(n - 1)
"-----------------"
test()
