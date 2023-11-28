def test():
  "--- test function ---"
  param =[(40,),(11,),(94,),(73,),(6,),(73,),(58,),(40,),(64,),(66,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  N = 10
  count = 1
  for i in range(1, n + 1):
    count = int(count *(N + i - 1))
    count = int(count / i)
  return count
"-----------------"
test()
