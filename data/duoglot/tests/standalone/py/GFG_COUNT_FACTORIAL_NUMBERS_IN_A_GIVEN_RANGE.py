def test():
  "--- test function ---"
  param =[(57, 79,),(57, 21,),(31, 37,),(62, 87,),(49, 98,),(82, 76,),(31, 45,),(5, 52,),(76, 43,),(55, 6,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(low, high):
  fact = 1
  x = 1
  while(fact < low):
    fact = fact * x
    x += 1
  res = 0
  while(fact <= high):
    res += 1
    fact = fact * x
    x += 1
  return res
"-----------------"
test()
