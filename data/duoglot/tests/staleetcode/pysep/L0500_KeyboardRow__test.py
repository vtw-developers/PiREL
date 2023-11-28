from L0500_KeyboardRow import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["Hello", "Alaska", "Dad", "Peace"]]
    # output: ["Alaska","Dad"]
    ,
    # example 2
    [["omk"]]
    # output: []
    ,
    # example 3
    [["adsdf", "sfd"]]
    # output: ["adsdf","sfd"]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
