from L0760_FindAnagramMappings import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[12, 28, 46, 32, 50], [50, 12, 32, 46, 28]]
    # output: [1,4,3,2,0]
    # EXPLANATION:  As mapping[0] = 1 because the 0<sup>th</sup> element of nums1 appears at nums2[1], and mapping[1] = 4 because the 1<sup>st</sup> element of nums1 appears at nums2[4], and so on.
    ,
    # example 2
    [[84, 46], [84, 46]]
    # output: [0,1]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
