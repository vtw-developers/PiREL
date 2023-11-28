from L1258_SynonymousSentences import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[["happy", "joy"], ["sad", "sorrow"], ["joy", "cheerful"]], "I am happy today but was sad yesterday"]
    # output: ["I am cheerful today but was sad yesterday","I am cheerful today but was sorrow yesterday","I am happy today but was sad yesterday","I am happy today but was sorrow yesterday","I am joy today but was sad yesterday","I am joy today but was sorrow yesterday"]
    ,
    # example 2
    [[["happy", "joy"], ["cheerful", "glad"]], "I am happy today but was sad yesterday"]
    # output: ["I am happy today but was sad yesterday","I am joy today but was sad yesterday"]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
