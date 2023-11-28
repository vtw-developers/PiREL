
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


"-----------------"
### findSubstring 
from collections import Counter
from typing import *
def f_gold(s: str, words: List[str]) -> List[int]:
    cnt = Counter(words)
    sublen = len(words[0])
    n, m = len(s), len(words)
    ans = []
    for i in range(sublen):
        cnt1 = Counter()
        l = r = i
        t = 0
        while r + sublen <= n:
            w = s[r : r + sublen]
            r += sublen
            if w not in cnt:
                l = r
                cnt1.clear()
                t = 0
                continue
            cnt1[w] += 1
            t += 1
            while cnt1[w] > cnt[w]:
                remove = s[l : l + sublen]
                l += sublen
                cnt1[remove] -= 1
                t -= 1
            if m == t:
                ans.append(l)
    return ans
"-----------------"
test()

