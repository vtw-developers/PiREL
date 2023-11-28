from L2268_MinimumNumberofKeypresses import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["apple"]
    # output: 5
    # EXPLANATION:  One optimal way to setup your keypad is shown above. Type 'a' by pressing button 1 once. Type 'p' by pressing button 6 once. Type 'p' by pressing button 6 once. Type 'l' by pressing button 5 once. Type 'e' by pressing button 3 once. A total of 5 button presses are needed, so return 5.
    ,
    # example 2
    ["abcdefghijkl"]
    # output: 15
    # EXPLANATION:  One optimal way to setup your keypad is shown above. The letters 'a' to 'i' can each be typed by pressing a button once. Type 'j' by pressing button 1 twice. Type 'k' by pressing button 2 twice. Type 'l' by pressing button 3 twice. A total of 15 button presses are needed, so return 15.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
