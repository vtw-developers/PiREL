def test():
  "--- test function ---"
  param =[(75,),(50,),(93,),(87,),(35,),(25,),(43,),(61,),(54,),(91,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(h):
  MOD = 1000000007
  dp =[0 for i in range(h + 1)]
  dp[0] = 1
  dp[1] = 1
  for i in range(2, h + 1): dp[i] =(dp[i - 1] *((2 * dp[i - 2])% MOD + dp[i - 1])% MOD)% MOD
  return dp[h]
"-----------------"
test()
