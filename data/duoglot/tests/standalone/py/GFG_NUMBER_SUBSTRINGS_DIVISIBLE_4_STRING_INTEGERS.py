def test():
  "--- test function ---"
  param =[('Qaq',),('9400761825850',),('0011001111',),('lasWqrLRq',),('5662',),('110',),(' tOYKf',),('6536991235305',),('11111',),('uZftT iDHcYiCt',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(s):
  n = len(s)
  count = 0 ;
  for i in range(0, n, 1):
    if(s[i] == '4' or s[i] == '8' or s[i] == '0'): count += 1
  for i in range(0, n - 1, 1):
    h =(ord(s[i])- ord('0'))* 10 +(ord(s[i + 1])- ord('0'))
    if(h % 4 == 0): count = count + i + 1
  return count
"-----------------"
test()
