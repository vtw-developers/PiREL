
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["<DIV>This is the first line <![CDATA[<div>]]></DIV>"]
    # output: true
    # EXPLANATION:   The code is wrapped in a closed tag : <DIV> and </DIV>.  The TAG_NAME is valid, the TAG_CONTENT consists of some characters and cdata.  Although CDATA_CONTENT has an unmatched start tag with invalid TAG_NAME, it should be considered as plain text, not parsed as a tag. So TAG_CONTENT is valid, and then the code is valid. Thus return true.
    ,
    # example 2
    ["<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"]
    # output: true
    # EXPLANATION:  We first separate the code into : start_tag|tag_content|end_tag. start_tag -> <b>"<DIV>"</b> end_tag -> <b>"</DIV>"</b> tag_content could also be separated into : text1|cdata|text2. text1 -> <b>">>  ![cdata[]] "</b> cdata -> <b>"<![CDATA[<div>]>]]>"</b>, where the CDATA_CONTENT is <b>"<div>]>"</b> text2 -> <b>"]]>>]"</b> The reason why start_tag is NOT <b>"<DIV>>>"</b> is because of the rule 6. The reason why cdata is NOT <b>"<![CDATA[<div>]>]]>]]>"</b> is because of the rule 7.
    ,
    # example 3
    ["<A>  <B> </A>   </B>"]
    # output: false
    # EXPLANATION:  Unbalanced. If "<A>" is closed, then "<B>" must be unmatched, and vice versa.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### isValid 
from typing import *
def f_gold(code: str) -> bool:
    def check(tag):
        return 1 <= len(tag) <= 9 and all(c.isupper() for c in tag)
    stk = []
    i, n = 0, len(code)
    while i < n:
        if i and not stk:
            return False
        if code[i : i + 9] == '<![CDATA[':
            i = code.find(']]>', i + 9)
            if i < 0:
                return False
            i += 2
        elif code[i : i + 2] == '</':
            j = i + 2
            i = code.find('>', j)
            if i < 0:
                return False
            t = code[j:i]
            if not check(t) or not stk or stk.pop() != t:
                return False
        elif code[i] == '<':
            j = i + 1
            i = code.find('>', j)
            if i < 0:
                return False
            t = code[j:i]
            if not check(t):
                return False
            stk.append(t)
        i += 1
    return not stk
"-----------------"
test()

