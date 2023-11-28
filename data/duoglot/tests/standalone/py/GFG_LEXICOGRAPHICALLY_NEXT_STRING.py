def test():
  "--- test function ---"
  param =[('amKIRzPiqLTIy',),('68',),('100',),('f',),('802205375',),('0111',),('GRjRYIvYwgua',),('8139910006809',),('100101',),('rw',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(s):
  if(s == " "): return "a"
  i = len(s)- 1
  while(s[i] == 'z' and i >= 0): i -= 1
  if(i == - 1): s = s + 'a'
  else: s = s.replace(s[i], chr(ord(s[i])+ 1), 1)
  return s
"-----------------"
test()
