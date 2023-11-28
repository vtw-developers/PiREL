
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[4, 6, 5, 9, 3, 7], [0, 0, 2], [2, 3, 5]]
    # output: <code>[true,false,true]</code>
    # EXPLANATION:  In the 0<sup>th</sup> query, the subarray is [4,6,5]. This can be rearranged as [6,5,4], which is an arithmetic sequence. In the 1<sup>st</sup> query, the subarray is [4,6,5,9]. This cannot be rearranged as an arithmetic sequence. In the 2<sup>nd</sup> query, the subarray is <code>[5,9,3,7]. This</code> can be rearranged as <code>[3,5,7,9]</code>, which is an arithmetic sequence.
    ,
    # example 2
    [[-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10], [0, 1, 6, 4, 8, 7], [4, 4, 9, 7, 9, 10]]
    # output: [false,true,false,false,true,true]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### checkArithmeticSubarrays 
from typing import *
def f_gold(nums: List[int], l: List[int], r: List[int]
) -> List[bool]:
    def check(nums, l, r):
        if r - l < 2:
            return True
        s = set(nums[l : r + 1])
        mx = max(nums[l : r + 1])
        mi = min(nums[l : r + 1])
        if (mx - mi) % (r - l) != 0:
            return False
        delta = (mx - mi) / (r - l)
        for i in range(1, r - l + 1):
            if (mi + delta * i) not in s:
                return False
        return True
    return [check(nums, l[i], r[i]) for i in range(len(l))]
"-----------------"
test()

