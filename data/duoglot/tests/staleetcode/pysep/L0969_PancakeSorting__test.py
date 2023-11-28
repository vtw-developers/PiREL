from L0969_PancakeSorting import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 2, 4, 1]]
    # output: [4,2,4,3]
    # EXPLANATION:  We perform 4 pancake flips, with k values 4, 2, 4, and 3. Starting state: arr = [3, 2, 4, 1] After 1st flip (k = 4): arr = [<u>1</u>, <u>4</u>, <u>2</u>, <u>3</u>] After 2nd flip (k = 2): arr = [<u>4</u>, <u>1</u>, 2, 3] After 3rd flip (k = 4): arr = [<u>3</u>, <u>2</u>, <u>1</u>, <u>4</u>] After 4th flip (k = 3): arr = [<u>1</u>, <u>2</u>, <u>3</u>, 4], which is sorted.
    ,
    # example 2
    [[1, 2, 3]]
    # output: []
    # EXPLANATION: The input is already sorted, so there is no need to flip anything. Note that other answers, such as [3, 3], would also be accepted.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
