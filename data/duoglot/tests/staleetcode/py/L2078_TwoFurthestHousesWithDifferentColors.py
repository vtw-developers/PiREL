
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 1, 1, 6, 1, 1, 1]]
    # output: 3
    # EXPLANATION:  In the above image, color 1 is blue, and color 6 is red. The furthest two houses with different colors are house 0 and house 3. House 0 has color 1, and house 3 has color 6. The distance between them is abs(0 - 3) = 3. Note that houses 3 and 6 can also produce the optimal answer.
    ,
    # example 2
    [[1, 8, 3, 8, 3]]
    # output: 4
    # EXPLANATION:  In the above image, color 1 is blue, color 8 is yellow, and color 3 is green. The furthest two houses with different colors are house 0 and house 4. House 0 has color 1, and house 4 has color 3. The distance between them is abs(0 - 4) = 4.
    ,
    # example 3
    [[0, 1]]
    # output: 1
    # EXPLANATION:  The furthest two houses with different colors are house 0 and house 1. House 0 has color 0, and house 1 has color 1. The distance between them is abs(0 - 1) = 1.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxDistance 
from typing import *
def f_gold(colors: List[int]) -> int:
    ans, n = 0, len(colors)
    for i in range(n):
        for j in range(i + 1, n):
            if colors[i] != colors[j]:
                ans = max(ans, abs(i - j))
    return ans
"-----------------"
test()

