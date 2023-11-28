def test():
  "--- test function ---"
  param =[(34,),(49,),(41,),(17,),(67,),(38,),(59,),(64,),(61,),(58,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
import math ;
def f_gold(n):
  ans = 0
  for length in range(1, int(math.sqrt(n))+ 1):
    height = length
    while(height * length <= n):
      ans += 1
      height += 1
  return ans
"-----------------"
test()
