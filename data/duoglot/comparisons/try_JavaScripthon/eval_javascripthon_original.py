# http://www.transcrypt.org/docs/html/installation_use.html#compiling-for-node-js
import subprocess
import os
import signal 
import timeit
import sys

def command_execute(command, timeout=10):
  print("--- Executing command:", command)
  try:
    proc = subprocess.Popen(command, cwd=os.path.abspath(os.path.dirname(__file__)), shell=True, preexec_fn=os.setsid)
    proc.wait(timeout)
  except Exception as e:
    os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
    raise e


source_path = "../../tests/standalone/py"
gold_path = "./standalone/pygold"

TESTING_BENCH_NAME = "standalone_ext" if "ext" in sys.argv else "standalone"
combined_savepath = f"./{TESTING_BENCH_NAME}/combined"
runoutputpath = f"./{TESTING_BENCH_NAME}/output"
additionallogpath = f"./{TESTING_BENCH_NAME}/runtest.log"

if not os.path.exists("./standalone/"): os.mkdir("./standalone/")
if not os.path.exists(f"./{TESTING_BENCH_NAME}/"): os.mkdir(f"./{TESTING_BENCH_NAME}/")
if not os.path.exists(gold_path): os.mkdir(gold_path)
if not os.path.exists(combined_savepath): os.mkdir(combined_savepath)
if not os.path.exists(runoutputpath): os.mkdir(runoutputpath)

TESTSCRIPT_DIR_NAME = "standalone_ext-exportextscript" if "ext" in sys.argv else "standalone-exportscript"
testscript_path = f"../../tests/_output_/{TESTSCRIPT_DIR_NAME}/py_js"
testscript_list = sorted(list(os.listdir(testscript_path)))

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


if "trans" in sys.argv:
  skipcount = 0
  for file in sorted(list(os.listdir(source_path))):
    if not file.startswith("GFG"): continue
    if not file.endswith(".py"): continue
    jsfile = file.replace(".py", ".js")
    filedir = file.replace(".py", "")
    if not jsfile in testscript_list:
      print(f"WARNING: {file} no testscript. Skipped for now.")
      skipcount += 1
      continue
    srcpath = os.path.join(source_path, file)
    content = read_content(srcpath)
    before_test = content.split("def test()")[0]
    gold_func = content.split('"-----------------"')[1]
    gold_code = before_test + '\n"------- imports -------"\n' + gold_func
    gold_savepath = os.path.join(gold_path, file)
    save_content(gold_savepath, gold_code)
    time1 = timeit.default_timer()
    command_execute(f"python -m metapensiero.pj {gold_savepath}")
    time2 = timeit.default_timer()
    print(f"({file}) TRANSTIME:" + str(time2 - time1))
  print("SKIPPED:" + str(skipcount))


if "fill" in sys.argv:
  skipcount = 0
  errorcount = 0
  for file in sorted(list(os.listdir(source_path))):
    if not file.startswith("GFG"): continue
    jsfile = file.replace(".py", ".js")
    filedir = file.replace(".py", "")
    if not jsfile in testscript_list:
      print(f"WARNING: {file} no testscript. Skipped for now.")
      skipcount += 1
      continue
    gold_transpath = os.path.join(gold_path, jsfile)
    if not os.path.exists(gold_transpath):
      print(f"NOTICE: {file} no translation. count as error.")
      errorcount += 1
      continue
    goldtrans_content = read_content(gold_transpath)

    testpath = os.path.join(testscript_path, jsfile)
    test_content = read_content(testpath)

    combpath = f"{os.path.join(combined_savepath, jsfile)}"
    combined_testcode = test_content.replace("//TRANSlATED_PLACEHOLDER_NO_OUTPUT_EXPECTED", goldtrans_content)
    combined_testcode = combined_testcode.replace("const SKIP_LOGGING = false", "const SKIP_LOGGING = true")
    save_content(combpath, combined_testcode)

  print("skipcount: " + str(skipcount) + "  errorcount: " + str(errorcount))

if "run" in sys.argv:
  skipcount = 0
  errcount = 0
  save_content(additionallogpath, "")
  for file in sorted(list(os.listdir(source_path))):
    if not file.startswith("GFG"): continue
    jsfile = file.replace(".py", ".js")
    filedir = file.replace(".py", "")
    if not jsfile in testscript_list:
      print(f"WARNING: {file} no testscript. Skipped for now.")
      skipcount += 1
      continue
    srcpath = os.path.join(source_path, file)
    comb_path = os.path.join(combined_savepath, jsfile)
    output_stdout_path = os.path.join(runoutputpath, jsfile + ".out")
    output_stderr_path = os.path.join(runoutputpath, jsfile + ".err")
    try:
      command_execute(f"node {comb_path} >{output_stdout_path} 2>{output_stderr_path}")
    except Exception as e:
      append_content(additionallogpath, f"Failed to execute {comb_path}:\n{str(e)}\n")
      errcount += 1
  
  print("SKIPPED:", skipcount)
  print("ERROR:", errcount)

import json
if "stat" in sys.argv:
  skipcount = 0
  executor_err_count = 0
  test_err_count = 0
  pass_count = 0
  additional_log_content = read_content(additionallogpath)
  # additional_log_dict = {y[0]:y[1] for y in [x.split(":\n") for x in additional_log_content.split("Failed to execute ") if x.strip() != ""]}
  pass_list = []
  test_err_list = []
  for file in sorted(list(os.listdir(source_path))):
    if not file.startswith("GFG"): continue
    jsfile = file.replace(".py", ".js")
    filedir = file.replace(".py", "")
    if not jsfile in testscript_list:
      print(f"WARNING: {file} no testscript. Skipped for now.")
      skipcount += 1
      continue
    if additional_log_content.find(jsfile) >= 0:
      executor_err_count += 1
      if "showerr" in sys.argv: print("SHOWERR:", file)
      test_err_list.append(file.replace(".py", ""))
      continue
    srcpath = os.path.join(source_path, file)
    output_stdout_path = os.path.join(runoutputpath, jsfile + ".out")
    output_stderr_path = os.path.join(runoutputpath, jsfile + ".err")
    err = read_content(output_stderr_path).strip()
    if err != "":
      test_err_count += 1
      if "showerr" in sys.argv: print("SHOWERR:", file)
      test_err_list.append(file.replace(".py", ""))
    else: 
      pass_count += 1
      pass_list.append(file.replace(".py", ""))
    ratio = pass_count / (pass_count + test_err_count)
  info = {"pass_list": pass_list, "test_err_list": test_err_list}
  solved_set_fname = f"./eval_javascripthon_solved_set.ext.json" if "ext" in sys.argv else f"./eval_javascripthon_solved_set.json"
  save_content(solved_set_fname, json.dumps(info, indent=2)) 
  print("ratio:", ratio,  " skipcount:", skipcount, " executor_err_count:", executor_err_count, " test_err_count:", test_err_count)
