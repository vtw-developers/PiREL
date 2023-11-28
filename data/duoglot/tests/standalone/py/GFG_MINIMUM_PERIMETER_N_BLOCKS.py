def test():
  "--- test function ---"
  param =[(45,),(80,),(54,),(48,),(83,),(68,),(32,),(20,),(68,),(66,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
import math ;
def f_gold(n):
  l = math.sqrt(n)
  sq = l * l
  if(sq == n): return l * 4
  else:
    row = n / l
    perimeter = 2 *(l + row)
    if(n % l != 0): perimeter += 2
    return perimeter
"-----------------"
test()
