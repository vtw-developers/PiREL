def test():
  "--- test function ---"
  param =[(76, 43,),(96, 52,),(19, 79,),(36, 2,),(60, 11,),(20, 15,),(76, 4,),(63, 93,),(2, 25,),(41, 39,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(low, high):
  f1, f2, f3 = 0, 1, 1
  result = 0
  while(f1 <= high):
    if(f1 >= low): result += 1
    f1 = f2
    f2 = f3
    f3 = f1 + f2
  return result
"-----------------"
test()
