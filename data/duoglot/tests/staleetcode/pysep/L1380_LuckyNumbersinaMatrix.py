### luckyNumbers 
from typing import *
def f_gold(matrix: List[List[int]]) -> List[int]:
    rows = {min(row) for row in matrix}
    cols = {max(col) for col in zip(*matrix)}
    return list(rows & cols)