def test():
  "--- test function ---"
  param =[(1,),(3,),(6,),(10,),(55,),(48,),(63,),(72,),(16,),(85,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
import math ;
def f_gold(num):
  if(num < 0): return False
  c =(- 2 * num)
  b, a = 1, 1
  d =(b * b)-(4 * a * c)
  if(d < 0): return False
  root1 =(- b + math.sqrt(d))/(2 * a)
  root2 =(- b - math.sqrt(d))/(2 * a)
  if(root1 > 0 and math.floor(root1)== root1): return True
  if(root2 > 0 and math.floor(root2)== root2): return True
  return False
"-----------------"
test()
