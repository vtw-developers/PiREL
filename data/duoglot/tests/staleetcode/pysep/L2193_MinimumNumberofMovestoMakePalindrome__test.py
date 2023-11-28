from L2193_MinimumNumberofMovestoMakePalindrome import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["aabb"]
    # output: 2
    # EXPLANATION:  We can obtain two palindromes from s, "abba" and "baab".  - We can obtain "abba" from s in 2 moves: "a<u><strong>ab</strong></u>b" -> "ab<u><strong>ab</strong></u>" -> "abba". - We can obtain "baab" from s in 2 moves: "a<u><strong>ab</strong></u>b" -> "<u><strong>ab</strong></u>ab" -> "baab". Thus, the minimum number of moves needed to make s a palindrome is 2.
    ,
    # example 2
    ["letelt"]
    # output: 2
    # EXPLANATION:  One of the palindromes we can obtain from s in 2 moves is "lettel". One of the ways we can obtain it is "lete<u><strong>lt</strong></u>" -> "let<u><strong>et</strong></u>l" -> "lettel". Other palindromes such as "tleelt" can also be obtained in 2 moves. It can be shown that it is not possible to obtain a palindrome in less than 2 moves.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
