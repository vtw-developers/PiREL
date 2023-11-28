def test():
  "--- test function ---"
  param =[('nObYIOjEQZ', 'uARTDTQbmGI',),('84574', '8538229',),('1010001010010', '11',),('DjZtAfUudk', 'OewGm',),('550', '132744553919',),('1110', '0101',),('GywyxwH', 'LPQqEqrDZiwY',),('67318370914755', '9928',),('11011000000101', '00000',),('G', 'V',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(s, t):
  count = 0
  for i in range(0, len(t)):
    if(count == len(s)): break
    if(t[i] == s[count]): count = count + 1
  return count
"-----------------"
test()
