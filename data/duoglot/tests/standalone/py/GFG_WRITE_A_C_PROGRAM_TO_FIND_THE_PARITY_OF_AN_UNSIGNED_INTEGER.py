def test():
  "--- test function ---"
  param =[(63,),(64,),(85,),(36,),(20,),(63,),(42,),(19,),(62,),(97,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  parity = 0
  while n:
    parity = ~ parity
    n = n &(n - 1)
  return parity
"-----------------"
test()
