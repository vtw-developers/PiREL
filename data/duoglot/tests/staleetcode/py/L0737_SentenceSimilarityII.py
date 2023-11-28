
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


"-----------------"
### areSentencesSimilarTwo 
from typing import *
def f_gold(sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]
) -> bool:
    if len(sentence1) != len(sentence2):
        return False
    n = len(similarPairs)
    p = list(range(n << 1))
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    words = {}
    idx = 0
    for a, b in similarPairs:
        if a not in words:
            words[a] = idx
            idx += 1
        if b not in words:
            words[b] = idx
            idx += 1
        p[find(words[a])] = find(words[b])
    for i in range(len(sentence1)):
        if sentence1[i] == sentence2[i]:
            continue
        if (
            sentence1[i] not in words
            or sentence2[i] not in words
            or find(words[sentence1[i]]) != find(words[sentence2[i]])
        ):
            return False
    return True
"-----------------"
test()

