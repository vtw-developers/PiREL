def test():
  "--- test function ---"
  param =[(8,),(39,),(25,),(44,),(72,),(6,),(72,),(62,),(48,),(39,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  C =[[0] *(n + 2)for i in range(0, n + 2)]
  for i in range(0, n + 1):
    for j in range(0, min(i, n)+ 1):
      if(j == 0 or j == i): C[i][j] = 1
      else: C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
  sum = 0
  for i in range(0, n + 1): sum += C[n][i]
  return sum
"-----------------"
test()
