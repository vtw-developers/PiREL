from L2323_FindMinimumTimetoFinishAllJobsII import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[5, 2, 4], [1, 7, 5]]
    # output: 2
    # EXPLANATION:  - Assign the 2<sup>nd</sup> worker to the 0<sup>th</sup> job. It takes them 1 day to finish the job. - Assign the 0<sup>th</sup> worker to the 1<sup>st</sup> job. It takes them 2 days to finish the job. - Assign the 1<sup>st</sup> worker to the 2<sup>nd</sup> job. It takes them 1 day to finish the job. It takes 2 days for all the jobs to be completed, so return 2. It can be proven that 2 days is the minimum number of days needed.
    ,
    # example 2
    [[3, 18, 15, 9], [6, 5, 1, 3]]
    # output: 3
    # EXPLANATION:  - Assign the 2<sup>nd</sup> worker to the 0<sup>th</sup> job. It takes them 3 days to finish the job. - Assign the 0<sup>th</sup> worker to the 1<sup>st</sup> job. It takes them 3 days to finish the job. - Assign the 1<sup>st</sup> worker to the 2<sup>nd</sup> job. It takes them 3 days to finish the job. - Assign the 3<sup>rd</sup> worker to the 3<sup>rd</sup> job. It takes them 3 days to finish the job. It takes 3 days for all the jobs to be completed, so return 3. It can be proven that 3 days is the minimum number of days needed.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
