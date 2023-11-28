from L1029_TwoCityScheduling import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[10, 20], [30, 200], [400, 50], [30, 20]]]
    # output: 110
    # EXPLANATION:  The first person goes to city A for a cost of 10. The second person goes to city A for a cost of 30. The third person goes to city B for a cost of 50. The fourth person goes to city B for a cost of 20.  The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
    ,
    # example 2
    [[[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]]
    # output: 1859
    ,
    # example 3
    [[[515, 563], [451, 713], [537, 709], [343, 819], [855, 779], [457, 60], [650, 359], [631, 42]]]
    # output: 3086
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
