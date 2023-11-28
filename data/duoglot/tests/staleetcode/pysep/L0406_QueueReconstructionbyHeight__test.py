from L0406_QueueReconstructionbyHeight import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]]
    # output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
    # EXPLANATION:  Person 0 has height 5 with no other people taller or the same height in front. Person 1 has height 7 with no other people taller or the same height in front. Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1. Person 3 has height 6 with one person taller or the same height in front, which is person 1. Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3. Person 5 has height 7 with one person taller or the same height in front, which is person 1. Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.
    ,
    # example 2
    [[[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]]
    # output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
