def test():
  "--- test function ---"
  param =[(' EgvQCeqYpZtv',),('488540',),('0000101010111',),('syw',),('402355',),('0',),('wmHMlAtq',),('7962',),('111111',),('UbgRGDquop',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(s):
  l = len(s)
  s1 = ""
  if(l % 2 == 0): isEven = True
  else: isEven = False
  for i in range(0, l, 2):
    if(isEven):
      s1 = s[i] + s1
      s1 += s[i + 1]
    else:
      if(l - i > 1):
        s1 += s[i]
        s1 = s[i + 1] + s1
      else: s1 += s[i]
  return s1
"-----------------"
test()
