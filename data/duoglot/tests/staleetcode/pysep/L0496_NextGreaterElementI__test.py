from L0496_NextGreaterElementI import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[4, 1, 2], [1, 3, 4, 2]]
    # output: [-1,3,-1]
    # EXPLANATION:  The next greater element for each value of nums1 is as follows: - 4 is underlined in nums2 = [1,3,<u>4</u>,2]. There is no next greater element, so the answer is -1. - 1 is underlined in nums2 = [<u>1</u>,3,4,2]. The next greater element is 3. - 2 is underlined in nums2 = [1,3,4,<u>2</u>]. There is no next greater element, so the answer is -1.
    ,
    # example 2
    [[2, 4], [1, 2, 3, 4]]
    # output: [3,-1]
    # EXPLANATION:  The next greater element for each value of nums1 is as follows: - 2 is underlined in nums2 = [1,<u>2</u>,3,4]. The next greater element is 3. - 4 is underlined in nums2 = [1,2,3,<u>4</u>]. There is no next greater element, so the answer is -1.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
