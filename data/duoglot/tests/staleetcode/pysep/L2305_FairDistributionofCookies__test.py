from L2305_FairDistributionofCookies import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[8, 15, 10, 20, 8], 2]
    # output: 31
    # EXPLANATION:  One optimal distribution is [8,15,8] and [10,20] - The 1<sup>st</sup> child receives [8,15,8] which has a total of 8 + 15 + 8 = 31 cookies. - The 2<sup>nd</sup> child receives [10,20] which has a total of 10 + 20 = 30 cookies. The unfairness of the distribution is max(31,30) = 31. It can be shown that there is no distribution with an unfairness less than 31.
    ,
    # example 2
    [[6, 1, 3, 2, 2, 4, 1, 2], 3]
    # output: 7
    # EXPLANATION:  One optimal distribution is [6,1], [3,2,2], and [4,1,2] - The 1<sup>st</sup> child receives [6,1] which has a total of 6 + 1 = 7 cookies. - The 2<sup>nd</sup> child receives [3,2,2] which has a total of 3 + 2 + 2 = 7 cookies. - The 3<sup>rd</sup> child receives [4,1,2] which has a total of 4 + 1 + 2 = 7 cookies. The unfairness of the distribution is max(7,7,7) = 7. It can be shown that there is no distribution with an unfairness less than 7.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
