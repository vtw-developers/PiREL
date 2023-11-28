### decode 
from typing import *
def f_gold(encoded: List[int], first: int) -> List[int]:
    ans = [first]
    for e in encoded:
        ans.append(ans[-1] ^ e)
    return ans