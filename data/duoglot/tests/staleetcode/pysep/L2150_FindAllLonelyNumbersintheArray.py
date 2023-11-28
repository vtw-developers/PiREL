### findLonely 
from collections import Counter
from typing import *
def f_gold(nums: List[int]) -> List[int]:
    counter = Counter(nums)
    ans = []
    for num, cnt in counter.items():
        if cnt == 1 and counter[num - 1] == 0 and counter[num + 1] == 0:
            ans.append(num)
    return ans