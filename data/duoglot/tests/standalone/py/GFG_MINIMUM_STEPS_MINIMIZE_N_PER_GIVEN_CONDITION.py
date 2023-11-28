def test():
  "--- test function ---"
  param =[(59,),(7,),(90,),(78,),(49,),(15,),(45,),(56,),(7,),(70,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  table =[0] *(n + 1)
  for i in range(n + 1): table[i] = n - i
  for i in range(n, 0, - 1):
    if(not(i % 2)): table[i // 2] = min(table[i] + 1, table[i // 2])
    if(not(i % 3)): table[i // 3] = min(table[i] + 1, table[i // 3])
  return table[1]
"-----------------"
test()
