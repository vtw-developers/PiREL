def test():
  "--- test function ---"
  param =[(8, 4, 2, 6, 0,),(400, 1, 10, 74, 38,),(1, 400, 10, 74, 38,),(61, 40, 2, 50, 0,),(60, 49, 68, 77, 71,),(88, 10, 69, 71, 26,),(60, 79, 92, 29, 38,),(26, 88, 75, 84, 10,),(33, 65, 57, 21, 61,),(70, 57, 77, 52, 87,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
import math ;
def f_gold(r, R, r1, x1, y1):
  dis = int(math.sqrt(x1 * x1 + y1 * y1))
  return(dis - r1 >= R and dis + r1 <= r)
"-----------------"
test()
