from L1507_ReformatDate import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["20th Oct 2052"]
    # output: "2052-10-20"
    ,
    # example 2
    ["6th Jun 1933"]
    # output: "1933-06-06"
    ,
    # example 3
    ["26th May 1960"]
    # output: "1960-05-26"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
