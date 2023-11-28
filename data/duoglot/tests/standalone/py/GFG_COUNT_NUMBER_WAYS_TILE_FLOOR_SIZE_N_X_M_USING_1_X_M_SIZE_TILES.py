def test():
  "--- test function ---"
  param =[(93, 54,),(17, 4,),(38, 39,),(33, 64,),(78, 35,),(40, 61,),(95, 6,),(12, 8,),(69, 60,),(78, 21,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n, m):
  count =[]
  for i in range(n + 2): count.append(0)
  count[0] = 0
  for i in range(1, n + 1):
    if(i > m): count[i] = count[i - 1] + count[i - m]
    elif(i < m): count[i] = 1
    else: count[i] = 2
  return count[n]
"-----------------"
test()
