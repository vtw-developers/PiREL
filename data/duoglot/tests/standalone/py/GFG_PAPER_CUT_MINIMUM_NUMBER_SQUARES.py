def test():
  "--- test function ---"
  param =[(87, 60,),(18, 35,),(68, 93,),(80, 20,),(87, 69,),(64, 29,),(64, 1,),(65, 95,),(43, 72,),(97, 41,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(a, b):
  result = 0
  rem = 0
  if(a < b): a, b = b, a
  while(b > 0):
    result += int(a / b)
    rem = int(a % b)
    a = b
    b = rem
  return result
"-----------------"
test()
