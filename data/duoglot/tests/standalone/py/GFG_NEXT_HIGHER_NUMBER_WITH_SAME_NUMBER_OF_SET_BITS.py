def test():
  "--- test function ---"
  param =[(42,),(75,),(94,),(5,),(52,),(22,),(77,),(44,),(85,),(59,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(x):
  next = 0
  if(x):
    rightOne = x & -(x)
    nextHigherOneBit = x + int(rightOne)
    rightOnesPattern = x ^ int(nextHigherOneBit)
    rightOnesPattern =(int(rightOnesPattern)/ int(rightOne))
    rightOnesPattern = int(rightOnesPattern)>> 2
    next = nextHigherOneBit | rightOnesPattern
  return next
"-----------------"
test()
