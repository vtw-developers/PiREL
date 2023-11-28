def test():
  "--- test function ---"
  param =[(95,),(49,),(10,),(73,),(74,),(40,),(10,),(94,),(64,),(16,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(base):
  base =(base - 2)
  base = base / 2
  return base *(base + 1)/ 2
"-----------------"
test()
