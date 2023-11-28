def test():
  "--- test function ---"
  param =[(68,),(70,),(69,),(93,),(99,),(44,),(91,),(8,),(83,),(51,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
import math ;
def f_gold(n):
  nthElement = 19 +(n - 1)* 9
  outliersCount = int(math.log10(nthElement))- 1
  nthElement += 9 * outliersCount
  return nthElement
"-----------------"
test()
