from functools import cmp_to_key
### largestNumber 
from typing import *
def f_gold(nums: List[int]) -> str:
    num_list = list(map(str, nums))
    num_list.sort(key=cmp_to_key(lambda x, y: int(y + x) - int(x + y)))
    return '0' if num_list[0] == '0' else ''.join(num_list)