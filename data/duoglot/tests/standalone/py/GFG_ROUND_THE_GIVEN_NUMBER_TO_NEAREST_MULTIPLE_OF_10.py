def test():
  "--- test function ---"
  param =[(31,),(78,),(19,),(36,),(77,),(94,),(86,),(16,),(95,),(2,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  a =(n // 10)* 10
  b = a + 10
  return(b if n - a > b - n else a)
"-----------------"
test()
