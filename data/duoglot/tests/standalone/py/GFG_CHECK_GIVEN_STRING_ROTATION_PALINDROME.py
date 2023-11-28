def test():
  "--- test function ---"
  param =[('aadaa',),('2674377254',),('11',),('0011000',),('26382426486138',),('111010111010',),('abccba',),('5191',),('1110101101',),('abcdecbe',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(string):
  l = 0
  h = len(string)- 1
  while h > l:
    l += 1
    h -= 1
    if string[l - 1] != string[h + 1]: return False
  return True
"-----------------"
test()
