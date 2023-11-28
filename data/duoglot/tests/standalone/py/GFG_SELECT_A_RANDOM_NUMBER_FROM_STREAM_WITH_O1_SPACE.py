def test():
  "--- test function ---"
  param =[(64,),(36,),(21,),(3,),(18,),(82,),(76,),(99,),(70,),(31,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(x):
  res = 0 ;
  count = 0 ;
  count += 1 ;
  if(count == 1): res = x ;
  else:
    i = random.randrange(count);
    if(i == count - 1): res = x ;
  return res ;
"-----------------"
test()
