def test():
  "--- test function ---"
  param =[('K',),('850076',),('00111',),('X',),('1',),('10010001100',),(' pgPeLz',),('53212456821275',),('101',),('V',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(num):
  series =[1, 3, 2, - 1, - 3, - 2] ;
  series_index = 0 ;
  result = 0 ;
  for i in range((len(num)- 1), - 1, - 1): digit = ord(num[i])- 48 ; result += digit * series[series_index] ; series_index =(series_index + 1)% 6 ; result %= 7 ;
  if(result < 0): result =(result + 7)% 7 ;
  return result ;
"-----------------"
test()
