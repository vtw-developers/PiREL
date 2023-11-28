from L0806_NumberofLinesToWriteString import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10], "abcdefghijklmnopqrstuvwxyz"]
    # output: [3,60]
    # EXPLANATION:  You can write s as follows: abcdefghij  // 100 pixels wide klmnopqrst  // 100 pixels wide uvwxyz      // 60 pixels wide There are a total of 3 lines, and the last line is 60 pixels wide.
    ,
    # example 2
    [[4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10], "bbbcccdddaaa"]
    # output: [2,4]
    # EXPLANATION:  You can write s as follows: bbbcccdddaa  // 98 pixels wide a            // 4 pixels wide There are a total of 2 lines, and the last line is 4 pixels wide.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
