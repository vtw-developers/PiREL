def test():
  "--- test function ---"
  param =[(85, 18,),(14, 13,),(83, 21,),(30, 35,),(96, 51,),(55, 58,),(82, 71,),(12, 74,),(38, 3,),(46, 73,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n, p):
  if n >= p: return 0
  result = 1
  for i in range(1, n + 1): result =(result * i)% p
  return result
"-----------------"
test()
