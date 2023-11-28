def test():
  "--- test function ---"
  param =[('LsvbpcviVPwq', 15,),('35225904', 2,),('010010', 36,),('QnYd', 44,),('2571694', 11,),('101101011010', 94,),('jb', 22,),('928874', 83,),('11', 93,),('FbvbkMb', 37,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(text, s):
  result = ""
  for i in range(len(text)):
    char = text[i]
    if(char.isupper()): result += chr((ord(char)+ s - 65)% 26 + 65)
    else: result += chr((ord(char)+ s - 97)% 26 + 97)
  return result
"-----------------"
test()
