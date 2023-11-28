### mostPoints 
def cache(f): return f
from typing import *
def f_gold(questions: List[List[int]]) -> int:
    @cache
    def dfs(i):
        if i >= len(questions):
            return 0
        return max(questions[i][0] + dfs(i + questions[i][1] + 1), dfs(i + 1))
    return dfs(0)