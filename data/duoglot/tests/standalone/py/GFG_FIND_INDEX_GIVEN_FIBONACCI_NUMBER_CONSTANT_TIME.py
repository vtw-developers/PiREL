def test():
  "--- test function ---"
  param =[(5,),(19,),(7,),(94,),(58,),(65,),(69,),(96,),(80,),(14,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  if(n <= 1): return n
  a = 0
  b = 1
  c = 1
  res = 1
  while(c < n):
    c = a + b
    res = res + 1
    a = b
    b = c
  return res
"-----------------"
test()
