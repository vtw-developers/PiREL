from L1629_SlowestKey import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[9, 29, 49, 50], "cbcd"]
    # output: "c"
    # EXPLANATION:  The keypresses were as follows: Keypress for 'c' had a duration of 9 (pressed at time 0 and released at time 9). Keypress for 'b' had a duration of 29 - 9 = 20 (pressed at time 9 right after the release of the previous character and released at time 29). Keypress for 'c' had a duration of 49 - 29 = 20 (pressed at time 29 right after the release of the previous character and released at time 49). Keypress for 'd' had a duration of 50 - 49 = 1 (pressed at time 49 right after the release of the previous character and released at time 50). The longest of these was the keypress for 'b' and the second keypress for 'c', both with duration 20. 'c' is lexicographically larger than 'b', so the answer is 'c'.
    ,
    # example 2
    [[12, 23, 36, 46, 62], "spuda"]
    # output: "a"
    # EXPLANATION:  The keypresses were as follows: Keypress for 's' had a duration of 12. Keypress for 'p' had a duration of 23 - 12 = 11. Keypress for 'u' had a duration of 36 - 23 = 13. Keypress for 'd' had a duration of 46 - 36 = 10. Keypress for 'a' had a duration of 62 - 46 = 16. The longest of these was the keypress for 'a' with duration 16.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
