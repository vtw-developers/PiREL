from L0692_TopKFrequentWords import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["i", "love", "leetcode", "i", "love", "coding"], 2]
    # output: ["i","love"]
    # EXPLANATION:  "i" and "love" are the two most frequent words. Note that "i" comes before "love" due to a lower alphabetical order.
    ,
    # example 2
    [["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4]
    # output: ["the","is","sunny","day"]
    # EXPLANATION:  "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
