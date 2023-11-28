def test():
  "--- test function ---"
  param =[(23, 16, 23, 18,),(62, 76, 81, 97,),(32, 46, 1, 78,),(82, 48, 72, 58,),(94, 99, 62, 38,),(44, 21, 46, 60,),(4, 57, 2, 77,),(53, 23, 80, 5,),(9, 55, 26, 85,),(23, 15, 73, 42,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n, a, b, c):
  dp =[- 1] *(n + 10)
  dp[0] = 0
  for i in range(0, n):
    if(dp[i] != - 1):
      if(i + a <= n): dp[i + a] = max(dp[i] + 1, dp[i + a])
      if(i + b <= n): dp[i + b] = max(dp[i] + 1, dp[i + b])
      if(i + c <= n): dp[i + c] = max(dp[i] + 1, dp[i + c])
  return dp[n]
"-----------------"
test()
