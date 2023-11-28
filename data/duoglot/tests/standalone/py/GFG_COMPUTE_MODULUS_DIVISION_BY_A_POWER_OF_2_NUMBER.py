def test():
  "--- test function ---"
  param =[(54, 59,),(39, 84,),(35, 81,),(9, 60,),(62, 68,),(16, 16,),(93, 96,),(32, 38,),(39, 62,),(63, 16,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n, d): return(n &(d - 1))
"-----------------"
test()
