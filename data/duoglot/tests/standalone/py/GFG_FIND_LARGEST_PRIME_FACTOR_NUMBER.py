def test():
  "--- test function ---"
  param =[(98,),(8,),(78,),(65,),(55,),(10,),(10,),(37,),(39,),(15,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
import math ;
def f_gold(n):
  maxPrime = - 1
  while n % 2 == 0:
    maxPrime = 2
    n >>= 1
  for i in range(3, int(math.sqrt(n))+ 1, 2):
    while n % i == 0:
      maxPrime = i
      n = n / i
  if n > 2: maxPrime = n
  return int(maxPrime)
"-----------------"
test()
