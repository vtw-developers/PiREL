from L2161_PartitionArrayAccordingtoGivenPivot import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[9, 12, 5, 10, 14, 3, 10], 10]
    # output: [9,5,3,10,10,12,14]
    # EXPLANATION:   The elements 9, 5, and 3 are less than the pivot so they are on the left side of the array. The elements 12 and 14 are greater than the pivot so they are on the right side of the array. The relative ordering of the elements less than and greater than pivot is also maintained. [9, 5, 3] and [12, 14] are the respective orderings.
    ,
    # example 2
    [[-3, 4, 3, 2], 2]
    # output: [-3,2,4,3]
    # EXPLANATION:   The element -3 is less than the pivot so it is on the left side of the array. The elements 4 and 3 are greater than the pivot so they are on the right side of the array. The relative ordering of the elements less than and greater than pivot is also maintained. [-3] and [4, 3] are the respective orderings.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
