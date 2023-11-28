def test():
  "--- test function ---"
  param =[(80, 54,),(63, 21,),(1, 56,),(22, 39,),(66, 7,),(61, 67,),(45, 63,),(29, 44,),(95, 65,),(9, 68,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(num, divisor): return(num - divisor *(num // divisor))
"-----------------"
test()
