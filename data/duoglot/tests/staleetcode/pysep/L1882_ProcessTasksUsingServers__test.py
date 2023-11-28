from L1882_ProcessTasksUsingServers import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 3, 2], [1, 2, 3, 2, 1, 2]]
    # output: [2,2,0,2,1,2]
    # EXPLANATION: Events in chronological order go as follows: - At second 0, task 0 is added and processed using server 2 until second 1. - At second 1, server 2 becomes free. Task 1 is added and processed using server 2 until second 3. - At second 2, task 2 is added and processed using server 0 until second 5. - At second 3, server 2 becomes free. Task 3 is added and processed using server 2 until second 5. - At second 4, task 4 is added and processed using server 1 until second 5. - At second 5, all servers become free. Task 5 is added and processed using server 2 until second 7.
    ,
    # example 2
    [[5, 1, 4, 3, 2], [2, 1, 2, 4, 5, 2, 1]]
    # output: [1,4,1,4,1,3,2]
    # EXPLANATION: Events in chronological order go as follows:  - At second 0, task 0 is added and processed using server 1 until second 2. - At second 1, task 1 is added and processed using server 4 until second 2. - At second 2, servers 1 and 4 become free. Task 2 is added and processed using server 1 until second 4.  - At second 3, task 3 is added and processed using server 4 until second 7. - At second 4, server 1 becomes free. Task 4 is added and processed using server 1 until second 9.  - At second 5, task 5 is added and processed using server 3 until second 7. - At second 6, task 6 is added and processed using server 2 until second 7.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
