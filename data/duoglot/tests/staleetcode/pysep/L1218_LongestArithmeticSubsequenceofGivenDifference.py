### longestSubsequence 
from collections import defaultdict
from typing import *
def f_gold(arr: List[int], difference: int) -> int:
    dp, ans = defaultdict(int), 1
    for num in arr:
        dp[num] = dp[num - difference] + 1
        ans = max(ans, dp[num])
    return ans