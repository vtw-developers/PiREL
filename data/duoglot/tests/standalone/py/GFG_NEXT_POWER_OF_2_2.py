def test():
  "--- test function ---"
  param =[(63,),(78,),(13,),(5,),(34,),(69,),(63,),(78,),(80,),(19,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  n -= 1
  n |= n >> 1
  n |= n >> 2
  n |= n >> 4
  n |= n >> 8
  n |= n >> 16
  n += 1
  return n
"-----------------"
test()
