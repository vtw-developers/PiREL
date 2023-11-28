def test():
  "--- test function ---"
  param =[(59, - 99,),(- 20, - 21,),(- 100, 79,),(54, - 49,),(- 16, 16,),(- 23, - 68,),(93, 37,),(24, - 61,),(- 8, 69,),(29, 10,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(x, y): return((x ^ y)< 0);
"-----------------"
test()
