def test():
  "--- test function ---"
  param =[(94, 0),(99, 1),(64, 3),(27, 3),(24, 4),(84, 6),(69, 98),(69, 39),(22, 60),(39, 57)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
import math ;
def f_gold(n, k):
  while(n % 2 == 0):
    k = k - 1
    n = n / 2
    if(k == 0): return 2
  i = 3
  while i <= math.sqrt(n):
    while(n % i == 0):
      if(k == 1): return i
      k = k - 1
      n = n / i
    i = i + 2
  if(n > 2 and k == 1): return n
  return - 1
"-----------------"
test()
