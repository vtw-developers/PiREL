from L2090_KRadiusSubarrayAverages import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[7, 4, 3, 9, 1, 8, 5, 2, 6], 3]
    # output: [-1,-1,-1,5,4,4,-1,-1,-1]
    # EXPLANATION:  - avg[0], avg[1], and avg[2] are -1 because there are less than k elements <strong>before</strong> each index. - The sum of the subarray centered at index 3 with radius 3 is: 7 + 4 + 3 + 9 + 1 + 8 + 5 = 37.   Using <strong>integer division</strong>, avg[3] = 37 / 7 = 5. - For the subarray centered at index 4, avg[4] = (4 + 3 + 9 + 1 + 8 + 5 + 2) / 7 = 4. - For the subarray centered at index 5, avg[5] = (3 + 9 + 1 + 8 + 5 + 2 + 6) / 7 = 4. - avg[6], avg[7], and avg[8] are -1 because there are less than k elements <strong>after</strong> each index.
    ,
    # example 2
    [[100000], 0]
    # output: [100000]
    # EXPLANATION:  - The sum of the subarray centered at index 0 with radius 0 is: 100000.   avg[0] = 100000 / 1 = 100000.
    ,
    # example 3
    [[8], 100000]
    # output: [-1]
    # EXPLANATION:   - avg[0] is -1 because there are less than k elements before and after index 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
