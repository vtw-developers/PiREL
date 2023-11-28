def test():
  "--- test function ---"
  param =[('fZOKCdZ Lav', 'fKA',),('2', '187012',),('1000001110', '0',),('IAOyBzgIWHo', 'oA',),('211806', '10',),('1', '001011100',),('CVaQTG', 'CT',),('6265187228', '628',),('10111101101000', '01111',),('vEi', 'bigsvkQG',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(a, b):
  m = len(a)
  n = len(b)
  lookup =[[0] *(n + 1)for i in range(m + 1)]
  for i in range(n + 1): lookup[0][i] = 0
  for i in range(m + 1): lookup[i][0] = 1
  for i in range(1, m + 1):
    for j in range(1, n + 1):
      if a[i - 1] == b[j - 1]: lookup[i][j] = lookup[i - 1][j - 1] + lookup[i - 1][j]
      else: lookup[i][j] = lookup[i - 1][j]
  return lookup[m][n]
"-----------------"
test()
