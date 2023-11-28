def test():
  "--- test function ---"
  param =[('KfcTJNP',),('05312505872',),('100111',),('tDEEhKxrQ',),('50824233019',),('10001110010',),('T SEZaNm MYQ',),('838415739',),('01110100',),('WYQiAey H',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(str):
  one_count = 0
  zero_count = 0
  n = len(str)
  for i in range(0, n, 1):
    if(str[i] == '1'): one_count += 1
    else: zero_count += 1
  if(one_count % 2 == 0): return zero_count
  return one_count
"-----------------"
test()
