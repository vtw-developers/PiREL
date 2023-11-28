def test():
  "--- test function ---"
  param =[('LPWsaI', 41,),('9037515104', 72,),('00100010010111', 95,),('SbwipuE', 27,),('574314109', 5,),('1101', 70,),('f', 91,),('068', 50,),('000011001', 38,),('BWbUtIkC', 79,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(s, n):
  s1 = s
  for i in range(1, n): s += s1
  return s
"-----------------"
test()
