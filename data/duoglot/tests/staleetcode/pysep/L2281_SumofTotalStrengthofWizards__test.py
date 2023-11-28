from L2281_SumofTotalStrengthofWizards import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 3, 1, 2]]
    # output: 44
    # EXPLANATION:  The following are all the contiguous groups of wizards: - [1] from [<u><strong>1</strong></u>,3,1,2] has a total strength of min([1]) * sum([1]) = 1 * 1 = 1 - [3] from [1,<u><strong>3</strong></u>,1,2] has a total strength of min([3]) * sum([3]) = 3 * 3 = 9 - [1] from [1,3,<u><strong>1</strong></u>,2] has a total strength of min([1]) * sum([1]) = 1 * 1 = 1 - [2] from [1,3,1,<u><strong>2</strong></u>] has a total strength of min([2]) * sum([2]) = 2 * 2 = 4 - [1,3] from [<u><strong>1,3</strong></u>,1,2] has a total strength of min([1,3]) * sum([1,3]) = 1 * 4 = 4 - [3,1] from [1,<u><strong>3,1</strong></u>,2] has a total strength of min([3,1]) * sum([3,1]) = 1 * 4 = 4 - [1,2] from [1,3,<u><strong>1,2</strong></u>] has a total strength of min([1,2]) * sum([1,2]) = 1 * 3 = 3 - [1,3,1] from [<u><strong>1,3,1</strong></u>,2] has a total strength of min([1,3,1]) * sum([1,3,1]) = 1 * 5 = 5 - [3,1,2] from [1,<u><strong>3,1,2</strong></u>] has a total strength of min([3,1,2]) * sum([3,1,2]) = 1 * 6 = 6 - [1,3,1,2] from [<u><strong>1,3,1,2</strong></u>] has a total strength of min([1,3,1,2]) * sum([1,3,1,2]) = 1 * 7 = 7 The sum of all the total strengths is 1 + 9 + 1 + 4 + 4 + 4 + 3 + 5 + 6 + 7 = 44.
    ,
    # example 2
    [[5, 4, 6]]
    # output: 213
    # EXPLANATION:  The following are all the contiguous groups of wizards:  - [5] from [<u><strong>5</strong></u>,4,6] has a total strength of min([5]) * sum([5]) = 5 * 5 = 25 - [4] from [5,<u><strong>4</strong></u>,6] has a total strength of min([4]) * sum([4]) = 4 * 4 = 16 - [6] from [5,4,<u><strong>6</strong></u>] has a total strength of min([6]) * sum([6]) = 6 * 6 = 36 - [5,4] from [<u><strong>5,4</strong></u>,6] has a total strength of min([5,4]) * sum([5,4]) = 4 * 9 = 36 - [4,6] from [5,<u><strong>4,6</strong></u>] has a total strength of min([4,6]) * sum([4,6]) = 4 * 10 = 40 - [5,4,6] from [<u><strong>5,4,6</strong></u>] has a total strength of min([5,4,6]) * sum([5,4,6]) = 4 * 15 = 60 The sum of all the total strengths is 25 + 16 + 36 + 36 + 40 + 60 = 213.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
