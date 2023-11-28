def test():
  "--- test function ---"
  param =[(46,),(68,),(4,),(12,),(56,),(14,),(81,),(29,),(26,),(40,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n): return int(1 + n *(n + 1)/ 2)
"-----------------"
test()
