def test():
  "--- test function ---"
  param =[('geeekk',),('3786868',),('110',),('aaaabbcbbb',),('11',),('011101',),('WoHNyJYLC',),('3141711779',),('10111101101',),('aabbabababcc',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(str):
  n = len(str)
  count = 0
  res = str[0]
  cur_count = 1
  for i in range(n):
    if(i < n - 1 and str[i] == str[i + 1]): cur_count += 1
    else:
      if cur_count > count:
        count = cur_count
        res = str[i]
      cur_count = 1
  return res
"-----------------"
test()
