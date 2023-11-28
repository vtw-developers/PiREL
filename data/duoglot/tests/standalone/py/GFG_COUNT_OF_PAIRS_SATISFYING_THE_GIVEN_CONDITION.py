def test():
  "--- test function ---"
  param =[(31, 91,),(72, 85,),(23, 49,),(42, 32,),(13, 7,),(93, 5,),(33, 32,),(94, 76,),(60, 60,),(11, 26,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(a, b):
  s = str(b)
  i = 0
  while i <(len(s)):
    if(s[i] != '9'): break
    i += 1
  result = 0
  if(i == len(s)): result = a * len(s)
  else: result = a *(len(s)- 1)
  return result
"-----------------"
test()
