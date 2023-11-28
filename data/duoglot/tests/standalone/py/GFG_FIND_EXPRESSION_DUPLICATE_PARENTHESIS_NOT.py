def test():
  "--- test function ---"
  param =[("((a+b)+((c+d)))",),("(((a+(b)))+(c+d))",),("(((a+(b))+c+d))",),("((a+b)+(c+d))",),("(8582007)",),("((a+(b))+(c+d))",),("(PylsShEdKAE)",),('886980680541',),('001',),('jsVmFeOq',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(string):
  Stack =[]
  for ch in string:
    if ch == ')':
      top = Stack.pop()
      elementsInside = 0
      while top != '(':
        elementsInside += 1
        top = Stack.pop()
      if elementsInside < 1: return True
    else: Stack.append(ch)
  return False
"-----------------"
test()
