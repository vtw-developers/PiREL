def test():
  "--- test function ---"
  param =[(55,),(36,),(69,),(92,),(73,),(16,),(88,),(19,),(66,),(68,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n): return(1 +(n * 2)+(n *((n * n)- 1)// 2))
"-----------------"
test()
