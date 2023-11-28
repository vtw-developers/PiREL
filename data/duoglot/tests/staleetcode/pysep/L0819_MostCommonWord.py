### mostCommonWord 
import re
from collections import Counter
from typing import *
def f_gold(paragraph: str, banned: List[str]) -> str:
    s = set(banned)
    p = Counter(re.findall('[a-z]+', paragraph.lower()))
    return next(word for word, _ in p.most_common() if word not in s)