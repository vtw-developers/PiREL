
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["132", [9, 8, 5, 0, 3, 6, 4, 2, 6, 8]]
    # output: "<u>8</u>32"
    # EXPLANATION:  Replace the substring "1": - 1 maps to change[1] = 8. Thus, "<u>1</u>32" becomes "<u>8</u>32". "832" is the largest number that can be created, so return it.
    ,
    # example 2
    ["021", [9, 4, 3, 5, 7, 2, 1, 9, 0, 6]]
    # output: "<u>934</u>"
    # EXPLANATION:  Replace the substring "021": - 0 maps to change[0] = 9. - 2 maps to change[2] = 3. - 1 maps to change[1] = 4. Thus, "<u>021</u>" becomes "<u>934</u>". "934" is the largest number that can be created, so return it.
    ,
    # example 3
    ["5", [1, 4, 7, 5, 3, 2, 5, 6, 9, 4]]
    # output: "5"
    # EXPLANATION:  "5" is already the largest number that can be created, so return it.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maximumNumber 
from typing import *
def f_gold(num: str, change: List[int]) -> str:
    find = False
    nums = list(num)
    for i, c in enumerate(num):
        if int(c) < change[int(c)]:
            nums[i] = str(change[int(c)])
            find = True
        elif find and int(c) == change[int(c)]:
            continue
        elif find:
            break
    return ''.join(nums)
"-----------------"
test()

