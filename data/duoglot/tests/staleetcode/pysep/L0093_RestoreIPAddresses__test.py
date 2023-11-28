from L0093_RestoreIPAddresses import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["25525511135"]
    # output: ["255.255.11.135","255.255.111.35"]
    ,
    # example 2
    ["0000"]
    # output: ["0.0.0.0"]
    ,
    # example 3
    ["101023"]
    # output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
