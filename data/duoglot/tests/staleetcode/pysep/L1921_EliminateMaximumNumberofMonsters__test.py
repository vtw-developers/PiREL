from L1921_EliminateMaximumNumberofMonsters import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 3, 4], [1, 1, 1]]
    # output: 3
    # EXPLANATION:  In the beginning, the distances of the monsters are [1,3,4]. You eliminate the first monster. After a minute, the distances of the monsters are [X,2,3]. You eliminate the second monster. After a minute, the distances of the monsters are [X,X,2]. You eliminate the thrid monster. All 3 monsters can be eliminated.
    ,
    # example 2
    [[1, 1, 2, 3], [1, 1, 1, 1]]
    # output: 1
    # EXPLANATION:  In the beginning, the distances of the monsters are [1,1,2,3]. You eliminate the first monster. After a minute, the distances of the monsters are [X,0,1,2], so you lose. You can only eliminate 1 monster.
    ,
    # example 3
    [[3, 2, 4], [5, 3, 2]]
    # output: 1
    # EXPLANATION:  In the beginning, the distances of the monsters are [3,2,4]. You eliminate the first monster. After a minute, the distances of the monsters are [X,0,2], so you lose. You can only eliminate 1 monster.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
