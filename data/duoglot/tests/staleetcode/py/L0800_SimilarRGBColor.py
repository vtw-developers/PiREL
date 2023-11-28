
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["#09f166"]
    # output: "#11ee66"
    # EXPLANATION:   The similarity is -(0x09 - 0x11)<sup>2</sup> -(0xf1 - 0xee)<sup>2</sup> - (0x66 - 0x66)<sup>2</sup> = -64 -9 -0 = -73. This is the highest among any shorthand color.
    ,
    # example 2
    ["#4e3fe1"]
    # output: "#5544dd"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### similarRGB 
from typing import *
def f_gold(color: str) -> str:
    def f(x):
        y, z = divmod(int(x, 16), 17)
        if z > 8:
            y += 1
        return '{:02x}'.format(17 * y)
    a, b, c = color[1:3], color[3:5], color[5:7]
    return f'#{f(a)}{f(b)}{f(c)}'
"-----------------"
test()

