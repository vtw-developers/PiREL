from L1311_GetWatchedVideosbyYourFriends import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[["A", "B"], ["C"], ["B", "C"], ["D"]], [[1, 2], [0, 3], [0, 3], [1, 2]], 0, 1]
    # output: ["B","C"]
    # EXPLANATION:   You have id = 0 (green color in the figure) and your friends are (yellow color in the figure): Person with id = 1 -> watchedVideos = ["C"]  Person with id = 2 -> watchedVideos = ["B","C"]  The frequencies of watchedVideos by your friends are:  B -> 1  C -> 2
    ,
    # example 2
    [[["A", "B"], ["C"], ["B", "C"], ["D"]], [[1, 2], [0, 3], [0, 3], [1, 2]], 0, 2]
    # output: ["D"]
    # EXPLANATION:   You have id = 0 (green color in the figure) and the only friend of your friends is the person with id = 3 (yellow color in the figure).
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
