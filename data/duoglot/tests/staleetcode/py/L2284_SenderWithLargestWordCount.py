
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["Hello userTwooo", "Hi userThree", "Wonderful day Alice", "Nice day userThree"], ["Alice", "userTwo", "userThree", "Alice"]]
    # output: "Alice"
    # EXPLANATION:  Alice sends a total of 2 + 3 = 5 words. userTwo sends a total of 2 words. userThree sends a total of 3 words. Since Alice has the largest word count, we return "Alice".
    ,
    # example 2
    [["How is leetcode for everyone", "Leetcode is useful for practice"], ["Bob", "Charlie"]]
    # output: "Charlie"
    # EXPLANATION:  Bob sends a total of 5 words. Charlie sends a total of 5 words. Since there is a tie for the largest word count, we return the sender with the lexicographically larger name, Charlie.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### largestWordCount 
from collections import Counter
from typing import *
def f_gold(messages: List[str], senders: List[str]) -> str:
    cnt = Counter()
    for m, s in zip(messages, senders):
        cnt[s] += m.count(' ') + 1
    return sorted(cnt.items(), key=lambda x: (x[1], x[0]))[-1][0]
"-----------------"
test()

