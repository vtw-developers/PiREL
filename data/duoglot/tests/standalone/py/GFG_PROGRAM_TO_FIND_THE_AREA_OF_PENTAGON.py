def test():
  "--- test function ---"
  param =[(2009.019461888707,),(- 1480.5131394215787,),(357.7870347569567,),(- 8040.293697508038,),(3821.882657293133,),(- 6840.635072240347,),(1623.036598830132,),(- 9714.00706195298,),(3916.454769669618,),(- 669.068424712943,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
from math import sqrt ;
def f_gold(a):
  area =(sqrt(5 *(5 + 2 *(sqrt(5))))* a * a)/ 4
  return area
"-----------------"
test()
