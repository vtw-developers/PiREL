from L1165_SingleRowKeyboard import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abcdefghijklmnopqrstuvwxyz", "cba"]
    # output: 4
    # EXPLANATION: The index moves from 0 to 2 to write 'c' then to 1 to write 'b' then to 0 again to write 'a'. Total time = 2 + 1 + 1 = 4.
    ,
    # example 2
    ["pqrstuvwxyzabcdefghijklmno", "leetcode"]
    # output: 73
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
