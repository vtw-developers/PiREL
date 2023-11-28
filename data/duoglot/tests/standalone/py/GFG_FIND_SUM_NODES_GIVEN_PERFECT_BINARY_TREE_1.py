def test():
  "--- test function ---"
  param =[(5,),(16,),(8,),(61,),(59,),(88,),(67,),(28,),(58,),(42,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
import math ;
def f_gold(l): leafNodeCount = math.pow(2, l - 1); sumLastLevel = 0 ; sumLastLevel =((leafNodeCount *(leafNodeCount + 1))/ 2); sum = sumLastLevel * l ; return int(sum);
"-----------------"
test()
