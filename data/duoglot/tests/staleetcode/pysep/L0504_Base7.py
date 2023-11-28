### convertToBase7 
from typing import *
def f_gold(num: int) -> str:
    if num == 0:
        return '0'
    if num < 0:
        return '-' + f_gold(-num)
    ans = []
    while num:
        ans.append(str(num % 7))
        num //= 7
    return ''.join(ans[::-1])