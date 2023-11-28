
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3]
    # output: ["1","2","Fizz"]
    ,
    # example 2
    [5]
    # output: ["1","2","Fizz","4","Buzz"]
    ,
    # example 3
    [15]
    # output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### fizzBuzz 
from typing import *
def f_gold(n: int) -> List[str]:
    ans = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            ans.append('FizzBuzz')
        elif i % 3 == 0:
            ans.append('Fizz')
        elif i % 5 == 0:
            ans.append('Buzz')
        else:
            ans.append(str(i))
    return ans
"-----------------"
test()

