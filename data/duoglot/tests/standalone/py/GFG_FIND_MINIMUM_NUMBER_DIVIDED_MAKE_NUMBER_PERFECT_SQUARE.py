def test():
  "--- test function ---"
  param =[(95,),(48,),(3,),(10,),(82,),(1,),(77,),(99,),(23,),(61,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
import math ;
def f_gold(n):
  count = 0
  ans = 1
  while n % 2 == 0:
    count += 1
    n //= 2
  if count % 2 != 0: ans *= 2
  for i in range(3,(int)(math.sqrt(n))+ 1, 2):
    count = 0
    while n % i == 0:
      count += 1
      n //= i
    if count % 2 != 0: ans *= i
  if n > 2: ans *= n
  return ans
"-----------------"
test()
