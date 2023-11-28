from L2024_MaximizetheConfusionofanExam import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["TTFF", 2]
    # output: 4
    # EXPLANATION:  We can replace both the 'F's with 'T's to make answerKey = "<u>TTTT</u>". There are four consecutive 'T's.
    ,
    # example 2
    ["TFFT", 1]
    # output: 3
    # EXPLANATION:  We can replace the first 'T' with an 'F' to make answerKey = "<u>FFF</u>T". Alternatively, we can replace the second 'T' with an 'F' to make answerKey = "T<u>FFF</u>". In both cases, there are three consecutive 'F's.
    ,
    # example 3
    ["TTFTTFTT", 1]
    # output: 5
    # EXPLANATION:  We can replace the first 'F' to make answerKey = "<u>TTTTT</u>FTT" Alternatively, we can replace the second 'F' to make answerKey = "TTF<u>TTTTT</u>".  In both cases, there are five consecutive 'T's.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
