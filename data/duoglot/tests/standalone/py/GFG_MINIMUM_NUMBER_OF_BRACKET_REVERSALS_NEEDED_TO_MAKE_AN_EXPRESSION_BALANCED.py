def test():
  "--- test function ---"
  param =[('}{',),('{{{',),('{{{{',),('{{{{}}',),('}{{}}{{{',),('{}',),('',),('8',),('01111000',),('XPkERzHcpId',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(expr):
  lenn = len(expr)
  if(lenn % 2): return - 1
  s =[]
  for i in range(lenn):
    if(expr[i] == '' and len(s)):
      if(s[0] == ''): s.pop(0)
      else: s.insert(0, expr[i])
    else: s.insert(0, expr[i])
  red_len = len(s)
  n = 0
  while(len(s)and s[0] == ''):
    s.pop(0)
    n += 1
  return(red_len // 2 + n % 2)
"-----------------"
test()
