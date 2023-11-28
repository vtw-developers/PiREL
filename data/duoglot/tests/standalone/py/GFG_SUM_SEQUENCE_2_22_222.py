def test():
  "--- test function ---"
  param =[(88,),(79,),(7,),(36,),(23,),(10,),(27,),(30,),(71,),(6,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
import math ;
def f_gold(n): return 0.0246 *(math.pow(10, n)- 1 -(9 * n))
"-----------------"
test()
