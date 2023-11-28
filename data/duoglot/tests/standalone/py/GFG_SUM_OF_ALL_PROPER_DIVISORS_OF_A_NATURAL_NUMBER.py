def test():
  "--- test function ---"
  param =[(2,),(57,),(28,),(43,),(38,),(29,),(45,),(47,),(44,),(3,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
import math ;
def f_gold(num):
  result = 0
  i = 2
  while i <=(math.sqrt(num)):
    if(num % i == 0):
      if(i ==(num / i)): result = result + i ;
      else: result = result +(i + num / i);
    i = i + 1
  return(result + 1);
"-----------------"
test()
