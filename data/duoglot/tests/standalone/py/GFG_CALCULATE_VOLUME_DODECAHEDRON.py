def test():
  "--- test function ---"
  param =[(56,),(73,),(22,),(10,),(84,),(20,),(51,),(91,),(10,),(83,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
import math ;
def f_gold(side): return(((15 +(7 *(math.sqrt(5))))/ 4)*(math.pow(side, 3)))
"-----------------"
test()
