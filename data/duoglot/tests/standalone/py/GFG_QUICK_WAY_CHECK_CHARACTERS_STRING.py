def test():
  "--- test function ---"
  param =[('',),('ggg',),('11',),('KoYIHns',),('232',),('10111000011101',),('DDDD',),('11',),('11111',),('ewJvixQzu',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(s):
  n = len(s)
  for i in range(1, n):
    if s[i] != s[0]: return False
  return True
"-----------------"
test()
