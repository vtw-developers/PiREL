from L2283_CheckifNumberHasEqualDigitCountandDigitValue import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["1210"]
    # output: true
    # EXPLANATION:  num[0] = '1'. The digit 0 occurs once in num. num[1] = '2'. The digit 1 occurs twice in num. num[2] = '1'. The digit 2 occurs once in num. num[3] = '0'. The digit 3 occurs zero times in num. The condition holds true for every index in "1210", so return true.
    ,
    # example 2
    ["030"]
    # output: false
    # EXPLANATION:  num[0] = '0'. The digit 0 should occur zero times, but actually occurs twice in num. num[1] = '3'. The digit 1 should occur three times, but actually occurs zero times in num. num[2] = '0'. The digit 2 occurs zero times in num. The indices 0 and 1 both violate the condition, so return false.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
