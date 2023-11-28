def test():
  "--- test function ---"
  param =[('lSUhEvxcgfI',),('77329283',),('010111111',),('Stazb',),('0702',),('01111111',),('a',),('359118754930',),('11011010010',),('rznb',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  res = n
  for j in range(len(n)- 1, - 1, - 1): res += n[j]
  return res
"-----------------"
test()
