
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


"-----------------"
### fullJustify 
from typing import *
def f_gold(words: List[str], maxWidth: int) -> List[str]:
    def partition(n, cnt):
        res = []
        base, mod = divmod(n, cnt)
        i = j = 0
        while i < cnt:
            t = [' ' * base]
            if j < mod:
                t.append(' ')
            res.append(''.join(t))
            i, j = i + 1, j + 1
        return res
    ans = []
    i, n = 0, len(words)
    while i < n:
        t = []
        cnt = len(words[i])
        t.append(words[i])
        i += 1
        while i < n and cnt + 1 + len(words[i]) <= maxWidth:
            cnt += 1 + len(words[i])
            t.append(words[i])
            i += 1
        if i == n or len(t) == 1:
            # this is the last line or only one word in a line
            left = ' '.join(t)
            right = ' ' * (maxWidth - len(left))
            ans.append(left + right)
            if i == n:
                break
            continue
        words_width = cnt - len(t) + 1
        space_width = maxWidth - words_width
        spaces = partition(space_width, len(t) - 1)
        sb = [t[0]]
        for j in range(len(t) - 1):
            sb.append(spaces[j])
            sb.append(t[j + 1])
        ans.append(''.join(sb))
    return ans
"-----------------"
test()

