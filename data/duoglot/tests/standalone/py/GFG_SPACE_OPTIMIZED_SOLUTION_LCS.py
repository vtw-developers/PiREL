def test():
  "--- test function ---"
  param =[('YNpjSv', 'qtUkJn',),('736519', '07592',),('11010000100010', '0',),('v ', 'qGBQT',),('8311172', '157219329531',),('100011101011', '1000001111',),('u', 'YzkubTqLhP',),('3943042', '3859',),('101', '00010000101010',),('MpbfF OsizevaM', 'WgsFGaQwtp',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(X, Y):
  m = len(X)
  n = len(Y)
  L =[[0 for i in range(n + 1)] for j in range(2)]
  bi = bool
  for i in range(m):
    bi = i & 1
    for j in range(n + 1):
      if(i == 0 or j == 0): L[bi][j] = 0
      elif(X[i] == Y[j - 1]): L[bi][j] = L[1 - bi][j - 1] + 1
      else: L[bi][j] = max(L[1 - bi][j], L[bi][j - 1])
  return L[bi][n]
"-----------------"
test()
