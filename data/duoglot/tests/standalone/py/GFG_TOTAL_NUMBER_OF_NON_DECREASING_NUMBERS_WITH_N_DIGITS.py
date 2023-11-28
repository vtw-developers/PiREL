def test():
  "--- test function ---"
  param =[(21,),(40,),(83,),(93,),(43,),(98,),(35,),(86,),(76,),(88,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  dp =[[0 for i in range(n + 1)] for i in range(10)]
  for i in range(10): dp[i][1] = 1
  for digit in range(10):
    for len in range(2, n + 1):
      for x in range(digit + 1): dp[digit][len] += dp[x][len - 1]
  count = 0
  for i in range(10): count += dp[i][n]
  return count
"-----------------"
test()
