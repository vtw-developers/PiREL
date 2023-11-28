
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4]]
    # output: 6
    # EXPLANATION:  The good subsets are: - [1,2]: product is 2, which is the product of distinct prime 2. - [1,2,3]: product is 6, which is the product of distinct primes 2 and 3. - [1,3]: product is 3, which is the product of distinct prime 3. - [2]: product is 2, which is the product of distinct prime 2. - [2,3]: product is 6, which is the product of distinct primes 2 and 3. - [3]: product is 3, which is the product of distinct prime 3.
    ,
    # example 2
    [[4, 2, 3, 15]]
    # output: 5
    # EXPLANATION:  The good subsets are: - [2]: product is 2, which is the product of distinct prime 2. - [2,3]: product is 6, which is the product of distinct primes 2 and 3. - [2,15]: product is 30, which is the product of distinct primes 2, 3, and 5. - [3]: product is 3, which is the product of distinct prime 3. - [15]: product is 15, which is the product of distinct primes 3 and 5.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numberOfGoodSubsets 
from collections import Counter
from typing import *
def f_gold(nums: List[int]) -> int:
    counter = Counter(nums)
    mod = 10**9 + 7
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    n = len(prime)
    dp = [0] * (1 << n)
    dp[0] = 1
    for x in range(2, 31):
        if counter[x] == 0 or x % 4 == 0 or x % 9 == 0 or x % 25 == 0:
            continue
        mask = 0
        for i, p in enumerate(prime):
            if x % p == 0:
                mask |= 1 << i
        for state in range(1 << n):
            if mask & state:
                continue
            dp[mask | state] = (dp[mask | state] + counter[x] * dp[state]) % mod
    ans = 0
    for i in range(1, 1 << n):
        ans = (ans + dp[i]) % mod
    for i in range(counter[1]):
        ans = (ans << 1) % mod
    return ans
"-----------------"
test()

