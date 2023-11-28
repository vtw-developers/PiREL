### findTheLongestSubstring 
import math
from math import inf
from typing import *
def f_gold(s: str) -> int:
    pos = [float('inf')] * 32
    pos[0] = -1
    vowels = 'aeiou'
    state = ans = 0
    for i, c in enumerate(s):
        for j, v in enumerate(vowels):
            if c == v:
                state ^= 1 << j
        ans = max(ans, i - pos[state])
        pos[state] = min(pos[state], i)
    return ans