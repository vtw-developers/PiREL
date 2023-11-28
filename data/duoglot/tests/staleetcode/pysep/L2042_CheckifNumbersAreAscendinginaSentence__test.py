from L2042_CheckifNumbersAreAscendinginaSentence import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["1 box has 3 blue 4 red 6 green and 12 yellow marbles"]
    # output: true
    # EXPLANATION:  The numbers in s are: 1, 3, 4, 6, 12. They are strictly increasing from left to right: 1 < 3 < 4 < 6 < 12.
    ,
    # example 2
    ["hello world 5 x 5"]
    # output: false
    # EXPLANATION:  The numbers in s are: <u><strong>5</strong></u>, <strong><u>5</u></strong>. They are not strictly increasing.
    ,
    # example 3
    ["sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"]
    # output: false
    # EXPLANATION:  The numbers in s are: 7, <u><strong>51</strong></u>, <u><strong>50</strong></u>, 60. They are not strictly increasing.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
