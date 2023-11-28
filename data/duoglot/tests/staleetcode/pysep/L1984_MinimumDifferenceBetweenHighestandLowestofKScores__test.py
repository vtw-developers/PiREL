from L1984_MinimumDifferenceBetweenHighestandLowestofKScores import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[90], 1]
    # output: 0
    # EXPLANATION:  There is one way to pick score(s) of one student: - [<strong><u>90</u></strong>]. The difference between the highest and lowest score is 90 - 90 = 0. The minimum possible difference is 0.
    ,
    # example 2
    [[9, 4, 1, 7], 2]
    # output: 2
    # EXPLANATION:  There are six ways to pick score(s) of two students: - [<strong><u>9</u></strong>,<strong><u>4</u></strong>,1,7]. The difference between the highest and lowest score is 9 - 4 = 5. - [<strong><u>9</u></strong>,4,<strong><u>1</u></strong>,7]. The difference between the highest and lowest score is 9 - 1 = 8. - [<strong><u>9</u></strong>,4,1,<strong><u>7</u></strong>]. The difference between the highest and lowest score is 9 - 7 = 2. - [9,<strong><u>4</u></strong>,<strong><u>1</u></strong>,7]. The difference between the highest and lowest score is 4 - 1 = 3. - [9,<strong><u>4</u></strong>,1,<strong><u>7</u></strong>]. The difference between the highest and lowest score is 7 - 4 = 3. - [9,4,<strong><u>1</u></strong>,<strong><u>7</u></strong>]. The difference between the highest and lowest score is 7 - 1 = 6. The minimum possible difference is 2.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
