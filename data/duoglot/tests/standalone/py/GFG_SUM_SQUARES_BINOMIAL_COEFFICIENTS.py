def test():
  "--- test function ---"
  param =[(57,),(44,),(19,),(24,),(64,),(60,),(57,),(22,),(15,),(63,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  C =[[0 for i in range(n + 1)] for j in range(n + 1)]
  for i in range(0, n + 1):
    for j in range(0, min(i, n)+ 1):
      if(j == 0 or j == i): C[i][j] = 1
      else: C[i][j] =(C[i - 1][j - 1] + C[i - 1][j])
  sum = 0
  for i in range(0, n + 1): sum = sum +(C[n][i] * C[n][i])
  return sum
"-----------------"
test()
