def test():
  "--- test function ---"
  param =[(4, 33,),(36, 67,),(65, 52,),(55, 37,),(35, 76,),(69, 98,),(84, 62,),(5, 80,),(15, 36,),(67, 84,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(a, b):
  res = 0
  while(b > 0):
    if(b & 1): res = res + a
    a = a << 1
    b = b >> 1
  return res
"-----------------"
test()
