def test():
  "--- test function ---"
  param =[(5859.798616323926,),(- 6381.210375893524,),(2442.246292006922,),(- 9624.81536339737,),(8679.436805247444,),(- 2682.3245401089525,),(7216.9161613024435,),(- 5881.789859815442,),(2497.776395789202,),(- 9598.912195459263,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
import math ;
def f_gold(side): return(2 *(1 +(math.sqrt(2)))* side * side)
"-----------------"
test()
