### findCenter 
from typing import *
def f_gold(edges: List[List[int]]) -> int:
    return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]