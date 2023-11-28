from L0864_ShortestPathtoGetAllKeys import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["@.a..", "###.#", "b.A.B"]]
    # output: 8
    # EXPLANATION:  Note that the goal is to obtain all the keys not to open all the locks.
    ,
    # example 2
    [["@..aA", "..B#.", "....b"]]
    # output: 6
    ,
    # example 3
    [["@Aa"]]
    # output: -1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
