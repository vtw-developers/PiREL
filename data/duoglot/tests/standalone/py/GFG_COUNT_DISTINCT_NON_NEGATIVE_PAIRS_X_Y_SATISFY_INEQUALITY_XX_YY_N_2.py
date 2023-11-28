def test():
  "--- test function ---"
  param =[(61,),(45,),(53,),(4,),(82,),(86,),(37,),(48,),(81,),(50,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  res = 0
  x = 0
  while(x * x < n):
    y = 0
    while(x * x + y * y < n):
      res = res + 1
      y = y + 1
    x = x + 1
  return res
"-----------------"
test()
