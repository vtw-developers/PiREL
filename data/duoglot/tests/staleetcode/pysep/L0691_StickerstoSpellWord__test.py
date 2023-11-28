from L0691_StickerstoSpellWord import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["with", "example", "science"], "thehat"]
    # output: 3
    # EXPLANATION:  We can use 2 "with" stickers, and 1 "example" sticker. After cutting and rearrange the letters of those stickers, we can form the target "thehat". Also, this is the minimum number of stickers necessary to form the target string.
    ,
    # example 2
    [["notice", "possible"], "basicbasic"]
    # output: -1
    # EXPLANATION:  We cannot form the target "basicbasic" from cutting letters from the given stickers.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
