def test():
  "--- test function ---"
  param =[(69,),(72,),(88,),(7,),(66,),(34,),(23,),(37,),(33,),(21,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  result = 0
  for i in range(1, 10):
    s =[]
    if(i <= n):
      s.append(i)
      result += 1
    while len(s)!= 0:
      tp = s[- 1]
      s.pop()
      for j in range(tp % 10, 10):
        x = tp * 10 + j
        if(x <= n):
          s.append(x)
          result += 1
  return result
"-----------------"
test()
