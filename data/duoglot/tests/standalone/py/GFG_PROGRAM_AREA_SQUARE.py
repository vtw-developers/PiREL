def test():
  "--- test function ---"
  param =[(50,),(64,),(92,),(23,),(38,),(55,),(67,),(56,),(60,),(90,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(side):
  area = side * side
  return area
"-----------------"
test()
