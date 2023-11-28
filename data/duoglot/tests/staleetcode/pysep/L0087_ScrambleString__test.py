from L0087_ScrambleString import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["great", "rgeat"]
    # output: true
    # EXPLANATION:  One possible scenario applied on s1 is: "great" --> "gr/eat" // divide at random index. "gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order. "gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at random index each of them. "g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second substring in the same order. "r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t". "r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order. The algorithm stops now, and the result string is "rgeat" which is s2. As one possible scenario led s1 to be scrambled to s2, we return true.
    ,
    # example 2
    ["abcde", "caebd"]
    # output: false
    ,
    # example 3
    ["a", "a"]
    # output: true
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
