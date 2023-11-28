def test():
  "--- test function ---"
  param =[(10, 4,),(5, 2,),(2, 8,),(83, 7,),(91, 0,),(18, 53,),(83, 41,),(98, 53,),(43, 37,),(31, 20,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(m, n):
  T =[[0 for i in range(n + 1)] for i in range(m + 1)]
  for i in range(m + 1):
    for j in range(n + 1):
      if i == 0 or j == 0: T[i][j] = 0
      elif i < j: T[i][j] = 0
      elif j == 1: T[i][j] = i
      else: T[i][j] = T[i - 1][j] + T[i // 2][j - 1]
  return T[m][n]
"-----------------"
test()
