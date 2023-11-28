from L0026_RemoveDuplicatesfromSortedArray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 1, 2]]
    # output: 2, nums = [1,2,_]
    # EXPLANATION:  Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).
    ,
    # example 2
    [[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]]
    # output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    # EXPLANATION:  Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
