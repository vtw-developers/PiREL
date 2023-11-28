def test():
  "--- test function ---"
  param =[('1001ab010abc01001',),('1001010001',),('010100010100',),('DLCu',),('7072430592',),('011',),('pnJpypYOza',),('1037',),('111',),('HxK',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(s):
  length = len(s)
  oneSeen = False
  count = 0
  for i in range(length):
    if(s[i] == '1' and oneSeen):
      if(s[i - 1] == '0'): count += 1
    if(s[i] == '1' and oneSeen == 0): oneSeen = True
    if(s[i] != '0' and s[i] != '1'): oneSeen = False
  return count
"-----------------"
test()
