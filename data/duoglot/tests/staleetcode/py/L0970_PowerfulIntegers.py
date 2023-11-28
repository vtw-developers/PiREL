
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2, 3, 10]
    # output: [2,3,4,5,7,9,10]
    # EXPLANATION:  2 = 2<sup>0</sup> + 3<sup>0</sup> 3 = 2<sup>1</sup> + 3<sup>0</sup> 4 = 2<sup>0</sup> + 3<sup>1</sup> 5 = 2<sup>1</sup> + 3<sup>1</sup> 7 = 2<sup>2</sup> + 3<sup>1</sup> 9 = 2<sup>3</sup> + 3<sup>0</sup> 10 = 2<sup>0</sup> + 3<sup>2</sup>
    ,
    # example 2
    [3, 5, 15]
    # output: [2,4,6,8,10,14]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### powerfulIntegers 
from typing import *
def f_gold(x: int, y: int, bound: int) -> List[int]:
    s = set()
    i = 1
    while i < bound:
        j = 1
        while j < bound:
            if i + j <= bound:
                s.add(i + j)
            if y == 1:
                break
            j *= y
        if x == 1:
            break
        i *= x
    return list(s)
"-----------------"
test()

