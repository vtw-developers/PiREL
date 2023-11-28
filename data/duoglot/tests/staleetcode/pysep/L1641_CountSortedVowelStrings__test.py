from L1641_CountSortedVowelStrings import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1]
    # output: 5
    # EXPLANATION:  The 5 sorted strings that consist of vowels only are <code>["a","e","i","o","u"].</code>
    ,
    # example 2
    [2]
    # output: 15
    # EXPLANATION:  The 15 sorted strings that consist of vowels only are ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"]. Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
    ,
    # example 3
    [33]
    # output: 66045
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
