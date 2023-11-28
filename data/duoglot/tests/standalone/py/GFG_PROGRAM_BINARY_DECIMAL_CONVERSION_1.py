def test():
  "--- test function ---"
  param =[('uEmIAgF',),('753310137',),('010011010',),('kNi',),('04562016903312',),('000111101',),('bk',),('9',),('1',),('XxT nXLlk',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  num = n ;
  dec_value = 0 ;
  base1 = 1 ;
  len1 = len(num);
  for i in range(len1 - 1, - 1, - 1):
    if(num[i] == '1'): dec_value += base1 ;
    base1 = base1 * 2 ;
  return dec_value ;
"-----------------"
test()
