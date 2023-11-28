def test():
  "--- test function ---"
  param =[(52,),(75,),(25,),(80,),(18,),(17,),(33,),(8,),(99,),(8,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  nCr = 1
  res = 1
  for r in range(1, n + 1): nCr =(nCr *(n + 1 - r))/ r ; res += nCr * nCr ;
  return res ;
"-----------------"
test()
