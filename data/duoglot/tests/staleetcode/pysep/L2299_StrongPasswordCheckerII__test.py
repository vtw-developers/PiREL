from L2299_StrongPasswordCheckerII import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["IloveLe3tcode!"]
    # output: true
    # EXPLANATION:  The password meets all the requirements. Therefore, we return true.
    ,
    # example 2
    ["Me+You--IsMyDream"]
    # output: false
    # EXPLANATION:  The password does not contain a digit and also contains 2 of the same character in adjacent positions. Therefore, we return false.
    ,
    # example 3
    ["1aB!"]
    # output: false
    # EXPLANATION:  The password does not meet the length requirement. Therefore, we return false.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
