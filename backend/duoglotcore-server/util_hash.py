import hashlib

def string_sha256(string):
  """
  Return a SHA-256 hash of the given string
  """
  return hashlib.sha256(string.encode('utf-8')).hexdigest()

def strings_sha256(string_list):
  """
  Return a SHA-256 hash of the concatenation of all the strings in the list
  """
  return hashlib.sha256(b''.join([string.encode('utf-8') for string in string_list])).hexdigest()

def file_sha256(filepath):
  with open(filepath, 'rb') as f:
    return hashlib.sha256(f.read()).hexdigest()
