from L0599_MinimumIndexSumofTwoLists import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]]
    # output: ["Shogun"]
    # EXPLANATION:  The only restaurant they both like is "Shogun".
    ,
    # example 2
    [["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"]]
    # output: ["Shogun"]
    # EXPLANATION:  The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
