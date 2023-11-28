### defangIPaddr 
from typing import *
def f_gold(address: str) -> str:
    return address.replace('.', '[.]')