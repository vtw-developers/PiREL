from L0526_BeautifulArrangement import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2]
    # output: 2
    # EXPLANATION:   The first beautiful arrangement is [1,2]:     - perm[1] = 1 is divisible by i = 1     - perm[2] = 2 is divisible by i = 2 The second beautiful arrangement is [2,1]:     - perm[1] = 2 is divisible by i = 1     - i = 2 is divisible by perm[2] = 1
    ,
    # example 2
    [1]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
