def test():
  "--- test function ---"
  param =[('JxZFz',),('7648992235770',),('11100000',),('cRN  SgYjPsctJ',),('434',),('1',),('JRfZIAsbrPBZ',),('03779368305592',),('1111000',),('BkULuIi',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(str):
  n = len(str)
  dp =[[0] *(n + 1)] *(n + 1)
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      if(str[i - 1] == str[j - 1] and i != j): dp[i][j] = 1 + dp[i - 1][j - 1]
      else: dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
  return dp[n][n]
"-----------------"
test()
