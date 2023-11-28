
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["(name)is(age)yearsold", [["name", "bob"], ["age", "two"]]]
    # output: "bobistwoyearsold"
    # EXPLANATION:  The key "name" has a value of "bob", so replace "(name)" with "bob". The key "age" has a value of "two", so replace "(age)" with "two".
    ,
    # example 2
    ["hi(name)", [["a", "b"]]]
    # output: "hi?"
    # EXPLANATION:  As you do not know the value of the key "name", replace "(name)" with "?".
    ,
    # example 3
    ["(a)(a)(a)aaa", [["a", "yes"]]]
    # output: "yesyesyesaaa"
    # EXPLANATION:  The same key can appear multiple times. The key "a" has a value of "yes", so replace all occurrences of "(a)" with "yes". Notice that the "a"s not in a bracket pair are not evaluated.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### evaluate 
from typing import *
def f_gold(s: str, knowledge: List[List[str]]) -> str:
    def find_right_bracket(s, start, end):
        for i in range(start, end):
            if s[i] == ')':
                return i
    knowledge_dict = {item[0]: item[1] for item in knowledge}
    res, n = [], len(s)
    i = 0
    while i < n:
        if s[i] == '(':
            right_bracket_pos = find_right_bracket(s, i + 1, n)
            key = s[i + 1 : right_bracket_pos]
            res.append(knowledge_dict.get(key, '?'))
            i = right_bracket_pos + 1
        else:
            res.append(s[i])
            i += 1
    return ''.join(res)
"-----------------"
test()

