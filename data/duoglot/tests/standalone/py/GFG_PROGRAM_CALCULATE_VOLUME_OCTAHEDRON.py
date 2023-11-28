def test():
  "--- test function ---"
  param =[(3355.322051344013,),(- 891.0551553192736,),(8242.699647177868,),(- 9259.146104439229,),(7712.806145993083,),(- 4998.858862079315,),(9771.127582524628,),(- 5415.8106399098115,),(670.0774772280249,),(- 7068.634369272122,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
import math ;
def f_gold(side): return((side * side * side)*(math.sqrt(2)/ 3))
"-----------------"
test()
