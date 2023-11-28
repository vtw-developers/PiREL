def test():
  "--- test function ---"
  param =[('ab',),('303',),('11110000',),('aba',),('404',),('10101',),('abab',),('6366',),('001',),('',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(str):
  i = 0 ;
  j = len(str)- 1 ;
  while(i < j):
    if(str[i] != str[j]): return False ;
    i += 1 ;
    j -= 1 ;
  return True ;
"-----------------"
test()
