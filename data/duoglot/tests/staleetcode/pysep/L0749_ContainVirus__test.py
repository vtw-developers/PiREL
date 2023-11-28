from L0749_ContainVirus import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0]]]
    # output: 10
    # EXPLANATION:  There are 2 contaminated regions. On the first day, add 5 walls to quarantine the viral region on the left. The board after the virus spreads is: <img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0749.Contain%20Virus/images/virus12edited-grid.jpg" style="width: 500px; height: 257px;" /> On the second day, add 5 walls to quarantine the viral region on the right. The virus is fully contained. <img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0749.Contain%20Virus/images/virus13edited-grid.jpg" style="width: 500px; height: 261px;" />
    ,
    # example 2
    [[[1, 1, 1], [1, 0, 1], [1, 1, 1]]]
    # output: 4
    # EXPLANATION:  Even though there is only one cell saved, there are 4 walls built. Notice that walls are only built on the shared boundary of two different cells.
    ,
    # example 3
    [[[1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0, 0, 0]]]
    # output: 13
    # EXPLANATION:  The region on the left only builds two new walls.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
