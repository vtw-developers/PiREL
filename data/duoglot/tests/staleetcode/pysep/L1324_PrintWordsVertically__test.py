from L1324_PrintWordsVertically import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["HOW ARE YOU"]
    # output: ["HAY","ORO","WEU"]
    # EXPLANATION: Each word is printed vertically.    "HAY"   "ORO"   "WEU"
    ,
    # example 2
    ["TO BE OR NOT TO BE"]
    # output: ["TBONTB","OEROOE","   T"]
    # EXPLANATION: Trailing spaces is not allowed.   "TBONTB"  "OEROOE"  "   T"
    ,
    # example 3
    ["CONTEST IS COMING"]
    # output: ["CIC","OSO","N M","T I","E N","S G","T"]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
