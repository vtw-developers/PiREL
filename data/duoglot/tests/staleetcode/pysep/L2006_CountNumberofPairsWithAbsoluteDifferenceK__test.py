from L2006_CountNumberofPairsWithAbsoluteDifferenceK import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 2, 1], 1]
    # output: 4
    # EXPLANATION:  The pairs with an absolute difference of 1 are: - [<strong><u>1</u></strong>,<strong><u>2</u></strong>,2,1] - [<strong><u>1</u></strong>,2,<strong><u>2</u></strong>,1] - [1,<strong><u>2</u></strong>,2,<strong><u>1</u></strong>] - [1,2,<strong><u>2</u></strong>,<strong><u>1</u></strong>]
    ,
    # example 2
    [[1, 3], 3]
    # output: 0
    # EXPLANATION:  There are no pairs with an absolute difference of 3.
    ,
    # example 3
    [[3, 2, 1, 5, 4], 2]
    # output: 3
    # EXPLANATION:  The pairs with an absolute difference of 2 are: - [<strong><u>3</u></strong>,2,<strong><u>1</u></strong>,5,4] - [<strong><u>3</u></strong>,2,1,<strong><u>5</u></strong>,4] - [3,<strong><u>2</u></strong>,1,5,<strong><u>4</u></strong>]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
