from L0591_TagValidator import f_gold

##########
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

##########

test()
