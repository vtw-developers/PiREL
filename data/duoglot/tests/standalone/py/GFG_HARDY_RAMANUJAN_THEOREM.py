def test():
  "--- test function ---"
  param =[(99,),(33,),(50,),(17,),(18,),(69,),(23,),(18,),(94,),(16,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
import math ;
def f_gold(n):
  count = 0
  if(n % 2 == 0):
    count = count + 1
    while(n % 2 == 0): n = int(n / 2)
  i = 3
  while(i <= int(math.sqrt(n))):
    if(n % i == 0):
      count = count + 1
      while(n % i == 0): n = int(n / i)
    i = i + 2
  if(n > 2): count = count + 1
  return count
"-----------------"
test()
