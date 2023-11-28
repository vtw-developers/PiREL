from L0027_RemoveElement import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 2, 2, 3], 3]
    # output: 2, nums = [2,2,_,_]
    # EXPLANATION:  Your function should return k = 2, with the first two elements of nums being 2. It does not matter what you leave beyond the returned k (hence they are underscores).
    ,
    # example 2
    [[0, 1, 2, 2, 3, 0, 4, 2], 2]
    # output: 5, nums = [0,1,4,0,3,_,_,_]
    # EXPLANATION:  Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4. Note that the five elements can be returned in any order. It does not matter what you leave beyond the returned k (hence they are underscores).
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
