def test():
  "--- test function ---"
  param =[(72,),(90,),(61,),(28,),(70,),(13,),(7,),(98,),(99,),(67,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  res = 1
  for i in range(0, n):
    res *=(2 * n - i)
    res /=(i + 1)
  return res /(n + 1)
"-----------------"
test()
