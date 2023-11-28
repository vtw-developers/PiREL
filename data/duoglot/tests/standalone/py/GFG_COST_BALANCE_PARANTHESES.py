def test():
  "--- test function ---"
  param =[('()',),('))((',),('())',),('(()',),('(()()())',),('))())(()(())',),('))(())((',),('49',),('00001111',),('KDahByG ',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(s):
  if(len(s)== 0): print(0)
  ans = 0
  o = 0
  c = 0
  for i in range(len(s)):
    if(s[i] == '('): o += 1
    if(s[i] == ')'): c += 1
  if(o != c): return - 1
  a =[0 for i in range(len(s))]
  if(s[0] == '('): a[0] = 1
  else: a[0] = - 1
  if(a[0] < 0): ans += abs(a[0])
  for i in range(1, len(s)):
    if(s[i] == '('): a[i] = a[i - 1] + 1
    else: a[i] = a[i - 1] - 1
    if(a[i] < 0): ans += abs(a[i])
  return ans
"-----------------"
test()
