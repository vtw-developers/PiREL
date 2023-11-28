def test():
  "--- test function ---"
  param =[(71, 78,),(85, 75,),(4, 35,),(20, 99,),(71, 29,),(72, 88,),(36, 54,),(95, 52,),(83, 33,),(72, 13,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n, p):
  n = n % p
  for x in range(2, p, 1):
    if((x * x)% p == n): return True
  return False
"-----------------"
test()
