def test():
  "--- test function ---"
  param =[(62,),(53,),(8,),(6,),(35,),(35,),(46,),(74,),(69,),(3,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  if(n == 2 or n == 3): return(n - 1)
  res = 1
  while(n > 4):
    n -= 3
    res *= 3
  return(n * res)
"-----------------"
test()
