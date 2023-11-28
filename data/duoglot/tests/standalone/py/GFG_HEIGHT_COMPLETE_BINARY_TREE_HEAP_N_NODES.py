def test():
  "--- test function ---"
  param =[(65,),(94,),(52,),(31,),(9,),(1,),(41,),(98,),(45,),(24,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
import math ;
def f_gold(N): return math.ceil(math.log2(N + 1))- 1
"-----------------"
test()
