
import os
import sys
import eval_py2js_lib

BENCHNAME = "stactci"
TESTING_BENCH_NAME = f"{BENCHNAME}_ext" if "ext" in sys.argv else f"{BENCHNAME}"

source_path = f"../../tests/{BENCHNAME}/py"
gold_path = f"./{BENCHNAME}/pygold"
combined_savepath = f"./{TESTING_BENCH_NAME}/combined"
runoutputpath = f"./{TESTING_BENCH_NAME}/output"
additionallogpath = f"./{TESTING_BENCH_NAME}/runtest.log"

PY2JS_PATH = "/root/py2js"
PY2JS_SCRIPT_PATH = "/root/py2js/pyjs.py"

if not os.path.exists(f"./{BENCHNAME}/"): os.mkdir(f"./{BENCHNAME}/")
if not os.path.exists(f"./{TESTING_BENCH_NAME}/"): os.mkdir(f"./{TESTING_BENCH_NAME}/")
if not os.path.exists(gold_path): os.mkdir(gold_path)
if not os.path.exists(combined_savepath): os.mkdir(combined_savepath)
if not os.path.exists(runoutputpath): os.mkdir(runoutputpath)

TESTSCRIPT_DIR_NAME = f"{BENCHNAME}_ext-exportextscript" if "ext" in sys.argv else f"{BENCHNAME}-exportscript"
testscript_path = f"../../tests/_output_/{TESTSCRIPT_DIR_NAME}/py_js"
testscript_list = sorted(list(os.listdir(testscript_path)))


bench_prefix = "AL"
is_prepend_bef_test = False

step_name = sys.argv[-1]
eval_py2js_lib.run_step(
  step_name=step_name, 
  PY2JS_SCRIPT_PATH=PY2JS_SCRIPT_PATH,
  PY2JS_PATH=PY2JS_PATH,
  bench_prefix=bench_prefix,
  is_prepend_bef_test=is_prepend_bef_test, 
  is_showerr="showerr" in sys.argv,
  is_ext="ext" in sys.argv, 
  is_allinone=True,
  gold_cleanup_func=lambda x : "\n".join(list(filter(lambda x : not x.startswith("###"), x.split("\n")))),
  source_path=source_path,
  gold_path=gold_path,
  combined_savepath=combined_savepath,
  runoutputpath=runoutputpath,
  additionallogpath=additionallogpath,
  testscript_path=testscript_path,
  testscript_list=testscript_list)