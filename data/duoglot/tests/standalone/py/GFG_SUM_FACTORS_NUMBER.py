def test():
  "--- test function ---"
  param =[(76,),(21,),(4,),(49,),(35,),(55,),(43,),(39,),(36,),(5,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
import math ;
def f_gold(n):
  result = 0
  for i in range(2,(int)(math.sqrt(n))+ 1):
    if(n % i == 0):
      if(i ==(n / i)): result = result + i
      else: result = result +(i + n // i)
  return(result + n + 1)
"-----------------"
test()
