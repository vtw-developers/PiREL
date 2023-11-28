def test():
  "--- test function ---"
  param =[(57, 57,),(22, 22,),(17, 17,),(74, 74,),(93, 22,),(56, 54,),(5, 33,),(5, 68,),(9, 75,),(98, 21,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n, m): return n if(n == m)else 1
"-----------------"
test()
