def test():
  "--- test function ---"
  param =[(64, 4,),(16, 2,),(27, 3,),(81, 72,),(1, 9,),(69, 17,),(8, 20,),(31, 79,),(43, 81,),(54, 89,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n, k):
  oneSeen = False
  while(n > 0):
    digit = n % k
    if(digit > 1): return False
    if(digit == 1):
      if(oneSeen): return False
      oneSeen = True
    n //= k
  return True
"-----------------"
test()
