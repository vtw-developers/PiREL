def test():
  "--- test function ---"
  param =[(17,),(97,),(73,),(68,),(6,),(84,),(72,),(66,),(57,),(11,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  position = 1
  m = 1
  while(not(n & m)):
    m = m << 1
    position += 1
  return position
"-----------------"
test()
