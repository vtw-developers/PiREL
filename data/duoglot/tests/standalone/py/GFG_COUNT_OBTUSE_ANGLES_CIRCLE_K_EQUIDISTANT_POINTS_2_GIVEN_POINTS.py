def test():
  "--- test function ---"
  param =[(83, 98, 86,),(3, 39, 87,),(11, 96, 30,),(50, 67, 48,),(40, 16, 32,),(62, 86, 76,),(40, 78, 71,),(66, 11, 74,),(6, 9, 19,),(25, 5, 5,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(a, b, k):
  c1 =(b - a)- 1
  c2 =(k - b)+(a - 1)
  if(c1 == c2): return 0
  return min(c1, c2)
"-----------------"
test()
