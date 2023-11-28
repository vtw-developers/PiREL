from L0506_RelativeRanks import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[5, 4, 3, 2, 1]]
    # output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
    # EXPLANATION:  The placements are [1<sup>st</sup>, 2<sup>nd</sup>, 3<sup>rd</sup>, 4<sup>th</sup>, 5<sup>th</sup>].
    ,
    # example 2
    [[10, 3, 8, 9, 4]]
    # output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
    # EXPLANATION:  The placements are [1<sup>st</sup>, 5<sup>th</sup>, 3<sup>rd</sup>, 2<sup>nd</sup>, 4<sup>th</sup>].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
