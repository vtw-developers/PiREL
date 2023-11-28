from L1371_FindtheLongestSubstringContainingVowelsinEvenCounts import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["eleetminicoworoep"]
    # output: 13
    # EXPLANATION: The longest substring is "leetminicowor" which contains two each of the vowels: <strong>e</strong>, <strong>i</strong> and <strong>o</strong> and zero of the vowels: <strong>a</strong> and <strong>u</strong>.
    ,
    # example 2
    ["leetcodeisgreat"]
    # output: 5
    # EXPLANATION:  The longest substring is "leetc" which contains two e's.
    ,
    # example 3
    ["bcbcbc"]
    # output: 6
    # EXPLANATION:  In this case, the given string "bcbcbc" is the longest because all vowels: <strong>a</strong>, <strong>e</strong>, <strong>i</strong>, <strong>o</strong> and <strong>u</strong> appear zero times.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
