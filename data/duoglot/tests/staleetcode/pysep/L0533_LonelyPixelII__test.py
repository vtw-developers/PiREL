from L0533_LonelyPixelII import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[["W", "B", "W", "B", "B", "W"], ["W", "B", "W", "B", "B", "W"], ["W", "B", "W", "B", "B", "W"], ["W", "W", "B", "W", "B", "W"]], 3]
    # output: 6
    # EXPLANATION:  All the green 'B' are the black pixels we need (all 'B's at column 1 and 3). Take 'B' at row r = 0 and column c = 1 as an example:  - Rule 1, row r = 0 and column c = 1 both have exactly target = 3 black pixels.   - Rule 2, the rows have black pixel at column c = 1 are row 0, row 1 and row 2. They are exactly the same as row r = 0.
    ,
    # example 2
    [[["W", "W", "B"], ["W", "W", "B"], ["W", "W", "B"]], 1]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
