def test():
  "--- test function ---"
  param =[(39,),(20,),(10,),(39,),(70,),(21,),(21,),(80,),(89,),(99,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  S = 0
  for i in range(1, n + 1): S += i * i -(i - 1)*(i - 1)
  return S
"-----------------"
test()
