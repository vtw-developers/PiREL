def test():
  "--- test function ---"
  param =[(94, 4, 69,),(7, 12, 33,),(20, 44, 24,),(90, 94, 88,),(50, 58, 27,),(32, 90, 29,),(46, 25, 6,),(82, 50, 87,),(43, 82, 70,),(6, 83, 19,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(m, n, x):
  table =[[0] *(x + 1)for i in range(n + 1)]
  for j in range(1, min(m + 1, x + 1)): table[1][j] = 1
  for i in range(2, n + 1):
    for j in range(1, x + 1):
      for k in range(1, min(m + 1, j)): table[i][j] += table[i - 1][j - k]
  return table[- 1][- 1]
"-----------------"
test()
