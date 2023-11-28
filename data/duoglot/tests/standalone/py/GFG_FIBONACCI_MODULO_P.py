def test():
  "--- test function ---"
  param =[(51,),(40,),(68,),(7,),(8,),(32,),(93,),(75,),(71,),(15,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(p):
  first = 1
  second = 1
  number = 2
  next = 1
  while(next):
    next =(first + second)% p
    first = second
    second = next
    number = number + 1
  return number
"-----------------"
test()
