def test():
  "--- test function ---"
  param =[(70, 13,),(77, 3,),(77, 73,),(88, 54,),(96, 39,),(6, 10,),(79, 95,),(44, 32,),(26, 86,),(82, 91,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(num, divisor):
  while(num >= divisor): num -= divisor ;
  return num ;
"-----------------"
test()
