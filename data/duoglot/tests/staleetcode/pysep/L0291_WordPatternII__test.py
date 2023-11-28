from L0291_WordPatternII import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abab", "redblueredblue"]
    # output: true
    # EXPLANATION:  One possible mapping is as follows: 'a' -> "red" 'b' -> "blue"
    ,
    # example 2
    ["aaaa", "asdasdasdasd"]
    # output: true
    # EXPLANATION:  One possible mapping is as follows: 'a' -> "asd"
    ,
    # example 3
    ["aabb", "xyzabcxzyabc"]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
