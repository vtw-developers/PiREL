### squareIsWhite 
from typing import *
def f_gold(coordinates: str) -> bool:
    x = ord(coordinates[0]) - ord('a') + 1
    y = int(coordinates[1])
    return ((x + y) & 1) == 1