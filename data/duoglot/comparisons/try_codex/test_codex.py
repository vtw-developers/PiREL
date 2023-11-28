# %%
import openai
import json
import sys

def read_content(filename):
  with open(filename, 'r') as f:
    return f.read()

def save_content(filename, content):
  print("Write file:", filename)
  with open(filename, 'w') as f:
    f.write(content)

def append_content(filename, content):
  print("Write file:", filename)
  with open(filename, 'a') as f:
    f.write(content)

# pip install --upgrade openai
openai.api_key = json.loads(read_content("./drvtry"))

# %%
# prompt = read_content("./microtests/test1.txt")
prompt = """
##### Translate this function from Python into JavaScript
### Python

def f_gold(mat, r, c):
  result = 0
  for i in range(r):
    j = 0
    for j in range(c - 1):
      if mat[i][j + 1] <= mat[i][j]: break
    if j == c - 2: result += 1
  for i in range(0, r):
    j = 0
    for j in range(c - 1, 0, - 1):
      if mat[i][j - 1] <= mat[i][j]: break
    if c > 1 and j == 1: result += 1
  return result
    
### JavaScript
"""

# Too large max_tokens result in InvalidRequestError: This model's maximum context length is 4097 tokens, however you requested 4159 tokens (159 in your prompt; 4000 for the completion). Please reduce your prompt; or completion length.
res = openai.Completion.create(
   engine='code-davinci-001', # 'code-davinci-002'
   prompt=prompt,
   max_tokens=256, # 4000 # 5432
   temperature=0,
   logprobs=1,
   # echo=True,
   n=1
)

if len(res["choices"]) > 0: print("----- SUCCESSFUL -----")
for choice in res["choices"]:
  print(choice["text"])
# %%
