def test():
  "--- test function ---"
  param =[(77,),(62,),(42,),(16,),(82,),(37,),(29,),(32,),(82,),(91,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  if(n == 0): return 1
  return n * f_gold(n - 1)
"-----------------"
test()
