def test():
  "--- test function ---"
  param =[('gILrzLimS', 'm',),('307471222', '2',),('110', '0',),('GcAB', 'v',),('113', '3',),('011110010', '0',),('wcwob', 'w',),('74571582216153', '1',),('100000011', '0',),('ryPErkzY', 'q',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(s, c):
  oneSeen = False
  i = 0
  n = len(s)
  while(i < n):
    if(s[i] == c):
      if(oneSeen == True): return False
      while(i < n and s[i] == c): i = i + 1
      oneSeen = True
    else: i = i + 1
  return True
"-----------------"
test()
