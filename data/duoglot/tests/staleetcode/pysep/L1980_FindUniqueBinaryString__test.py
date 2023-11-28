from L1980_FindUniqueBinaryString import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["01", "10"]]
    # output: "11"
    # EXPLANATION:  "11" does not appear in nums. "00" would also be correct.
    ,
    # example 2
    [["00", "01"]]
    # output: "11"
    # EXPLANATION:  "11" does not appear in nums. "10" would also be correct.
    ,
    # example 3
    [["111", "011", "001"]]
    # output: "101"
    # EXPLANATION:  "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
