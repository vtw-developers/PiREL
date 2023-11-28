from L2186_MinimumNumberofStepstoMakeTwoStringsAnagramII import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["leetcode", "coats"]
    # output: 7
    # EXPLANATION:   - In 2 steps, we can append the letters in "as" onto s = "leetcode", forming s = "leetcode<strong><u>as</u></strong>". - In 5 steps, we can append the letters in "leede" onto t = "coats", forming t = "coats<u><strong>leede</strong></u>". "leetcodeas" and "coatsleede" are now anagrams of each other. We used a total of 2 + 5 = 7 steps. It can be shown that there is no way to make them anagrams of each other with less than 7 steps.
    ,
    # example 2
    ["night", "thing"]
    # output: 0
    # EXPLANATION:  The given strings are already anagrams of each other. Thus, we do not need any further steps.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
