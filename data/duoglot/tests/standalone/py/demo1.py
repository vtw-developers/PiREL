def test():
  "--- test function ---"
  param = [
    [
      {"alice": ["Earth", 123456, 20], "Bob": ["Earth", 432155, 20], "Eve": ["Mars", 111111, 20]},
      [1, 2, 3],
      (["hello world", "hello bob", "bob hi"], ["BOB", "HELLO", "HI"]),
      ["OaITtzE", "RnYlJUqzk"],
      ["TTFT", "|&^", 4],
      [20, 31, [1, 6, 11, 14, 14, 15, 23, 24, 26, 28, 30, 35, 40, 45, 47, 50, 52, 54, 56, 57, 59, 60, 61, 66, 70, 77, 78, 80, 80, 87, 88, 97]],
      ([9, 30, 49, 65, 78, 85, 85, 92], 4, 4, 5, 4,),
      ["4370992644981", "5", "6"],
    ],
    [
      {"alice": ["Mars", 987, 5], "Bob": ["Mars", 654, 5], "Eve": ["Mars", 765, 3]},
      [0.1, 0.2, 0.3],
      (["a b c d e", "b c d e", "e f g"], ["A", "C", "E", "F"]),
      ["88111031", "558471"],
      ["TFF", "^|", 3],
      [13, 19, [60, 96, 34, 69, 96, 9, 58, 59, 59, 68, 14, 53, 68, 89, 2, 5, 42, 31, 1, 33, 62, 1, 91, 85, 70, 68, 18]],
      ([- 91, - 85, - 77, - 73, - 70, - 68, - 24, - 21, - 12, - 1, 9, 29, 48, 52, 56, 63, 88], 8, 12, 8, 8,),
      ["010110000", "1", "1"],
    ]
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)

"-----------------"

def f_gold(p1, p2, p3, p4, p5, p6, p7, p8):
  return [
    test_closure_and_higher_order(p1),
    multi_func(p2),
    avg_wc(p3[0], p3[1]),
    str_mult(p4[0], p4[1]),
    boolean_parenthesization(p5[0], p5[1], p5[2]),
    print_zigzag(p6[0], p6[1], p6[2]),
    sort_arr_using_poly_expr(p7[0], p7[1], p7[2], p7[3], p7[4]),
    str_slice_concat(p8[0], p8[1], p8[2])
  ]


def test_closure_and_higher_order(data):
  sep = "-"
  def grouping_function(key, val):
    print(key)
    grouping_key_segs = [str(val[0]), str(val[2])]
    return sep.join(grouping_key_segs)
  result = group_by(
    data,
    [grouping_function]
  )
  return result

def group_by(dataset, key_funcs):
    if len(key_funcs) == 0:
        return dataset
    current_func = key_funcs[0]
    rest_funcs = key_funcs[1:]
    temp_list = []
    temp_dict = {}
    for datakey in dataset:
        group_val = current_func(datakey, dataset[datakey])
        if group_val not in temp_dict:
          temp_list.append(group_val)
          temp_dict[group_val] = {}
        temp_dict[group_val][datakey] = dataset[datakey]
    result = [[group_val, group_by(temp_dict[group_val], rest_funcs)] for group_val in temp_list]
    return result


def multi_func(ys):
  def sequence(y):
    return [i * y for i in range(5)]
  
  def squared(y):
    return [x * x for x in sequence(y)]
  
  def exp_func(y, func):
    return [2.71828 ** x for x in func(y)]
  
  return [exp_func(y, squared) for y in ys]


def avg_wc(lines, word_list):
  trwords = [[y.upper() for y in x.split(" ")] for x in lines]
  count_dict = {}
  for line_split in trwords:
    for word in line_split:
      if word in word_list:
        if word not in count_dict: 
          count_dict[word] = 0
          word_list.append(word)
        count_dict[word] += 1
  for i in range(len(word_list)):
    word = word_list[i] 
    msg = "found" if word in count_dict else "not found"
    print(i, word, msg)
  count_sum = 0 
  for word in count_dict: count_sum += count_dict[word]
  return count_sum // len(word_list)


def str_mult(num1, num2):
  len1 = len(num1)
  len2 = len(num2)
  if len1 == 0 or len2 == 0: return "0"
  result =[0] *(len1 + len2)
  i_n1 = 0
  i_n2 = 0
  for i in range(len1 - 1, - 1, - 1):
    carry = 0
    n1 = ord(num1[i])- 48
    i_n2 = 0
    for j in range(len2 - 1, - 1, - 1):
      n2 = ord(num2[j])- 48
      summ = n1 * n2 + result[i_n1 + i_n2] + carry
      carry = summ // 10
      result[i_n1 + i_n2] = summ % 10
      i_n2 += 1
    if(carry > 0): result[i_n1 + i_n2] += carry
    i_n1 += 1
  i = len(result)- 1
  while(i >= 0 and result[i] == 0): i -= 1
  if(i == - 1): return "0"
  s = ""
  while(i >= 0):
    s += chr(result[i] + 48)
    i -= 1
  print("s=", s)
  return s


def boolean_parenthesization(symb, oper, n):
  F =[[0 for i in range(n + 1)] for i in range(n + 1)]
  T =[[0 for i in range(n + 1)] for i in range(n + 1)]
  for i in range(n):
    if symb[i] == 'F': F[i][i] = 1
    else: F[i][i] = 0
    if symb[i] == 'T': T[i][i] = 1
    else: T[i][i] = 0
  for gap in range(1, n):
    i = 0
    for j in range(gap, n):
      T[i][j] = F[i][j] = 0
      for g in range(gap):
        k = i + g
        tik = T[i][k] + F[i][k]
        tkj = T[k + 1][j] + F[k + 1][j]
        if oper[k] == '&':
          T[i][j] += T[i][k] * T[k + 1][j]
          F[i][j] +=(tik * tkj - T[i][k] * T[k + 1][j])
        if oper[k] == '|':
          F[i][j] += F[i][k] * F[k + 1][j]
          T[i][j] +=(tik * tkj - F[i][k] * F[k + 1][j])
        if oper[k] == '^':
          T[i][j] +=(F[i][k] * T[k + 1][j] + T[i][k] * F[k + 1][j])
          F[i][j] +=(T[i][k] * T[k + 1][j] + F[i][k] * F[k + 1][j])
      i += 1
  return T[0][n - 1]


def print_zigzag(rows, columns, numbers):
  k = 0
  arr =[[0 for i in range(columns)] for j in range(rows)]
  for i in range(rows):
    if(i % 2 == 0):
      j = 0
      while j < columns and numbers[k] > 0:
        arr[i][j] = k + 1
        numbers[k] -= 1
        if numbers[k] == 0: k += 1
        j += 1
    else:
      j = columns - 1
      while j >= 0 and numbers[k] > 0:
        arr[i][j] = k + 1
        numbers[k] -= 1
        if numbers[k] == 0: k += 1
        j -= 1
  for i in arr:
    for j in i: print(j, end = " ")
    print()


import sys
def sort_arr_using_poly_expr(arr, n, A, B, C):
  for i in range(n): 
    arr[i] = A * arr[i] * arr[i] + B * arr[i] + C
  index = -(sys.maxsize - 1)
  maximum = -(sys.maxsize - 1)
  for i in range(n):
    if maximum < arr[i]:
      index = i
      maximum = arr[i]
  i = 0
  j = n - 1
  new_arr = [0] * n
  k = 0
  while i < index and j > index:
    if arr[i] < arr[j]:
      new_arr[k] = arr[i]
      k += 1
      i += 1
    else:
      new_arr[k] = arr[j]
      k += 1
      j -= 1
  while i < index:
    new_arr[k] = arr[i]
    k += 1
    i += 1
  while j > index:
    new_arr[k] = arr[j]
    k += 1
    j -= 1
    new_arr[n - 1] = maximum
  for i in range(n): 
    arr[i] = new_arr[i]
  return arr

def str_slice_concat(s, c1, c2):
  l = len(s)
  for i in range(l):
    if(s[i] == c1): s = s[0: i] + c2 + s[i + 1:]
    elif(s[i] == c2): s = s[0: i] + c1 + s[i + 1:]
  return s

"-----------------"
test()