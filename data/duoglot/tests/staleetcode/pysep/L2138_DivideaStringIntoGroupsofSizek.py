### divideString 
from typing import *
def f_gold(s: str, k: int, fill: str) -> List[str]:
    return [s[i : i + k].ljust(k, fill) for i in range(0, len(s), k)]