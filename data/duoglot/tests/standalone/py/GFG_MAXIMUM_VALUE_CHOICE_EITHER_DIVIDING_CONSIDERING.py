def test():
  "--- test function ---"
  param =[(3,),(19,),(39,),(89,),(96,),(68,),(48,),(5,),(3,),(4,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  res = list()
  res.append(0)
  res.append(1)
  i = 2
  while i < n + 1:
    res.append(max(i,(res[int(i / 2)] + res[int(i / 3)] + res[int(i / 4)] + res[int(i / 5)])))
    i = i + 1
  return res[n]
"-----------------"
test()
