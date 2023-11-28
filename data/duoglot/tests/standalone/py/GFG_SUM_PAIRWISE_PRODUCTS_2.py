def test():
  "--- test function ---"
  param =[(57,),(18,),(97,),(9,),(42,),(67,),(71,),(66,),(69,),(18,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n): return n *(n + 1)*(n + 2)*(3 * n + 1)/ 24
"-----------------"
test()
