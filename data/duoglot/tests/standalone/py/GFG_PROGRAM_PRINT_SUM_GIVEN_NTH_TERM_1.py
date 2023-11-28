def test():
  "--- test function ---"
  param =[(42,),(40,),(67,),(73,),(18,),(16,),(74,),(33,),(92,),(22,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
import math ;
def f_gold(n): return math.pow(n, 2)
"-----------------"
test()
