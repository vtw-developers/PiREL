from L0444_SequenceReconstruction import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3], [[1, 2], [1, 3]]]
    # output: false
    # EXPLANATION:  There are two possible supersequences: [1,2,3] and [1,3,2]. The sequence [1,2] is a subsequence of both: [<strong><u>1</u></strong>,<strong><u>2</u></strong>,3] and [<strong><u>1</u></strong>,3,<strong><u>2</u></strong>]. The sequence [1,3] is a subsequence of both: [<strong><u>1</u></strong>,2,<strong><u>3</u></strong>] and [<strong><u>1</u></strong>,<strong><u>3</u></strong>,2]. Since nums is not the only shortest supersequence, we return false.
    ,
    # example 2
    [[1, 2, 3], [[1, 2]]]
    # output: false
    # EXPLANATION:  The shortest possible supersequence is [1,2]. The sequence [1,2] is a subsequence of it: [<strong><u>1</u></strong>,<strong><u>2</u></strong>]. Since nums is not the shortest supersequence, we return false.
    ,
    # example 3
    [[1, 2, 3], [[1, 2], [1, 3], [2, 3]]]
    # output: true
    # EXPLANATION:  The shortest possible supersequence is [1,2,3]. The sequence [1,2] is a subsequence of it: [<strong><u>1</u></strong>,<strong><u>2</u></strong>,3]. The sequence [1,3] is a subsequence of it: [<strong><u>1</u></strong>,2,<strong><u>3</u></strong>]. The sequence [2,3] is a subsequence of it: [1,<strong><u>2</u></strong>,<strong><u>3</u></strong>]. Since nums is the only shortest supersequence, we return true.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
