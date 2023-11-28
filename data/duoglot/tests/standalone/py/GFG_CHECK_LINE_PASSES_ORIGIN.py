def test():
  "--- test function ---"
  param =[(1, 28, 2, 56,),(10, 0, 20, 0,),(0, 1, 0, 17,),(1, 1, 10, 10,),(82, 86, 19, 4,),(78, 86, 11, 6,),(13, 46, 33, 33,),(18, 29, 95, 12,),(42, 35, 25, 36,),(29, 17, 45, 35,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(x1, y1, x2, y2): return(x1 *(y2 - y1)== y1 *(x2 - x1))
"-----------------"
test()
