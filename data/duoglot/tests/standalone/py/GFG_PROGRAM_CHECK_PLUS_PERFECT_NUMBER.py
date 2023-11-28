def test():
  "--- test function ---"
  param =[(371,),(9474,),(85,),(35,),(54,),(17,),(97,),(63,),(12,),(43,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
import math ;
def f_gold(x):
  temp = x
  n = 0
  while(x != 0):
    x = x // 10
    n = n + 1
  x = temp
  sm = 0
  while(x != 0):
    sm = sm +(int)(math.pow(x % 10, n))
    x = x // 10
  return(sm == temp)
"-----------------"
test()
