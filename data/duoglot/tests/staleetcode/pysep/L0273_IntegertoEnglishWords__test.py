from L0273_IntegertoEnglishWords import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [123]
    # output: "One Hundred Twenty Three"
    ,
    # example 2
    [12345]
    # output: "Twelve Thousand Three Hundred Forty Five"
    ,
    # example 3
    [1234567]
    # output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
