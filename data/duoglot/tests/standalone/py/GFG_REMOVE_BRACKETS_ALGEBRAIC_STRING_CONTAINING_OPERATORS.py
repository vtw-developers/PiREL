def test():
  "--- test function ---"
  param =[('ggbsMvMZcMOVd',),('384292670',),('10000100',),('fdHME',),('09198832',),('0011111011',),('SnXwRS',),('071',),('01101',),('xwmqxgBa',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(Str):
  Len = len(Str)
  res =[None] * Len
  index = 0
  i = 0
  s =[]
  s.append(0)
  while(i < Len):
    if(Str[i] == '+'):
      if(s[- 1] == 1):
        res[index] = '-'
        index += 1
      if(s[- 1] == 0):
        res[index] = '+'
        index += 1
    elif(Str[i] == '-'):
      if(s[- 1] == 1):
        res[index] = '+'
        index += 1
      elif(s[- 1] == 0):
        res[index] = '-'
        index += 1
    elif(Str[i] == '(' and i > 0):
      if(Str[i - 1] == '-'):
        x = 0 if(s[- 1] == 1)else 1
        s.append(x)
      elif(Str[i - 1] == '+'): s.append(s[- 1])
    elif(Str[i] == ')'): s.pop()
    else:
      res[index] = Str[i]
      index += 1
    i += 1
  return res
"-----------------"
test()
