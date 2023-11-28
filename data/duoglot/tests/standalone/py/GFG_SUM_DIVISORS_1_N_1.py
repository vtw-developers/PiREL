def test():
  "--- test function ---"
  param =[(73,),(41,),(36,),(28,),(49,),(24,),(85,),(59,),(82,),(40,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  sum = 0
  for i in range(1, n + 1): sum += int(n / i)* i
  return int(sum)
"-----------------"
test()
