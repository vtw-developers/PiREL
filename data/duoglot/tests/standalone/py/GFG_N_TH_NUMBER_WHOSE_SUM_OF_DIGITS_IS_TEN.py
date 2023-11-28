def test():
  "--- test function ---"
  param =[(37,),(13,),(51,),(69,),(76,),(10,),(97,),(40,),(69,),(4,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
import itertools ;
def f_gold(n):
  count = 0
  for curr in itertools.count():
    sum = 0
    x = curr
    while(x):
      sum = sum + x % 10
      x = x // 10
    if(sum == 10): count = count + 1
    if(count == n): return curr
  return - 1
"-----------------"
test()
