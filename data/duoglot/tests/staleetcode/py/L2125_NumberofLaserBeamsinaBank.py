
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["011001", "000000", "010100", "001000"]]
    # output: 8
    # EXPLANATION:  Between each of the following device pairs, there is one beam. In total, there are 8 beams:  * bank[0][1] -- bank[2][1]  * bank[0][1] -- bank[2][3]  * bank[0][2] -- bank[2][1]  * bank[0][2] -- bank[2][3]  * bank[0][5] -- bank[2][1]  * bank[0][5] -- bank[2][3]  * bank[2][1] -- bank[3][2]  * bank[2][3] -- bank[3][2] Note that there is no beam between any device on the 0<sup>th</sup> row with any on the 3<sup>rd</sup> row. This is because the 2<sup>nd</sup> row contains security devices, which breaks the second condition.
    ,
    # example 2
    [["000", "111", "000"]]
    # output: 0
    # EXPLANATION:  There does not exist two devices located on two different rows.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numberOfBeams 
from typing import *
def f_gold(bank: List[str]) -> int:
    last = ans = 0
    for b in bank:
        if (t := b.count('1')) > 0:
            ans += last * t
            last = t
    return ans
"-----------------"
test()

