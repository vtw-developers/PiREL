def test():
  "--- test function ---"
  param =[(60,),(44,),(72,),(90,),(99,),(45,),(27,),(11,),(65,),(52,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  arr =[[0 for x in range(n)] for y in range(n)]
  for i in range(n):
    for j in range(n): arr[i][j] = abs(i - j)
  sum = 0
  for i in range(n):
    for j in range(n): sum += arr[i][j]
  return sum
"-----------------"
test()
