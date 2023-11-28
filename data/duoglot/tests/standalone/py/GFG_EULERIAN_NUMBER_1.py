def test():
  "--- test function ---"
  param =[(27, 7,),(77, 34,),(35, 22,),(26, 20,),(6, 10,),(66, 47,),(44, 29,),(26, 33,),(74, 86,),(65, 97,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n, m):
  dp =[[0 for x in range(m + 1)] for y in range(n + 1)]
  for i in range(1, n + 1):
    for j in range(0, m + 1):
      if(i > j):
        if(j == 0): dp[i][j] = 1
        else: dp[i][j] =(((i - j)* dp[i - 1][j - 1])+((j + 1)* dp[i - 1][j]))
  return dp[n][m]
"-----------------"
test()
