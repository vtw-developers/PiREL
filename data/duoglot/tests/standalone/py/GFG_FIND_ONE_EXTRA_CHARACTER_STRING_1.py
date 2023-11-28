def test():
  "--- test function ---"
  param =[('obfLA mmMYvghH', 'obfLA  mmMYvghH',),('2941', '2941',),('0111111', '0111111',),('oWvbFstI', 'oWvbFstI',),('4937516500', '4937516500',),('101110100', '101110100',),('hYZscJQFBE', 'hYZscJQFBE',),('58443', '58443',),('1100', '1100',),('ZUdYuIBVNaeeb', 'ZUdYuIBVNaeeb',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(strA, strB):
  res = 0
  for i in range(0, len(strA)): res = res ^(ord)(strA[i])
  for i in range(0, len(strB)): res = res ^(ord)(strB[i])
  return((chr)(res));
"-----------------"
test()
