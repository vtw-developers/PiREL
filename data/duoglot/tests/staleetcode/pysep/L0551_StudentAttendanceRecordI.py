### checkRecord 
from typing import *
def f_gold(s: str) -> bool:
    return s.count('A') <= 1 and 'LLL' not in s