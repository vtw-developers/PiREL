import sys
import os
import eval_codex_lib

print("""
===============================================================================
===============================================================================
===============================================================================
""")


prompt1 = lambda pycode: f"""##### Translate this function from Python into JavaScript
### Python

{pycode}
    
### JavaScript
"use strict";
"""

# https://beta.openai.com/docs/api-reference/completions/create
configs = {
  "temp0-prompt1-model001": {
    "model": 'code-davinci-001',
    "temp": 0,
    "prompt": prompt1,
    "maxtokens_list": [384, 4000],
    "logprobs": 1
  },
  "temp0-prompt1-model002": {
    "model": 'code-davinci-002',
    "temp": 0,
    "prompt": prompt1,
    "maxtokens_list": [384, 4000],
    "logprobs": 1
  },
}


print(configs.keys())
CONFIG_KEY = sys.argv[1]
if CONFIG_KEY not in configs:
  raise Exception("CONFIG_KEY should be in " + str(list(configs.keys())))

TEMP = configs[CONFIG_KEY]["temp"]
PROMPT = configs[CONFIG_KEY]["prompt"]
MAX_TOKENS_LIST = configs[CONFIG_KEY]["maxtokens_list"]
MODEL_NAME = configs[CONFIG_KEY]["model"]
LOGPROBS = configs[CONFIG_KEY]["logprobs"]


is_ext = "ext" in sys.argv 
show_err = "showerr" in sys.argv

BENCHNAME = "staleetcode"
ROOTDIR = f"{BENCHNAME}-codex-" + CONFIG_KEY
TESTROOTDIR = ROOTDIR # f"{BENCHNAME}_ext-codex-" + CONFIG_KEY if is_ext else f"{BENCHNAME}-codex-" + CONFIG_KEY
source_path = f"../../tests/{BENCHNAME}/py"
gold_path = os.path.join(ROOTDIR, "./pygold")
prompted_path = os.path.join(ROOTDIR, "./prompted")
trans_path = os.path.join(ROOTDIR, "./trans")
combined_savepath = os.path.join(TESTROOTDIR, "./combined")
runoutputpath = os.path.join(TESTROOTDIR, "./output")
additionallogpath = os.path.join(TESTROOTDIR, "./runtest.log")

if not os.path.exists(ROOTDIR): os.mkdir(ROOTDIR)
if not os.path.exists(TESTROOTDIR): os.mkdir(TESTROOTDIR)
if not os.path.exists(gold_path): os.mkdir(gold_path)
if not os.path.exists(prompted_path): os.mkdir(prompted_path)
if not os.path.exists(trans_path): os.mkdir(trans_path)
if not os.path.exists(combined_savepath): os.mkdir(combined_savepath)
if not os.path.exists(runoutputpath): os.mkdir(runoutputpath)

testscript_basic_path = f"../../tests/_output_/{BENCHNAME}-exportscript/py_js"
# testscript_ext_path = "../../tests/_output_/{BENCHNAME}_ext-exportextscript/py_js"
testscript_path = testscript_basic_path # testscript_ext_path if "ext" in sys.argv else testscript_basic_path

testscript_list = sorted(list(os.listdir(testscript_path)))


eval_codex_lib.run_steps(
  sys.argv[-1].split(","),
  bench_prefix="L",
  is_allinone=False,
  PROMPT=PROMPT,
  TEMP=TEMP,
  LOGPROBS=LOGPROBS,
  MAX_TOKENS_LIST=MAX_TOKENS_LIST,
  MODEL_NAME=MODEL_NAME,
  source_path=source_path,
  testscript_path=testscript_path,
  testscript_list=testscript_list,
  gold_path=gold_path,
  prompted_path=prompted_path,
  trans_path=trans_path,
  combined_savepath=combined_savepath,
  additionallogpath=additionallogpath,
  runoutputpath=runoutputpath,
  is_prepend_bef_test=False,
  gold_cleanup_func=lambda x : "\n".join(list(filter(lambda x : not x.startswith("###"), x.split("\n")))),
  is_ext=is_ext,
  show_err=show_err
)