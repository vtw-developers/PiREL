def test():
  "--- test function ---"
  param =[(91, 29,),(99, 55,),(11, 56,),(23, 56,),(12, 97,),(1, 64,),(18, 5,),(14, 37,),(13, 55,),(36, 99,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
import math ;
def f_gold(C, l):
  if(l >= C): return C
  eq_root =(math.sqrt(1 + 8 *(C - l))- 1)/ 2
  return math.ceil(eq_root)+ l
"-----------------"
test()
