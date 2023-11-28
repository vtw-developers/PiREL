def test():
  "--- test function ---"
  param =[('smnKL',),('270083',),('0',),('kcZdsz',),('483544224',),('000011',),('WysGCirMwKBzP',),('3366',),('110',),('NlaMkpCjUgg',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(str1):
  result = 0 ;
  n = len(str1)
  for i in range(0, n):
    for j in range(i + 1, n):
      if(abs(ord(str1[i])- ord(str1[j]))== abs(i - j)): result += 1 ;
  return result ;
"-----------------"
test()
