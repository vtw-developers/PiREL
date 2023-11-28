def test():
  "--- test function ---"
  param =[(54, 83,),(42, 56,),(63, 12,),(19, 76,),(41, 50,),(7, 26,),(39, 42,),(11, 64,),(96, 81,),(15, 54,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
import math ;
def f_gold(a, b):
  AM =(a + b)/ 2
  GM = math.sqrt(a * b)
  HM =(GM * GM)/ AM
  return HM
"-----------------"
test()
