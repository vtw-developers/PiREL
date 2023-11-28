def test():
  "--- test function ---"
  param =[(37,),(25,),(63,),(66,),(32,),(5,),(41,),(82,),(54,),(5,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  num = n ;
  dec_value = 0 ;
  base = 1 ;
  temp = num ;
  while(temp): last_digit = temp % 10 ; temp = int(temp / 10); dec_value += last_digit * base ; base = base * 8 ;
  return dec_value ;
"-----------------"
test()
