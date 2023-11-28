from L2122_RecovertheOriginalArray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 10, 6, 4, 8, 12]]
    # output: [3,7,11]
    # EXPLANATION:  If arr = [3,7,11] and k = 1, we get lower = [2,6,10] and higher = [4,8,12]. Combining lower and higher gives us [2,6,10,4,8,12], which is a permutation of nums. Another valid possibility is that arr = [5,7,9] and k = 3. In that case, lower = [2,4,6] and higher = [8,10,12].
    ,
    # example 2
    [[1, 1, 3, 3]]
    # output: [2,2]
    # EXPLANATION:  If arr = [2,2] and k = 1, we get lower = [1,1] and higher = [3,3]. Combining lower and higher gives us [1,1,3,3], which is equal to nums. Note that arr cannot be [1,3] because in that case, the only possible way to obtain [1,1,3,3] is with k = 0. This is invalid since k must be positive.
    ,
    # example 3
    [[5, 435]]
    # output: [220]
    # EXPLANATION:  The only possible combination is arr = [220] and k = 215. Using them, we get lower = [5] and higher = [435].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
