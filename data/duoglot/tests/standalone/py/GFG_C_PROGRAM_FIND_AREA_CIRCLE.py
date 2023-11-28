def test():
  "--- test function ---"
  param =[(93,),(83,),(51,),(77,),(13,),(34,),(49,),(12,),(68,),(80,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(r):
  PI = 3.142
  return PI *(r * r);
"-----------------"
test()
