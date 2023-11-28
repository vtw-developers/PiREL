from L2267_CheckifThereIsaValidParenthesesStringPath import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[["(", "(", "("], [")", "(", ")"], ["(", "(", ")"], ["(", "(", ")"]]]
    # output: true
    # EXPLANATION:  The above diagram shows two possible paths that form valid parentheses strings. The first path shown results in the valid parentheses string "()(())". The second path shown results in the valid parentheses string "((()))". Note that there may be other valid parentheses string paths.
    ,
    # example 2
    [[[")", ")"], ["(", "("]]]
    # output: false
    # EXPLANATION:  The two possible paths form the parentheses strings "))(" and ")((". Since neither of them are valid parentheses strings, we return false.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
