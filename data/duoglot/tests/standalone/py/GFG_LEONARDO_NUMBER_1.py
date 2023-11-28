def test():
  "--- test function ---"
  param =[(75,),(76,),(55,),(14,),(43,),(10,),(16,),(30,),(44,),(65,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  dp =[] ;
  dp.append(1);
  dp.append(1);
  for i in range(2, n + 1): dp.append(dp[i - 1] + dp[i - 2] + 1);
  return dp[n] ;
"-----------------"
test()
