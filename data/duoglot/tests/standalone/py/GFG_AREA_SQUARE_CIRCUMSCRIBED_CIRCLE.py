def test():
  "--- test function ---"
  param =[(14,),(78,),(45,),(66,),(18,),(32,),(60,),(16,),(99,),(65,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(r): return(2 * r * r)
"-----------------"
test()
