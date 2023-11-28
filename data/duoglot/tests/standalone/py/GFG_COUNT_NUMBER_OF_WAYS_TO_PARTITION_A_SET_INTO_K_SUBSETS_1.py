def test():
  "--- test function ---"
  param =[(84, 99,),(95, 64,),(67, 21,),(92, 22,),(97, 35,),(13, 77,),(37, 46,),(9, 92,),(10, 26,),(90, 94,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n, k):
  dp =[[0 for i in range(k + 1)] for j in range(n + 1)]
  for i in range(n + 1): dp[i][0] = 0
  for i in range(k + 1): dp[0][k] = 0
  for i in range(1, n + 1):
    for j in range(1, k + 1):
      if(j == 1 or i == j): dp[i][j] = 1
      else: dp[i][j] =(j * dp[i - 1][j] + dp[i - 1][j - 1])
  return dp[n][k]
"-----------------"
test()
