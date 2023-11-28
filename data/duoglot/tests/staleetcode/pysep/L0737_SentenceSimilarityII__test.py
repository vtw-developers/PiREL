from L0737_SentenceSimilarityII import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["great", "acting", "skills"], ["fine", "drama", "talent"], [["great", "good"], ["fine", "good"], ["drama", "acting"], ["skills", "talent"]]]
    # output: true
    # EXPLANATION:  The two sentences have the same length and each word i of sentence1 is also similar to the corresponding word in sentence2.
    ,
    # example 2
    [["I", "love", "leetcode"], ["I", "love", "onepiece"], [["manga", "onepiece"], ["platform", "anime"], ["leetcode", "platform"], ["anime", "manga"]]]
    # output: true
    # EXPLANATION:  "leetcode" --> "platform" --> "anime" --> "manga" --> "onepiece". Since "leetcode is similar to "onepiece" and the first two words are the same, the two sentences are similar.
    ,
    # example 3
    [["I", "love", "leetcode"], ["I", "love", "onepiece"], [["manga", "hunterXhunter"], ["platform", "anime"], ["leetcode", "platform"], ["anime", "manga"]]]
    # output: false
    # EXPLANATION:  "leetcode" is not similar to "onepiece".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
