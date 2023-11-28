from L1860_IncrementalMemoryLeak import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2, 2]
    # output: [3,1,0]
    # EXPLANATION:  The memory is allocated as follows: - At the 1<sup>st</sup> second, 1 bit of memory is allocated to stick 1. The first stick now has 1 bit of available memory. - At the 2<sup>nd</sup> second, 2 bits of memory are allocated to stick 2. The second stick now has 0 bits of available memory. - At the 3<sup>rd</sup> second, the program crashes. The sticks have 1 and 0 bits available respectively.
    ,
    # example 2
    [8, 11]
    # output: [6,0,4]
    # EXPLANATION:  The memory is allocated as follows: - At the 1<sup>st</sup> second, 1 bit of memory is allocated to stick 2. The second stick now has 10 bit of available memory. - At the 2<sup>nd</sup> second, 2 bits of memory are allocated to stick 2. The second stick now has 8 bits of available memory. - At the 3<sup>rd</sup> second, 3 bits of memory are allocated to stick 1. The first stick now has 5 bits of available memory. - At the 4<sup>th</sup> second, 4 bits of memory are allocated to stick 2. The second stick now has 4 bits of available memory. - At the 5<sup>th</sup> second, 5 bits of memory are allocated to stick 1. The first stick now has 0 bits of available memory. - At the 6<sup>th</sup> second, the program crashes. The sticks have 0 and 4 bits available respectively.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
