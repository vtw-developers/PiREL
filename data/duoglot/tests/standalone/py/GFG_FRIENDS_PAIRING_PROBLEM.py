def test():
  "--- test function ---"
  param =[(99,),(62,),(87,),(87,),(61,),(88,),(73,),(62,),(98,),(57,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  dp =[0 for i in range(n + 1)]
  for i in range(n + 1):
    if(i <= 2): dp[i] = i
    else: dp[i] = dp[i - 1] +(i - 1)* dp[i - 2]
  return dp[n]
"-----------------"
test()
