def test():
  "--- test function ---"
  param =[('LZIKA',),('0556979952',),('110010',),('kGaYfd',),('413567670657',),('01001',),('EQPuFa',),('48848378',),('110',),('PLehNeP',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(s):
  result = 0 ;
  n = len(s);
  for i in range(n):
    for j in range(i, n):
      if(s[i] == s[j]): result = result + 1
  return result
"-----------------"
test()
