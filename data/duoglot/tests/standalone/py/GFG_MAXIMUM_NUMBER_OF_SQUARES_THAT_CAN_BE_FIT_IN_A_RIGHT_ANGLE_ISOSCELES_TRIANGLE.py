def test():
  "--- test function ---"
  param =[(40, 74,),(38, 35,),(47, 71,),(52, 29,),(21, 9,),(50, 33,),(8, 82,),(56, 80,),(93, 5,),(21, 90,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(b, m): return(b / m - 1)*(b / m)/ 2
"-----------------"
test()
