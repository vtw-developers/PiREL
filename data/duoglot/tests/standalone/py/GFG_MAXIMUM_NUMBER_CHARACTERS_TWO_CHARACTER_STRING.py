def test():
  "--- test function ---"
  param =[('cI',),('76478',),('1',),('tr',),('10',),('01',),('Rmhzp',),('5784080133917',),('1100',),('OK',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(str):
  n = len(str)
  res = - 1
  for i in range(0, n - 1):
    for j in range(i + 1, n):
      if(str[i] == str[j]): res = max(res, abs(j - i - 1))
  return res
"-----------------"
test()
