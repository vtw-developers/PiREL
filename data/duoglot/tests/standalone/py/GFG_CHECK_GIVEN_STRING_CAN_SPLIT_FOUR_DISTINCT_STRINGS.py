def test():
  "--- test function ---"
  param =[('WKTj Nw',),('8235021',),('0101',),('BLMhiQsQcFla',),('00363175722',),('10000',),('aqEYWNd bqgye',),('83',),('000011110111',),('E',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(s):
  if(len(s)>= 10): return True
  for i in range(1, len(s)):
    for j in range(i + 1, len(s)):
      for k in range(j + 1, len(s)):
        s1 = s[0: i]
        s2 = s[i: j - i]
        s3 = s[j: k - j]
        s4 = s[k: len(s)- k]
        if(s1 != s2 and s1 != s3 and s1 != s4 and s2 != s3 and s2 != s4 and s3 != s4): return True
  return False
"-----------------"
test()
