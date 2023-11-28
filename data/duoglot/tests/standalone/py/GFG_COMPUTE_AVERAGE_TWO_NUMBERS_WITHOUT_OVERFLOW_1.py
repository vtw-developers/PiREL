def test():
  "--- test function ---"
  param =[(9, 81,),(68, 79,),(51, 2,),(31, 49,),(14, 10,),(73, 9,),(51, 13,),(75, 67,),(98, 51,),(83, 74,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(a, b): return(a // 2)+(b // 2)+((a % 2 + b % 2)// 2)
"-----------------"
test()
