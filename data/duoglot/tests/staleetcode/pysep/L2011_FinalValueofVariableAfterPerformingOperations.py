### finalValueAfterOperations 
from typing import *
def f_gold(operations: List[str]) -> int:
    return sum(1 if s[1] == '+' else -1 for s in operations)