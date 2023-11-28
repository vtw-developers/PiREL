from L1409_QueriesonaPermutationWithKey import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 1, 2, 1], 5]
    # output: [2,1,2,1]
    # EXPLANATION:  The queries are processed as follow:   For i=0: queries[i]=3, P=[1,2,3,4,5], position of 3 in P is <strong>2</strong>, then we move 3 to the beginning of P resulting in P=[3,1,2,4,5].   For i=1: queries[i]=1, P=[3,1,2,4,5], position of 1 in P is <strong>1</strong>, then we move 1 to the beginning of P resulting in P=[1,3,2,4,5].   For i=2: queries[i]=2, P=[1,3,2,4,5], position of 2 in P is <strong>2</strong>, then we move 2 to the beginning of P resulting in P=[2,1,3,4,5].   For i=3: queries[i]=1, P=[2,1,3,4,5], position of 1 in P is <strong>1</strong>, then we move 1 to the beginning of P resulting in P=[1,2,3,4,5].   Therefore, the array containing the result is [2,1,2,1].
    ,
    # example 2
    [[4, 1, 2, 2], 4]
    # output: [3,1,2,0]
    ,
    # example 3
    [[7, 5, 5, 8, 3], 8]
    # output: [6,5,0,7,5]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
