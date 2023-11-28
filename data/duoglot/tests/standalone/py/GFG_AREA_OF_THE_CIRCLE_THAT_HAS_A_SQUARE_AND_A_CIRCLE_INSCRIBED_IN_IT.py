def test():
  "--- test function ---"
  param =[(77,),(18,),(83,),(39,),(68,),(28,),(71,),(14,),(21,),(73,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
import math ;
def f_gold(a):
  area =(math.pi * a * a)/ 4
  return area
"-----------------"
test()
