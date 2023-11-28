
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2, [[0, 0, 0, 0], [0, 1, 1, 1]], [[0, 0], [0, 1]]]
    # output: 1
    # EXPLANATION:   The different colors represent different artifacts. Excavated cells are labeled with a 'D' in the grid. There is 1 artifact that can be extracted, namely the red artifact. The blue artifact has one part in cell (1,1) which remains uncovered, so we cannot extract it. Thus, we return 1.
    ,
    # example 2
    [2, [[0, 0, 0, 0], [0, 1, 1, 1]], [[0, 0], [0, 1], [1, 1]]]
    # output: 2
    # EXPLANATION:  Both the red and blue artifacts have all parts uncovered (labeled with a 'D') and can be extracted, so we return 2.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### digArtifacts 
from typing import *
def f_gold(n: int, artifacts: List[List[int]], dig: List[List[int]]
) -> int:
    def check(artifact):
        r1, c1, r2, c2 = artifact
        for x in range(r1, r2 + 1):
            for y in range(c1, c2 + 1):
                if (x, y) not in s:
                    return False
        return True
    s = {(i, j) for i, j in dig}
    return sum(check(v) for v in artifacts)
"-----------------"
test()

