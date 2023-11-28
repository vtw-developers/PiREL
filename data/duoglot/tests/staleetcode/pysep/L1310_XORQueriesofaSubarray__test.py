from L1310_XORQueriesofaSubarray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]]]
    # output: [2,7,14,8]
    # EXPLANATION:   The binary representation of the elements in the array are: 1 = 0001  3 = 0011  4 = 0100  8 = 1000  The XOR values for queries are: [0,1] = 1 xor 3 = 2  [1,2] = 3 xor 4 = 7  [0,3] = 1 xor 3 xor 4 xor 8 = 14  [3,3] = 8
    ,
    # example 2
    [[4, 8, 2, 10], [[2, 3], [1, 3], [0, 0], [0, 3]]]
    # output: [8,0,4,4]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
