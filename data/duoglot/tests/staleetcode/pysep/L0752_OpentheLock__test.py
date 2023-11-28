from L0752_OpentheLock import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["0201", "0101", "0102", "1212", "2002"], "0202"]
    # output: 6
    # EXPLANATION:   A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202". Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid, because the wheels of the lock become stuck after the display becomes the dead end "0102".
    ,
    # example 2
    [["8888"], "0009"]
    # output: 1
    # EXPLANATION:  We can turn the last wheel in reverse to move from "0000" -> "0009".
    ,
    # example 3
    [["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888"]
    # output: -1
    # EXPLANATION:  We cannot reach the target without getting stuck.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
