def test():
  "--- test function ---"
  param =[(18,),(66,),(73,),(70,),(26,),(41,),(20,),(25,),(52,),(13,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  dp =[[0 for x in range(10)] for y in range(n + 1)] ;
  if(n == 1): return 10 ;
  for j in range(10): dp[1][j] = 1 ;
  for i in range(2, n + 1):
    for j in range(10):
      if(j == 0): dp[i][j] = dp[i - 1][j + 1] ;
      elif(j == 9): dp[i][j] = dp[i - 1][j - 1] ;
      else: dp[i][j] =(dp[i - 1][j - 1] + dp[i - 1][j + 1]);
  sum = 0 ;
  for j in range(1, 10): sum = sum + dp[n][j] ;
  return sum ;
"-----------------"
test()
