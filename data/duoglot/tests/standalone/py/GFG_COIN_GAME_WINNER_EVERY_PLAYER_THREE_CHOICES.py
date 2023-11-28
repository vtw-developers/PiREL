def test():
  "--- test function ---"
  param =[(6, 27, 51,),(32, 88, 69,),(99, 18, 48,),(22, 1, 74,),(26, 78, 95,),(67, 51, 27,),(69, 57, 91,),(39, 8, 9,),(7, 82, 41,),(91, 56, 7,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(x, y, n):
  dp =[0 for i in range(n + 1)]
  dp[0] = False
  dp[1] = True
  for i in range(2, n + 1):
    if(i - 1 >= 0 and not dp[i - 1]): dp[i] = True
    elif(i - x >= 0 and not dp[i - x]): dp[i] = True
    elif(i - y >= 0 and not dp[i - y]): dp[i] = True
    else: dp[i] = False
  return dp[n]
"-----------------"
test()
