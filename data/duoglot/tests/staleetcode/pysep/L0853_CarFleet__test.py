from L0853_CarFleet import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]]
    # output: 3
    # EXPLANATION:  The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The car starting at 0 does not catch up to any other car, so it is a fleet by itself. The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target. Note that no other cars meet these fleets before the destination, so the answer is 3.
    ,
    # example 2
    [10, [3], [3]]
    # output: 1
    # EXPLANATION:  There is only one car, hence there is only one fleet.
    ,
    # example 3
    [100, [0, 2, 4], [4, 2, 1]]
    # output: 1
    # EXPLANATION:  The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The fleet moves at speed 2. Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
