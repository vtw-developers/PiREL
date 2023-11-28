def test():
  "--- test function ---"
  param =[(73,),(28,),(33,),(23,),(84,),(31,),(48,),(46,),(45,),(90,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(N):
  dp =[0 for i in range(N)]
  dp[0] = 1
  dp[1] = 2
  i = 1
  while dp[i] <= N:
    i = i + 1
    dp[i] = dp[i - 1] + dp[i - 2]
  return(i - 1)
"-----------------"
test()
