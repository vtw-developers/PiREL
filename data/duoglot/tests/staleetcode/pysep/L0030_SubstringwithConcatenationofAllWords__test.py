from L0030_SubstringwithConcatenationofAllWords import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["barfoothefoobarman", ["foo", "bar"]]
    # output: [0,9]
    # EXPLANATION:  Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively. The output order does not matter, returning [9,0] is fine too.
    ,
    # example 2
    ["wordgoodgoodgoodbestword", ["word", "good", "best", "word"]]
    # output: []
    ,
    # example 3
    ["barfoofoobarthefoobarman", ["bar", "foo", "the"]]
    # output: [6,9,12]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
