def test():
  "--- test function ---"
  param =[(58, 39,),(37, 49,),(56, 52,),(22, 43,),(77, 12,),(34, 31,),(74, 54,),(37, 52,),(21, 37,),(75, 30,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(l, w): return(2 *(l + w))
"-----------------"
test()
