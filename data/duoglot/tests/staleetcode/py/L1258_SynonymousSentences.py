
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[["happy", "joy"], ["sad", "sorrow"], ["joy", "cheerful"]], "I am happy today but was sad yesterday"]
    # output: ["I am cheerful today but was sad yesterday","I am cheerful today but was sorrow yesterday","I am happy today but was sad yesterday","I am happy today but was sorrow yesterday","I am joy today but was sad yesterday","I am joy today but was sorrow yesterday"]
    ,
    # example 2
    [[["happy", "joy"], ["cheerful", "glad"]], "I am happy today but was sad yesterday"]
    # output: ["I am happy today but was sad yesterday","I am joy today but was sad yesterday"]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### generateSentences 
from collections import defaultdict
from typing import *
def f_gold(synonyms: List[List[str]], text: str) -> List[str]:
    p = {}
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    for a, b in synonyms:
        p[a] = a
        p[b] = b
    for a, b in synonyms:
        p[find(a)] = find(b)
    s = defaultdict(set)
    for a, b in synonyms:
        s[find(a)].add(a)
        s[find(b)].add(b)
    res = []
    for word in text.split(' '):
        if word not in p:
            if not res:
                res.append([word])
            else:
                for a in res:
                    a.append(word)
        else:
            words = sorted(s[find(word)])
            if not res:
                for b in words:
                    res.append([b])
            else:
                res = [a + [b] for a in res for b in words]
    return [' '.join(sentence) for sentence in res]
"-----------------"
test()

