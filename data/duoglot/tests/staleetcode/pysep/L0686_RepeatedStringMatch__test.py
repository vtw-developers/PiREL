from L0686_RepeatedStringMatch import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abcd", "cdabcdab"]
    # output: 3
    # EXPLANATION:  We return 3 because by repeating a three times "ab<strong>cdabcdab</strong>cd", b is a substring of it.
    ,
    # example 2
    ["a", "aa"]
    # output: 2
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
