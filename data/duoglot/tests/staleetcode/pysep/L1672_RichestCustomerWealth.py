### maximumWealth 
from typing import *
def f_gold(accounts: List[List[int]]) -> int:
    return max(sum(account) for account in accounts)