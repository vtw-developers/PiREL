from L0953_VerifyinganAlienDictionary import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"]
    # output: true
    # EXPLANATION: As 'h' comes before 'l' in this language, then the sequence is sorted.
    ,
    # example 2
    [["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"]
    # output: false
    # EXPLANATION: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
    ,
    # example 3
    [["apple", "app"], "abcdefghijklmnopqrstuvwxyz"]
    # output: false
    # EXPLANATION: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > ' ', where ' ' is defined as the blank character which is less than any other character (<a href="https://en.wikipedia.org/wiki/Lexicographical_order" target="_blank">More info</a>).
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
