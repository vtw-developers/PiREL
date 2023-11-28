def test():
  "--- test function ---"
  param =[(61,),(22,),(65,),(57,),(36,),(25,),(16,),(26,),(92,),(5,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  dp =[0 for _ in range(n + 1)]
  for i in range(1, n + 1):
    if i <= 3: dp[i] = 1
    elif i == 4: dp[i] = 2
    else: dp[i] = dp[i - 1] + dp[i - 4]
  return dp[n]
"-----------------"
test()
