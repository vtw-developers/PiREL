
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 2, 3, 3], 5, 5]
    # output: 1
    # EXPLANATION:  - Initially, Alice and Bob have 5 units of water each in their watering cans. - Alice waters plant 0, Bob waters plant 3. - Alice and Bob now have 3 units and 2 units of water respectively. - Alice has enough water for plant 1, so she waters it. Bob does not have enough water for plant 2, so he refills his can then waters it. So, the total number of times they have to refill to water all the plants is 0 + 0 + 1 + 0 = 1.
    ,
    # example 2
    [[2, 2, 3, 3], 3, 4]
    # output: 2
    # EXPLANATION:  - Initially, Alice and Bob have 3 units and 4 units of water in their watering cans respectively. - Alice waters plant 0, Bob waters plant 3. - Alice and Bob now have 1 unit of water each, and need to water plants 1 and 2 respectively. - Since neither of them have enough water for their current plants, they refill their cans and then water the plants. So, the total number of times they have to refill to water all the plants is 0 + 1 + 1 + 0 = 2.
    ,
    # example 3
    [[5], 10, 8]
    # output: 0
    # EXPLANATION:  - There is only one plant. - Alice's watering can has 10 units of water, whereas Bob's can has 8 units. Since Alice has more water in her can, she waters this plant. So, the total number of times they have to refill is 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minimumRefill 
from typing import *
def f_gold(plants: List[int], capacityA: int, capacityB: int) -> int:
    i, j = 0, len(plants) - 1
    ans = 0
    a, b = capacityA, capacityB
    while i <= j:
        if i == j:
            if max(capacityA, capacityB) < plants[i]:
                ans += 1
            break
        if capacityA < plants[i]:
            capacityA = a - plants[i]
            ans += 1
        else:
            capacityA -= plants[i]
        if capacityB < plants[j]:
            capacityB = b - plants[j]
            ans += 1
        else:
            capacityB -= plants[j]
        i += 1
        j -= 1
    return ans
"-----------------"
test()

