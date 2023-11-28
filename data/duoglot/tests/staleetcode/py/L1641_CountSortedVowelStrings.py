
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1]
    # output: 5
    # EXPLANATION:  The 5 sorted strings that consist of vowels only are <code>["a","e","i","o","u"].</code>
    ,
    # example 2
    [2]
    # output: 15
    # EXPLANATION:  The 15 sorted strings that consist of vowels only are ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"]. Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
    ,
    # example 3
    [33]
    # output: 66045
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countVowelStrings 
from typing import *
def f_gold(n: int) -> int:
    cnt = [1] * 5
    for i in range(2, n + 1):
        for j in range(3, -1, -1):
            cnt[j] += cnt[j + 1]
    return sum(cnt)
"-----------------"
test()

