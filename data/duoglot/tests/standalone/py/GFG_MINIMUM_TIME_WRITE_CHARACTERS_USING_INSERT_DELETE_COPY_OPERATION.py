def test():
  "--- test function ---"
  param =[(59, 75, 12, 45,),(66, 68, 32, 41,),(98, 55, 69, 5,),(63, 4, 41, 12,),(99, 37, 98, 55,),(45, 28, 59, 7,),(60, 53, 40, 52,),(11, 96, 50, 50,),(96, 95, 48, 84,),(54, 6, 50, 82,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(N, insrt, remov, cpy):
  if N == 0: return 0
  if N == 1: return insrt
  dp =[0] *(N + 1)
  for i in range(1, N + 1):
    if i % 2 == 0: dp[i] = min(dp[i - 1] + insrt, dp[i // 2] + cpy)
    else: dp[i] = min(dp[i - 1] + insrt, dp[(i + 1)// 2] + cpy + remov)
  return dp[N]
"-----------------"
test()
