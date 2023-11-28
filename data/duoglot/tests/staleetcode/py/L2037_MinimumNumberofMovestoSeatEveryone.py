
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 1, 5], [2, 7, 4]]
    # output: 4
    # EXPLANATION:  The students are moved as follows: - The first student is moved from from position 2 to position 1 using 1 move. - The second student is moved from from position 7 to position 5 using 2 moves. - The third student is moved from from position 4 to position 3 using 1 move. In total, 1 + 2 + 1 = 4 moves were used.
    ,
    # example 2
    [[4, 1, 5, 9], [1, 3, 2, 6]]
    # output: 7
    # EXPLANATION:  The students are moved as follows: - The first student is not moved. - The second student is moved from from position 3 to position 4 using 1 move. - The third student is moved from from position 2 to position 5 using 3 moves. - The fourth student is moved from from position 6 to position 9 using 3 moves. In total, 0 + 1 + 3 + 3 = 7 moves were used.
    ,
    # example 3
    [[2, 2, 6, 6], [1, 3, 2, 6]]
    # output: 4
    # EXPLANATION:  Note that there are two seats at position 2 and two seats at position 6. The students are moved as follows: - The first student is moved from from position 1 to position 2 using 1 move. - The second student is moved from from position 3 to position 6 using 3 moves. - The third student is not moved. - The fourth student is not moved. In total, 1 + 3 + 0 + 0 = 4 moves were used.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minMovesToSeat 
from typing import *
def f_gold(seats: List[int], students: List[int]) -> int:
    seats.sort()
    students.sort()
    return sum(abs(seats[i] - students[i]) for i in range(len(seats)))
"-----------------"
test()

