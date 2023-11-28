def test():
  "--- test function ---"
  param =[('7',),('305745689',),('444',),('4',),('2074',),('27',),('447',),('255',),('10000111111011',),('fAKcSDRTNz',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  i = 0
  j = len(n)
  pos = 0
  while(i < j):
    if(n[i] == '4'): pos = pos * 2 + 1
    if(n[i] == '7'): pos = pos * 2 + 2
    i = i + 1
  return pos
"-----------------"
test()
