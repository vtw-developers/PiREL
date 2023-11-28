from L1313_DecompressRunLengthEncodedList import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4]]
    # output: [2,4,4,4]
    # EXPLANATION:  The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2]. The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4]. At the end the concatenation [2] + [4,4,4] is [2,4,4,4].
    ,
    # example 2
    [[1, 1, 2, 3]]
    # output: [1,3,3]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
