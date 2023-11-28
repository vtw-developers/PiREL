
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[["Earth", "North America", "South America"], ["North America", "United States", "Canada"], ["United States", "New York", "Boston"], ["Canada", "Ontario", "Quebec"], ["South America", "Brazil"]], "Quebec", "New York"]
    # output: "North America"
    ,
    # example 2
    [[["Earth", "North America", "South America"], ["North America", "United States", "Canada"], ["United States", "New York", "Boston"], ["Canada", "Ontario", "Quebec"], ["South America", "Brazil"]], "Canada", "South America"]
    # output: "Earth"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findSmallestRegion 
from typing import *
def f_gold(regions: List[List[str]], region1: str, region2: str
) -> str:
    m = {}
    for region in regions:
        for r in region[1:]:
            m[r] = region[0]
    s = set()
    while m.get(region1):
        s.add(region1)
        region1 = m[region1]
    while m.get(region2):
        if region2 in s:
            return region2
        region2 = m[region2]
    return region1
"-----------------"
test()

