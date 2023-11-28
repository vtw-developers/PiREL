def test():
  "--- test function ---"
  param =[(57, 76,),(80, 46,),(84, 96,),(35, 16,),(3, 84,),(42, 79,),(7, 2,),(99, 83,),(13, 61,),(44, 8,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(y, x): return(y % pow(2, x))
"-----------------"
test()
