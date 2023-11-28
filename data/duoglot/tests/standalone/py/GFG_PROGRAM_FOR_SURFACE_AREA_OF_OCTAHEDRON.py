def test():
  "--- test function ---"
  param =[(1449.255716877097,),(- 8772.104874265995,),(2948.419328234334,),(- 1184.220109553511,),(7422.825800698956,),(- 5808.280006171851,),(829.8963781665169,),(- 7368.438572511732,),(5572.033890611617,),(- 3998.9441642787706,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
import math ;
def f_gold(side): return(2 *(math.sqrt(3))*(side * side))
"-----------------"
test()
