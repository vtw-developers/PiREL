
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 2, 3, 1]]
    # output: 2
    # EXPLANATION:   The input array has a degree of 2 because both elements 1 and 2 appear twice. Of the subarrays that have the same degree: [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2] The shortest length is 2. So return 2.
    ,
    # example 2
    [[1, 2, 2, 3, 1, 4, 2]]
    # output: 6
    # EXPLANATION:   The degree is 3 because the element 2 is repeated 3 times. So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findShortestSubArray 
from typing import *
def f_gold(nums: List[int]) -> int:
    mapper = {}
    for i, v in enumerate(nums):
        if v in mapper:
            arr = mapper[v]
            arr[0] += 1
            arr[2] = i
        else:
            arr = [1, i, i]
            mapper[v] = arr
    max_degree = min_len = 0
    for arr in mapper.values():
        if max_degree < arr[0]:
            max_degree = arr[0]
            min_len = arr[2] - arr[1] + 1
        elif max_degree == arr[0]:
            min_len = min(min_len, arr[2] - arr[1] + 1)
    return min_len
"-----------------"
test()

