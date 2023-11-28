from L2157_GroupsofStrings import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["a", "b", "ab", "cde"]]
    # output: [2,3]
    # EXPLANATION:  - words[0] can be used to obtain words[1] (by replacing 'a' with 'b'), and words[2] (by adding 'b'). So words[0] is connected to words[1] and words[2]. - words[1] can be used to obtain words[0] (by replacing 'b' with 'a'), and words[2] (by adding 'a'). So words[1] is connected to words[0] and words[2]. - words[2] can be used to obtain words[0] (by deleting 'b'), and words[1] (by deleting 'a'). So words[2] is connected to words[0] and words[1]. - words[3] is not connected to any string in words. Thus, words can be divided into 2 groups ["a","b","ab"] and ["cde"]. The size of the largest group is 3.
    ,
    # example 2
    [["a", "ab", "abc"]]
    # output: [1,3]
    # EXPLANATION:  - words[0] is connected to words[1]. - words[1] is connected to words[0] and words[2]. - words[2] is connected to words[1]. Since all strings are connected to each other, they should be grouped together. Thus, the size of the largest group is 3.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
