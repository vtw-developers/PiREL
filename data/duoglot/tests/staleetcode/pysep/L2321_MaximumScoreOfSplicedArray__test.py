from L2321_MaximumScoreOfSplicedArray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[60, 60, 60], [10, 90, 10]]
    # output: 210
    # EXPLANATION:  Choosing left = 1 and right = 1, we have nums1 = [60,<u><strong>90</strong></u>,60] and nums2 = [10,<u><strong>60</strong></u>,10]. The score is max(sum(nums1), sum(nums2)) = max(210, 80) = 210.
    ,
    # example 2
    [[20, 40, 20, 70, 30], [50, 20, 50, 40, 20]]
    # output: 220
    # EXPLANATION:  Choosing left = 3, right = 4, we have nums1 = [20,40,20,<u><strong>40,20</strong></u>] and nums2 = [50,20,50,<u><strong>70,30</strong></u>]. The score is max(sum(nums1), sum(nums2)) = max(140, 220) = 220.
    ,
    # example 3
    [[7, 11, 13], [1, 1, 1]]
    # output: 31
    # EXPLANATION:  We choose not to swap any subarray. The score is max(sum(nums1), sum(nums2)) = max(31, 3) = 31.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
