def test():
  "--- test function ---"
  param =[(34,),(56,),(90,),(47,),(36,),(63,),(21,),(76,),(18,),(75,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
import math ;
def f_gold(r):
  if(r <= 0): return 0
  result = 4
  for x in range(1, r):
    ySquare = r * r - x * x
    y = int(math.sqrt(ySquare))
    if(y * y == ySquare): result += 4
  return result
"-----------------"
test()
