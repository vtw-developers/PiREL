from L2249_CountLatticePointsInsideaCircle import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[2, 2, 1]]]
    # output: 5
    # EXPLANATION:  The figure above shows the given circle. The lattice points present inside the circle are (1, 2), (2, 1), (2, 2), (2, 3), and (3, 2) and are shown in green. Other points such as (1, 1) and (1, 3), which are shown in red, are not considered inside the circle. Hence, the number of lattice points present inside at least one circle is 5.
    ,
    # example 2
    [[[2, 2, 2], [3, 4, 1]]]
    # output: 16
    # EXPLANATION:  The figure above shows the given circles. There are exactly 16 lattice points which are present inside at least one circle.  Some of them are (0, 2), (2, 0), (2, 4), (3, 2), and (4, 4).
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
