from L2101_DetonatetheMaximumBombs import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[2, 1, 3], [6, 1, 4]]]
    # output: 2
    # EXPLANATION:  The above figure shows the positions and ranges of the 2 bombs. If we detonate the left bomb, the right bomb will not be affected. But if we detonate the right bomb, both bombs will be detonated. So the maximum bombs that can be detonated is max(1, 2) = 2.
    ,
    # example 2
    [[[1, 1, 5], [10, 10, 5]]]
    # output: 1
    # EXPLANATION: Detonating either bomb will not detonate the other bomb, so the maximum number of bombs that can be detonated is 1.
    ,
    # example 3
    [[[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]]
    # output: 5
    # EXPLANATION:  The best bomb to detonate is bomb 0 because: - Bomb 0 detonates bombs 1 and 2. The red circle denotes the range of bomb 0. - Bomb 2 detonates bomb 3. The blue circle denotes the range of bomb 2. - Bomb 3 detonates bomb 4. The green circle denotes the range of bomb 3. Thus all 5 bombs are detonated.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
