def test():
  "--- test function ---"
  param =[(14,),(61,),(37,),(86,),(47,),(98,),(70,),(24,),(76,),(24,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  sum = 0
  for i in range(1, n + 1): sum = sum +(2 * i - 1)*(2 * i - 1)
  return sum
"-----------------"
test()
