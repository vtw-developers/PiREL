def test():
  "--- test function ---"
  param =[('DXh',),('48703586411816',),('0001',),('yWg WvjNKS',),('8408568459',),('01',),('DFECZ CWtN',),('37742236',),('001101',),('LDxERLmYn',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(num1):
  l = len(num1);
  num = list(num1);
  i = l - 1 ;
  while(i >= 0):
    if(num[i] == '0'): num[i] = '1' ; break ;
    else: num[i] = '0' ;
    i -= 1 ;
  num1 = ''.join(num);
  if(i < 0): num1 = '1' + num1 ;
  return num1 ;
"-----------------"
test()
