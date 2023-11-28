def test():
  "--- test function ---"
  param =[('TEYndweqZA',),('01865',),('11001100',),('CzwznJmQet',),('318305446',),('0000001111110',),('yzT',),('38630230',),('01101',),('zoizI',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(s):
  n = len(s)
  s1 = ""
  s1 = s1 + s[0].lower()
  i = 1
  while i < n:
    if(s[i] == ' ' and i <= n):
      s1 = s1 + " " +(s[i + 1]).lower()
      i = i + 1
    else: s1 = s1 +(s[i]).upper()
    i = i + 1
  return s1
"-----------------"
test()
