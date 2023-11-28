def test():
  "--- test function ---"
  param =[(20,),(68,),(52,),(61,),(3,),(88,),(41,),(78,),(94,),(18,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(x): return(-(~ x));
"-----------------"
test()
