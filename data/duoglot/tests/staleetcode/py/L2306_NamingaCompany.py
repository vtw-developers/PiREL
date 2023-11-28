
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["coffee", "donuts", "time", "toffee"]]
    # output: 6
    # EXPLANATION:  The following selections are valid: - ("coffee", "donuts"): The company name created is "doffee conuts". - ("donuts", "coffee"): The company name created is "conuts doffee". - ("donuts", "time"): The company name created is "tonuts dime". - ("donuts", "toffee"): The company name created is "tonuts doffee". - ("time", "donuts"): The company name created is "dime tonuts". - ("toffee", "donuts"): The company name created is "doffee tonuts". Therefore, there are a total of 6 distinct company names.  The following are some examples of invalid selections: - ("coffee", "time"): The name "toffee" formed after swapping already exists in the original array. - ("time", "toffee"): Both names are still the same after swapping and exist in the original array. - ("coffee", "toffee"): Both names formed after swapping already exist in the original array.
    ,
    # example 2
    [["lack", "back"]]
    # output: 0
    # EXPLANATION:  There are no valid selections. Therefore, 0 is returned.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### distinctNames 
from typing import *
def f_gold(ideas: List[str]) -> int:
    s = set(ideas)
    f = [[0] * 26 for _ in range(26)]
    for v in ideas:
        i = ord(v[0]) - ord('a')
        t = list(v)
        for j in range(26):
            t[0] = chr(ord('a') + j)
            if ''.join(t) not in s:
                f[i][j] += 1
    ans = 0
    for v in ideas:
        i = ord(v[0]) - ord('a')
        t = list(v)
        for j in range(26):
            t[0] = chr(ord('a') + j)
            if ''.join(t) not in s:
                ans += f[j][i]
    return ans
"-----------------"
test()

