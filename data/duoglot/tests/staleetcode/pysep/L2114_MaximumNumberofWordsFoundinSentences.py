### mostWordsFound 
from typing import *
def f_gold(sentences: List[str]) -> int:
    return 1 + max(s.count(' ') for s in sentences)