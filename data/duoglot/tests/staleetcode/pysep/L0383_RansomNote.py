### canConstruct 
from collections import Counter
from typing import *
def f_gold(ransomNote: str, magazine: str) -> bool:
    counter = Counter(magazine)
    for c in ransomNote:
        if counter[c] <= 0:
            return False
        counter[c] -= 1
    return True