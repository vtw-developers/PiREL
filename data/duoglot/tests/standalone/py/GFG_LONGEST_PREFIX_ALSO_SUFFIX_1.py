def test():
  "--- test function ---"
  param =[('aabcdaabc',),('1372494598',),('110000100001',),('abcab',),('488938',),('011010101011',),('aaaa',),('3356203205',),('1010',),('kkXiiTZkGeh',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(s):
  n = len(s)
  lps =[0] * n
  l = 0
  i = 1
  while(i < n):
    if(s[i] == s[l]):
      l = l + 1
      lps[i] = l
      i = i + 1
    else:
      if(l != 0): l = lps[l - 1]
      else:
        lps[i] = 0
        i = i + 1
  res = lps[n - 1]
  if(res > n / 2): return n // 2
  else: return res
"-----------------"
test()
