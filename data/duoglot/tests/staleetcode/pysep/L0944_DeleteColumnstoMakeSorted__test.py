from L0944_DeleteColumnstoMakeSorted import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["cba", "daf", "ghi"]]
    # output: 1
    # EXPLANATION:  The grid looks as follows:   cba   daf   ghi Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.
    ,
    # example 2
    [["a", "b"]]
    # output: 0
    # EXPLANATION:  The grid looks as follows:   a   b Column 0 is the only column and is sorted, so you will not delete any columns.
    ,
    # example 3
    [["zyx", "wvu", "tsr"]]
    # output: 3
    # EXPLANATION:  The grid looks as follows:   zyx   wvu   tsr All 3 columns are not sorted, so you will delete all 3.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
