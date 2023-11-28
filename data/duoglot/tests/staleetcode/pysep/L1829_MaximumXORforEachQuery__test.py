from L1829_MaximumXORforEachQuery import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[0, 1, 1, 3], 2]
    # output: [0,3,2,3]
    # EXPLANATION: : The queries are answered as follows: 1<sup>st</sup> query: nums = [0,1,1,3], k = 0 since 0 XOR 1 XOR 1 XOR 3 XOR 0 = 3. 2<sup>nd</sup> query: nums = [0,1,1], k = 3 since 0 XOR 1 XOR 1 XOR 3 = 3. 3<sup>rd</sup> query: nums = [0,1], k = 2 since 0 XOR 1 XOR 2 = 3. 4<sup>th</sup> query: nums = [0], k = 3 since 0 XOR 3 = 3.
    ,
    # example 2
    [[2, 3, 4, 7], 3]
    # output: [5,2,6,5]
    # EXPLANATION: : The queries are answered as follows: 1<sup>st</sup> query: nums = [2,3,4,7], k = 5 since 2 XOR 3 XOR 4 XOR 7 XOR 5 = 7. 2<sup>nd</sup> query: nums = [2,3,4], k = 2 since 2 XOR 3 XOR 4 XOR 2 = 7. 3<sup>rd</sup> query: nums = [2,3], k = 6 since 2 XOR 3 XOR 6 = 7. 4<sup>th</sup> query: nums = [2], k = 5 since 2 XOR 5 = 7.
    ,
    # example 3
    [[0, 1, 2, 2, 5, 7], 3]
    # output: [4,3,6,4,6,7]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
