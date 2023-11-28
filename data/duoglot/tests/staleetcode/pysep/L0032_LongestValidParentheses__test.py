from L0032_LongestValidParentheses import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["(()"]
    # output: 2
    # EXPLANATION:  The longest valid parentheses substring is "()".
    ,
    # example 2
    [")()())"]
    # output: 4
    # EXPLANATION:  The longest valid parentheses substring is "()()".
    ,
    # example 3
    [""]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
