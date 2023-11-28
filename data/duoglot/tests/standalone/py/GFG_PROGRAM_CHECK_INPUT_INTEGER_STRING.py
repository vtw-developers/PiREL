def test():
  "--- test function ---"
  param =[('MgTOyHo NT',),('033675175',),('011001',),('XLlccG',),('8223900094410',),('000',),('aupp',),('90202721499',),('110000100011',),('MhYHsMQeLhG',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(s):
  for i in range(len(s)):
    if s[i].isdigit()!= True: return False
  return True
"-----------------"
test()
