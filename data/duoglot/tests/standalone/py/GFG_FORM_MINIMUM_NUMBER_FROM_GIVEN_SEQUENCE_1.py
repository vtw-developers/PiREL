def test():
  "--- test function ---"
  param =[('D',),('I',),('DD',),('II',),('DIDI',),('IIDDD',),('DDIDDIID',),('176297',),('1',),('XHkhZq',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(seq):
  n = len(seq)
  if(n >= 9): return "-1"
  result =[None] *(n + 1)
  count = 1
  for i in range(n + 1):
    if(i == n or seq[i] == 'I'):
      for j in range(i - 1, - 2, - 1):
        result[j + 1] = int('0' + str(count))
        count += 1
        if(j >= 0 and seq[j] == 'I'): break
  return result
"-----------------"
test()
