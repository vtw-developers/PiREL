def test():
  "--- test function ---"
  param =[(41,),(50,),(67,),(18,),(60,),(6,),(27,),(46,),(50,),(20,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  multiTerms = n *(n + 1)// 2
  sm = multiTerms
  for i in range(2, n + 1):
    multiTerms = multiTerms -(i - 1)
    sm = sm + multiTerms * i
  return sm
"-----------------"
test()
