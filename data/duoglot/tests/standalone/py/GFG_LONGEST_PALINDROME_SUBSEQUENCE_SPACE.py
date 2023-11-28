def test():
  "--- test function ---"
  param =[(' E',),('0845591950',),('00101011',),('pLSvlwrACvFaoT',),('7246',),('1010101100000',),('obPkcLSFp',),('914757557818',),('1',),('PKvUWIQ',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(s):
  n = len(s)
  a =[0] * n
  for i in range(n - 1, - 1, - 1):
    back_up = 0
    for j in range(i, n):
      if j == i: a[j] = 1
      elif s[i] == s[j]:
        temp = a[j]
        a[j] = back_up + 2
        back_up = temp
      else:
        back_up = a[j]
        a[j] = max(a[j - 1], a[j])
  return a[n - 1]
"-----------------"
test()
