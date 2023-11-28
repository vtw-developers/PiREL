def test():
  "--- test function ---"
  param =[(50,),(92,),(49,),(94,),(7,),(30,),(88,),(98,),(94,),(23,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  sum = 0
  while(n > 0):
    sum += int(n % 10)
    n = int(n / 10)
  return sum
"-----------------"
test()
