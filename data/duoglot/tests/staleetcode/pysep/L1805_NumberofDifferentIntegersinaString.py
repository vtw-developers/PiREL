import re
### numDifferentIntegers 
import re
from typing import *
def f_gold(word: str) -> int:
    nums = re.split(r'[a-z]+', word)
    return len({int(num) for num in nums if num != ''})