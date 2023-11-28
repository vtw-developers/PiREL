def test():
  "--- test function ---"
  param =[(8,),(96,),(96,),(96,),(12,),(95,),(72,),(81,),(42,),(13,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(s):
  length = int(s / 3)
  s -= length
  breadth = s / 2
  height = s - breadth
  return int(length * breadth * height)
"-----------------"
test()
