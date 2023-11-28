from L0844_BackspaceStringCompare import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["ab#c", "ad#c"]
    # output: true
    # EXPLANATION:  Both s and t become "ac".
    ,
    # example 2
    ["ab##", "c#d#"]
    # output: true
    # EXPLANATION:  Both s and t become "".
    ,
    # example 3
    ["a#c", "b"]
    # output: false
    # EXPLANATION:  s becomes "c" while t becomes "b".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
