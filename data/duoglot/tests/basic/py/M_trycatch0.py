try:
  raise Exception("CustomError")
except Exception as e:
  print("Exception!")
  print(e)