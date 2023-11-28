
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["1s3 PSt", ["step", "steps", "stripe", "stepple"]]
    # output: "steps"
    # EXPLANATION:  licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'. "step" contains 't' and 'p', but only contains 1 's'. "steps" contains 't', 'p', and both 's' characters. "stripe" is missing an 's'. "stepple" is missing an 's'. Since "steps" is the only word containing all the letters, that is the answer.
    ,
    # example 2
    ["1s3 456", ["looks", "pest", "stew", "show"]]
    # output: "pest"
    # EXPLANATION:  licensePlate only contains the letter 's'. All the words contain 's', but among these "pest", "stew", and "show" are shortest. The answer is "pest" because it is the word that appears earliest of the 3.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### shortestCompletingWord 
from typing import *
def f_gold(licensePlate: str, words: List[str]) -> str:
    def count(word):
        counter = [0] * 26
        for c in word:
            counter[ord(c) - ord('a')] += 1
        return counter
    def check(counter1, counter2):
        for i in range(26):
            if counter1[i] > counter2[i]:
                return False
        return True
    counter = count(c.lower() for c in licensePlate if c.isalpha())
    ans, n = None, 16
    for word in words:
        if n <= len(word):
            continue
        t = count(word)
        if check(counter, t):
            n = len(word)
            ans = word
    return ans
"-----------------"
test()

