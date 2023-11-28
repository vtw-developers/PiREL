from L1807_EvaluatetheBracketPairsofaString import f_gold

##########
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

##########

test()
