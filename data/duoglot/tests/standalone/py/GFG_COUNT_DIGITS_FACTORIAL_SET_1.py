def test():
  "--- test function ---"
  param =[(66,),(7,),(55,),(37,),(76,),(16,),(17,),(95,),(71,),(90,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
import math ;
def f_gold(n):
  if(n < 0): return 0 ;
  if(n <= 1): return 1 ;
  digits = 0 ;
  for i in range(2, n + 1): digits += math.log10(i);
  return math.floor(digits)+ 1 ;
"-----------------"
test()
