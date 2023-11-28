
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


"-----------------"
### watchedVideosByFriends 
from collections import deque
from collections import Counter
from typing import *
def f_gold(watchedVideos: List[List[str]],
    friends: List[List[int]],
    id: int,
    level: int,
) -> List[str]:
    n = len(friends)
    vis = [False] * n
    q = deque([id])
    vis[id] = True
    for _ in range(level):
        size = len(q)
        for _ in range(size):
            u = q.popleft()
            for v in friends[u]:
                if not vis[v]:
                    q.append(v)
                    vis[v] = True
    freq = Counter()
    for _ in range(len(q)):
        u = q.pop()
        for w in watchedVideos[u]:
            freq[w] += 1
    videos = list(freq.items())
    videos.sort(key=lambda x: (x[1], x[0]))
    return [v[0] for v in videos]
"-----------------"
test()

