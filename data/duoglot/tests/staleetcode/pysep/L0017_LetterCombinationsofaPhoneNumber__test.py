from L0017_LetterCombinationsofaPhoneNumber import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["23"]
    # output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    ,
    # example 2
    [""]
    # output: []
    ,
    # example 3
    ["2"]
    # output: ["a","b","c"]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
