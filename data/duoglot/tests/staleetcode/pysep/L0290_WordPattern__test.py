from L0290_WordPattern import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abba", "dog cat cat dog"]
    # output: true
    ,
    # example 2
    ["abba", "dog cat cat fish"]
    # output: false
    ,
    # example 3
    ["aaaa", "dog cat cat dog"]
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
