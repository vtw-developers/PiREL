def test():
  "--- test function ---"
  param =[(57,),(21,),(11,),(64,),(88,),(62,),(17,),(49,),(22,),(19,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  sum = 0
  while(n != 0):
    sum = sum + int(n % 10)
    n = int(n / 10)
  return sum
"-----------------"
test()
