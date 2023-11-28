def test():
  "--- test function ---"
  param =[(44, 17, 10, 65,),(33, 81, 67, 20,),(39, 77, 21, 34,),(52, 96, 23, 97,),(64, 48, 17, 33,),(45, 32, 89, 3,),(53, 88, 24, 74,),(86, 19, 29, 21,),(57, 67, 30, 32,),(11, 86, 96, 81,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(a, b, x, y):
  if a == 0:
    x = 0
    y = 1
    return b
  x1 = 1
  y1 = 1
  gcd = f_gold(b % a, a, x1, y1)
  x = y1 -(b / a)* x1
  y = x1
  return gcd
"-----------------"
test()
