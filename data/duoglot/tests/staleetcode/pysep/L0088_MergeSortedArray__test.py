from L0088_MergeSortedArray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3]
    # output: [1,2,2,3,5,6]
    # EXPLANATION:  The arrays we are merging are [1,2,3] and [2,5,6]. The result of the merge is [<u>1</u>,<u>2</u>,2,<u>3</u>,5,6] with the underlined elements coming from nums1.
    ,
    # example 2
    [[1], 1, [], 0]
    # output: [1]
    # EXPLANATION:  The arrays we are merging are [1] and []. The result of the merge is [1].
    ,
    # example 3
    [[0], 0, [1], 1]
    # output: [1]
    # EXPLANATION:  The arrays we are merging are [] and [1]. The result of the merge is [1]. Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
