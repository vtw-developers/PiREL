from L2200_FindAllKDistantIndicesinanArray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 4, 9, 1, 3, 9, 5], 9, 1]
    # output: [1,2,3,4,5,6]
    # EXPLANATION:  Here, <code>nums[2] == key</code> and <code>nums[5] == key. - For index 0, |0 - 2| > k and |0 - 5| > k, so there is no j</code> where <code>|0 - j| <= k</code> and <code>nums[j] == key. Thus, 0 is not a k-distant index. - For index 1, |1 - 2| <= k and nums[2] == key, so 1 is a k-distant index. - For index 2, |2 - 2| <= k and nums[2] == key, so 2 is a k-distant index. - For index 3, |3 - 2| <= k and nums[2] == key, so 3 is a k-distant index. - For index 4, |4 - 5| <= k and nums[5] == key, so 4 is a k-distant index. - For index 5, |5 - 5| <= k and nums[5] == key, so 5 is a k-distant index. - For index 6, |6 - 5| <= k and nums[5] == key, so 6 is a k-distant index. </code>Thus, we return [1,2,3,4,5,6] which is sorted in increasing order.
    ,
    # example 2
    [[2, 2, 2, 2, 2], 2, 2]
    # output: [0,1,2,3,4]
    # EXPLANATION:  For all indices i in nums, there exists some index j such that |i - j| <= k and nums[j] == key, so every index is a k-distant index.  Hence, we return [0,1,2,3,4].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
