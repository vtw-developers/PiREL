from L1239_MaximumLengthofaConcatenatedStringwithUniqueCharacters import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["un", "iq", "ue"]]
    # output: 4
    # EXPLANATION:  All the valid concatenations are: - "" - "un" - "iq" - "ue" - "uniq" ("un" + "iq") - "ique" ("iq" + "ue") Maximum length is 4.
    ,
    # example 2
    [["cha", "r", "act", "ers"]]
    # output: 6
    # EXPLANATION:  Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
    ,
    # example 3
    [["abcdefghijklmnopqrstuvwxyz"]]
    # output: 26
    # EXPLANATION:  The only string in arr has all 26 characters.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
