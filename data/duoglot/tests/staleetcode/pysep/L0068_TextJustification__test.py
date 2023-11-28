from L0068_TextJustification import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["This", "is", "an", "example", "of", "text", "justification."], 16]
    # output: [   "This    is    an",   "example  of text",   "justification.  "]
    ,
    # example 2
    [["What", "must", "be", "acknowledgment", "shall", "be"], 16]
    # output: [  "What   must   be",  "acknowledgment  ",  "shall be        "]
    # EXPLANATION:  Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified. Note that the second line is also left-justified because it contains only one word.
    ,
    # example 3
    [["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20]
    # output: [  "Science  is  what we",  "understand      well",  "enough to explain to",  "a  computer.  Art is",  "everything  else  we",  "do                  "]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
