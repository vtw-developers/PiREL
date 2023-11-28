def test():
  "--- test function ---"
  param =[(68,),(91,),(99,),(79,),(61,),(48,),(89,),(20,),(83,),(1,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  dp =[[0] *(n + 1)for i in range(2)]
  dp[0][1] = 1
  dp[1][1] = 2
  for i in range(2, n + 1):
    dp[0][i] = dp[0][i - 1] + dp[1][i - 1]
    dp[1][i] =(dp[0][i - 1] * 2 + dp[1][i - 1])
  return dp[0][n] + dp[1][n]
"-----------------"
test()
