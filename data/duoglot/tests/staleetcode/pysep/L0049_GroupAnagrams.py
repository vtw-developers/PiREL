### groupAnagrams 
from collections import defaultdict
from typing import *
def f_gold(strs: List[str]) -> List[List[str]]:
    chars = defaultdict(list)
    for s in strs:
        k = ''.join(sorted(list(s)))
        chars[k].append(s)
    return list(chars.values())