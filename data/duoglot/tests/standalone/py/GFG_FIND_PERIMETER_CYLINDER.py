def test():
  "--- test function ---"
  param =[(70, 78,),(97, 46,),(49, 26,),(56, 61,),(87, 79,),(64, 21,),(75, 93,),(90, 16,),(55, 16,),(73, 29,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(diameter, height): return 2 *(diameter + height)
"-----------------"
test()
