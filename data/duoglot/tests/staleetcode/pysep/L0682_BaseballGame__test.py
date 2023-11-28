from L0682_BaseballGame import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["5", "2", "C", "D", "+"]]
    # output: 30
    # EXPLANATION:  "5" - Add 5 to the record, record is now [5]. "2" - Add 2 to the record, record is now [5, 2]. "C" - Invalidate and remove the previous score, record is now [5]. "D" - Add 2 * 5 = 10 to the record, record is now [5, 10]. "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15]. The total sum is 5 + 10 + 15 = 30.
    ,
    # example 2
    [["5", "-2", "4", "C", "D", "9", "+", "+"]]
    # output: 27
    # EXPLANATION:  "5" - Add 5 to the record, record is now [5]. "-2" - Add -2 to the record, record is now [5, -2]. "4" - Add 4 to the record, record is now [5, -2, 4]. "C" - Invalidate and remove the previous score, record is now [5, -2]. "D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4]. "9" - Add 9 to the record, record is now [5, -2, -4, 9]. "+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5]. "+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14]. The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.
    ,
    # example 3
    [["1", "C"]]
    # output: 0
    # EXPLANATION:  "1" - Add 1 to the record, record is now [1]. "C" - Invalidate and remove the previous score, record is now []. Since the record is empty, the total sum is 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
