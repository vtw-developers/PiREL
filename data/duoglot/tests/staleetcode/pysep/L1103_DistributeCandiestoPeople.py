### distributeCandies 
from typing import *
def f_gold(candies: int, num_people: int) -> List[int]:
    ans = [0] * num_people
    i = 0
    while candies > 0:
        ans[i % num_people] += min(candies, i + 1)
        candies -= min(candies, i + 1)
        i += 1
    return ans