from L0929_UniqueEmailAddresses import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]]
    # output: 2
    # EXPLANATION:  "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
    ,
    # example 2
    [["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]]
    # output: 3
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
