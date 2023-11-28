def test():
  "--- test function ---"
  param =[(78,),(89,),(46,),(56,),(79,),(71,),(80,),(77,),(48,),(16,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n): ans = 2 *(pow(3, n))- 1 ; return ans ;
"-----------------"
test()
