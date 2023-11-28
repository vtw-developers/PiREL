def test():
  "--- test function ---"
  param =[(23, 98, 25,),(87, 55, 94,),(35, 90, 29,),(25, 9, 41,),(93, 22, 39,),(52, 42, 96,),(95, 88, 26,),(91, 64, 51,),(75, 1, 6,),(96, 44, 76,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(x, y, z):
  c = 0
  while(x and y and z):
    x = x - 1
    y = y - 1
    z = z - 1
    c = c + 1
  return c
"-----------------"
test()
