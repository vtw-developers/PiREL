### groupStrings 
from collections import defaultdict
from typing import *
def f_gold(strings: List[str]) -> List[List[str]]:
    mp = defaultdict(list)
    for s in strings:
        t = []
        diff = ord(s[0]) - ord('a')
        for c in s:
            d = ord(c) - diff
            if d < ord('a'):
                d += 26
            t.append(chr(d))
        k = ''.join(t)
        mp[k].append(s)
    return list(mp.values())