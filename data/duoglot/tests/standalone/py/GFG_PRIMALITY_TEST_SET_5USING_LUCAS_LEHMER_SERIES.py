def test():
  "--- test function ---"
  param =[(11,),(27,),(31,),(47,),(3,),(14,),(41,),(72,),(39,),(22,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(p):
  checkNumber = 2 ** p - 1
  nextval = 4 % checkNumber
  for i in range(1, p - 1): nextval =(nextval * nextval - 2)% checkNumber
  if(nextval == 0): return True
  else: return False
"-----------------"
test()
