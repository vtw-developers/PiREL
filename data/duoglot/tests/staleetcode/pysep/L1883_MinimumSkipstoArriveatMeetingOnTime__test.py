from L1883_MinimumSkipstoArriveatMeetingOnTime import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 3, 2], 4, 2]
    # output: 1
    # EXPLANATION:  Without skipping any rests, you will arrive in (1/4 + 3/4) + (3/4 + 1/4) + (2/4) = 2.5 hours. You can skip the first rest to arrive in ((1/4 + <u>0</u>) + (3/4 + 0)) + (2/4) = 1.5 hours. Note that the second rest is shortened because you finish traveling the second road at an integer hour due to skipping the first rest.
    ,
    # example 2
    [[7, 3, 5, 5], 2, 10]
    # output: 2
    # EXPLANATION:  Without skipping any rests, you will arrive in (7/2 + 1/2) + (3/2 + 1/2) + (5/2 + 1/2) + (5/2) = 11.5 hours. You can skip the first and third rest to arrive in ((7/2 + <u>0</u>) + (3/2 + 0)) + ((5/2 + <u>0</u>) + (5/2)) = 10 hours.
    ,
    # example 3
    [[7, 3, 5, 5], 1, 10]
    # output: -1
    # EXPLANATION:  It is impossible to arrive at the meeting on time even if you skip all the rests.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
