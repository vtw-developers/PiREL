def test():
  "--- test function ---"
  param =[(474,),(9445,),(90,),(30,),(37453,),(27,),(2400,),(98,),(46,),(722,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
import math ;
def f_gold(n):
  ar =[0] * 10
  while(n > 0):
    digit = math.floor(n % 10)
    if(ar[digit]): return 0
    ar[digit] = 1
    n = n / 10
  return 1
"-----------------"
test()
