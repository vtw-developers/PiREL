from L1763_LongestNiceSubstring import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["YazaAay"]
    # output: "aAa"
    # EXPLANATION: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear. "aAa" is the longest nice substring.
    ,
    # example 2
    ["Bb"]
    # output: "Bb"
    # EXPLANATION:  "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.
    ,
    # example 3
    ["c"]
    # output: ""
    # EXPLANATION:  There are no nice substrings.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
