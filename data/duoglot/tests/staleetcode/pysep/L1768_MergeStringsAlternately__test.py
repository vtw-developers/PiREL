from L1768_MergeStringsAlternately import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abc", "pqr"]
    # output: "apbqcr"
    # EXPLANATION:  The merged string will be merged as so:  word1:  a   b   c  word2:    p   q   r  merged: a p b q c r
    ,
    # example 2
    ["ab", "pqrs"]
    # output: "apbqrs"
    # EXPLANATION:  Notice that as word2 is longer, "rs" is appended to the end.  word1:  a   b   word2:    p   q   r   s  merged: a p b q   r   s
    ,
    # example 3
    ["abcd", "pq"]
    # output: "apbqcd"
    # EXPLANATION:  Notice that as word1 is longer, "cd" is appended to the end.  word1:  a   b   c   d  word2:    p   q   merged: a p b q c   d
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
