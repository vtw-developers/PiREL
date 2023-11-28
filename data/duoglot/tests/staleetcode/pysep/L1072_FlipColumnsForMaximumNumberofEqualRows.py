### maxEqualRowsAfterFlips 
from collections import Counter
from typing import *
def f_gold(matrix: List[List[int]]) -> int:
    cnt = Counter()
    for row in matrix:
        t = []
        for v in row:
            if row[0] == 1:
                v ^= 1
            t.append(str(v))
        s = ''.join(t)
        cnt[s] += 1
    return max(cnt.values())