def test():
  "--- test function ---"
  param =[('qnQxjoRx',),('27473733400077',),('000010111111',),('TNVwgrWSLu',),('9537',),('1100',),('lYcoiQfzN',),('52',),('00100001100',),('Rkxe',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(str):
  n = len(str)
  dp =[[0 for i in range(n + 1)] for j in range(n + 1)]
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      if(str[i - 1] == str[j - 1] and i != j): dp[i][j] = 1 + dp[i - 1][j - 1]
      else: dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
  res = ''
  i = n
  j = n
  while(i > 0 and j > 0):
    if(dp[i][j] == dp[i - 1][j - 1] + 1):
      res += str[i - 1]
      i -= 1
      j -= 1
    elif(dp[i][j] == dp[i - 1][j]): i -= 1
    else: j -= 1
  res = ''.join(reversed(res))
  return res
"-----------------"
test()
