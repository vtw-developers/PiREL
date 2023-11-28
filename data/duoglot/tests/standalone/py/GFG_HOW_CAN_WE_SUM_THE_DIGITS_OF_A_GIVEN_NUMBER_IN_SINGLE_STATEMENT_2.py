def test():
  "--- test function ---"
  param =[(73,),(91,),(27,),(79,),(31,),(84,),(68,),(9,),(85,),(35,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(no): return 0 if no == 0 else int(no % 10)+ f_gold(int(no / 10))
"-----------------"
test()
