
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3, [[0, 1]], [[0, 2], [2, 1]]]
    # output: [true,false]
    # EXPLANATION: Request 0: Person 0 and person 2 can be friends, so they become direct friends.  Request 1: Person 2 and person 1 cannot be friends since person 0 and person 1 would be indirect friends (1--2--0).
    ,
    # example 2
    [3, [[0, 1]], [[1, 2], [0, 2]]]
    # output: [true,false]
    # EXPLANATION: Request 0: Person 1 and person 2 can be friends, so they become direct friends. Request 1: Person 0 and person 2 cannot be friends since person 0 and person 1 would be indirect friends (0--2--1).
    ,
    # example 3
    [5, [[0, 1], [1, 2], [2, 3]], [[0, 4], [1, 2], [3, 1], [3, 4]]]
    # output: [true,false,true,false]
    # EXPLANATION: Request 0: Person 0 and person 4 can be friends, so they become direct friends. Request 1: Person 1 and person 2 cannot be friends since they are directly restricted. Request 2: Person 3 and person 1 can be friends, so they become direct friends. Request 3: Person 3 and person 4 cannot be friends since person 0 and person 1 would be indirect friends (0--4--3--1).
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### friendRequests 
from typing import *
def f_gold(n: int, restrictions: List[List[int]], requests: List[List[int]]
) -> List[bool]:
    p = list(range(n))
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    ans = []
    i = 0
    for u, v in requests:
        if find(u) == find(v):
            ans.append(True)
        else:
            valid = True
            for x, y in restrictions:
                if (find(u) == find(x) and find(v) == find(y)) or (
                    find(u) == find(y) and find(v) == find(x)
                ):
                    valid = False
                    break
            ans.append(valid)
            if valid:
                p[find(u)] = find(v)
    return ans
"-----------------"
test()

