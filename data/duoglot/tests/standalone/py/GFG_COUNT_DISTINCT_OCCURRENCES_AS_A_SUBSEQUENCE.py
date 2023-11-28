def test():
  "--- test function ---"
  param =[('banana', 'ban',),('49597223', '42',),('1000010000011', '010',),('BTlzufK', 'EpsVuzP lf',),('3474007', '370',),('0010', '00000',),('dKHhoTD', 'doT',),('9123259723', '123',),('11001000111110', '0',),('iY WJlIZ', 'iI',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(S, T):
  m = len(T)
  n = len(S)
  if m > n: return 0
  mat =[[0 for _ in range(n + 1)] for __ in range(m + 1)]
  for i in range(1, m + 1): mat[i][0] = 0
  for j in range(n + 1): mat[0][j] = 1
  for i in range(1, m + 1):
    for j in range(1, n + 1):
      if T[i - 1] != S[j - 1]: mat[i][j] = mat[i][j - 1]
      else: mat[i][j] =(mat[i][j - 1] + mat[i - 1][j - 1])
  return mat[m][n]
"-----------------"
test()
