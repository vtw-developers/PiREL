from L0008_StringtoInteger_atoi_ import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["42"]
    # output: 42
    # EXPLANATION:  The underlined characters are what is read in, the caret is the current reader position. Step 1: "42" (no characters read because there is no leading whitespace)          ^ Step 2: "42" (no characters read because there is neither a '-' nor '+')          ^ Step 3: "<u>42</u>" ("42" is read in)            ^ The parsed integer is 42. Since 42 is in the range [-2<sup>31</sup>, 2<sup>31</sup> - 1], the final result is 42.
    ,
    # example 2
    ["   -42"]
    # output: -42
    # EXPLANATION:  Step 1: "<u>   </u>-42" (leading whitespace is read and ignored)             ^ Step 2: "   <u>-</u>42" ('-' is read, so the result should be negative)              ^ Step 3: "   -<u>42</u>" ("42" is read in)                ^ The parsed integer is -42. Since -42 is in the range [-2<sup>31</sup>, 2<sup>31</sup> - 1], the final result is -42.
    ,
    # example 3
    ["4193 with words"]
    # output: 4193
    # EXPLANATION:  Step 1: "4193 with words" (no characters read because there is no leading whitespace)          ^ Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')          ^ Step 3: "<u>4193</u> with words" ("4193" is read in; reading stops because the next character is a non-digit)              ^ The parsed integer is 4193. Since 4193 is in the range [-2<sup>31</sup>, 2<sup>31</sup> - 1], the final result is 4193.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
