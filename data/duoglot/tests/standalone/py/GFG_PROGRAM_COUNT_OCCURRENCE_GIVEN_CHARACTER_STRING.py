def test():
  "--- test function ---"
  param =[('mhjnKfd', 'l',),('716662107', '6',),('01', '1',),('wPHSxIbnHakGRO', 'n',),('721106', '8',),('111', '0',),('TIBFU', 'Q',),('0', '3',),('10', '0',),('lqq', 'd',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(s, c):
  res = 0
  for i in range(len(s)):
    if(s[i] == c): res = res + 1
  return res
"-----------------"
test()
