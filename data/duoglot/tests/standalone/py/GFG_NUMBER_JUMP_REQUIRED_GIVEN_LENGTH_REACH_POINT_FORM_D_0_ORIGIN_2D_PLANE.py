def test():
  "--- test function ---"
  param =[(35, 8, 77,),(85, 55, 33,),(22, 23, 64,),(8, 43, 29,),(12, 64, 11,),(58, 25, 26,),(65, 4, 28,),(10, 95, 55,),(23, 13, 54,),(5, 50, 71,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(a, b, d):
  temp = a
  a = min(a, b)
  b = max(temp, b)
  if(d >= b): return(d + b - 1)/ b
  if(d == 0): return 0
  if(d == a): return 1
  return 2
"-----------------"
test()
