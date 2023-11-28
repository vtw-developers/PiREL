def test():
  "--- test function ---"
  param =[(67,),(47,),(57,),(89,),(67,),(40,),(16,),(83,),(93,),(43,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(x):
  i = 1 ;
  fact = 1 ;
  for i in range(1, x):
    fact = fact * i
    if(fact % x == 0): break
  return i
"-----------------"
test()
