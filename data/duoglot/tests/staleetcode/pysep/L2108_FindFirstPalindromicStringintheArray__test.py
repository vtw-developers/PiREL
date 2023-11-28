from L2108_FindFirstPalindromicStringintheArray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["abc", "car", "ada", "racecar", "cool"]]
    # output: "ada"
    # EXPLANATION:  The first string that is palindromic is "ada". Note that "racecar" is also palindromic, but it is not the first.
    ,
    # example 2
    [["notapalindrome", "racecar"]]
    # output: "racecar"
    # EXPLANATION:  The first and only string that is palindromic is "racecar".
    ,
    # example 3
    [["def", "ghi"]]
    # output: ""
    # EXPLANATION:  There are no palindromic strings, so the empty string is returned.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
