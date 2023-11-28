def test():
  "--- test function ---"
  param =[(17,),(66,),(53,),(97,),(34,),(54,),(9,),(99,),(59,),(87,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(N):
  if(N == 1): return 4
  countB = 1
  countS = 1
  for i in range(2, N + 1):
    prev_countB = countB
    prev_countS = countS
    countS = prev_countB + prev_countS
    countB = prev_countS
  result = countS + countB
  return(result * result)
"-----------------"
test()
