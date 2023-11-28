def get_content(line_mode):
  with open('./a.txt', 'r') as f:
    if not line_mode:
      return f.read()
    else:
      return f.readlines()