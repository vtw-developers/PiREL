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


def run_step_trans(bench_prefix, is_prepend_bef_test, gold_cleanup_func, source_path, testscript_list, testscript_path, gold_path, combined_savepath, is_allinone, **other_kwargs):
  skipcount = 0
  errcount = 0
  for file in sorted(list(os.listdir(source_path))):
    if not file.startswith(bench_prefix): continue
    jsfile = file.replace(".py", ".js")
    filedir = file.replace(".py", "")
    if not jsfile in testscript_list:
      print(f"WARNING: {file} no testscript. Skipped for now.")
      skipcount += 1
      continue
    srcpath = os.path.join(source_path, file)
    testpath = os.path.join(testscript_path, jsfile)
    content = read_content(srcpath)
    test_content = read_content(testpath)

    if is_allinone:
      gold_code = gold_cleanup_func(content)
    else:
      before_test = content.split("def test()")[0]
      gold_func = content.split('"-----------------"')[1]
      gold_code = gold_cleanup_func((before_test.strip() + '\n' + gold_func.strip()).strip() if is_prepend_bef_test else gold_func.strip())
    
    gold_savepath = os.path.join(gold_path, file)
    save_content(gold_savepath, gold_code)

    time1 = timeit.default_timer()
    command_execute(f"transcrypt -e6 -n -da -b -p .none {gold_savepath}") # use this line to keep assertions
    # command_execute(f"transcrypt -e6 -n -b -p .none {gold_savepath}")
    time2 = timeit.default_timer()
    print(f"({file}) TRANSTIME:" + str(time2 - time1))

    combdir = f"{os.path.join(combined_savepath, filedir)}"
    os.system(f"rm -rf {combdir}")
    tgt_path = os.path.join(os.path.dirname(gold_savepath), '__target__')
    if not os.path.exists(os.path.join(tgt_path, jsfile)): 
      print("!!!!!! TARGET FILE DOESN'T EXIST !!!!!!: ", jsfile)
      errcount += 1
      continue
    os.system(f"cp -r {tgt_path} {combdir}")
    comb_package_json_path = os.path.join(combdir, "package.json")
    save_content(comb_package_json_path, '{"type": "module"}')

    translated_path = os.path.join(combdir, jsfile)
    translated_code = read_content(translated_path)
    combined_testcode = test_content.replace("//TRANSlATED_PLACEHOLDER_NO_OUTPUT_EXPECTED", translated_code)
    combined_testcode = combined_testcode.replace("const SKIP_LOGGING = false", "const SKIP_LOGGING = true")
    save_content(translated_path, combined_testcode)
    save_content(translated_path + ".backup", translated_code)

  print("SKIPPED:", skipcount, "ERROR:", errcount)

def run_step_run(bench_prefix, additionallogpath, source_path, testscript_list, combined_savepath, runoutputpath, **other_kwargs):
  skipcount = 0
  errcount = 0
  save_content(additionallogpath, "")
  for file in sorted(list(os.listdir(source_path))):
    if not file.startswith(bench_prefix): continue
    jsfile = file.replace(".py", ".js")
    filedir = file.replace(".py", "")
    if not jsfile in testscript_list:
      print(f"WARNING: {file} no testscript. Skipped for now.")
      skipcount += 1
      continue
    srcpath = os.path.join(source_path, file)
    combdir = f"{os.path.join(combined_savepath, filedir)}"
    translated_path = os.path.join(combdir, jsfile)
    output_stdout_path = os.path.join(runoutputpath, jsfile + ".out")
    output_stderr_path = os.path.join(runoutputpath, jsfile + ".err")
    try:
      command_execute(f"node {translated_path} >{output_stdout_path} 2>{output_stderr_path}")
    except Exception as e:
      append_content(additionallogpath, f"Failed to execute {translated_path}:\n{str(e)}\n")
      errcount += 1
  
  print("SKIPPED:", skipcount)
  print("ERROR:", errcount)

import json
def run_step_stat(bench_prefix, is_showerr, is_ext, additionallogpath, testscript_list, source_path, runoutputpath, **other_kwargs):
  skipcount = 0
  executor_err_count = 0
  test_err_count = 0
  pass_count = 0
  additional_log_content = read_content(additionallogpath)
  # additional_log_dict = {y[0]:y[1] for y in [x.split(":\n") for x in additional_log_content.split("Failed to execute ") if x.strip() != ""]}
  pass_list = []
  test_err_list = []
  for file in sorted(list(os.listdir(source_path))):
    if not file.startswith(bench_prefix): continue
    jsfile = file.replace(".py", ".js")
    filedir = file.replace(".py", "")
    if not jsfile in testscript_list:
      print(f"WARNING: {file} no testscript. Skipped for now.")
      skipcount += 1
      continue
    if additional_log_content.find(jsfile) >= 0:
      executor_err_count += 1
      if is_showerr: print("SHOWERR:", file)
      test_err_list.append(file.replace(".py", ""))
      continue
    srcpath = os.path.join(source_path, file)
    output_stdout_path = os.path.join(runoutputpath, jsfile + ".out")
    output_stderr_path = os.path.join(runoutputpath, jsfile + ".err")
    err = read_content(output_stderr_path).strip()
    if err != "":
      test_err_count += 1
      if is_showerr: print("SHOWERR:", file)
      test_err_list.append(file.replace(".py", ""))
    else: 
      pass_count += 1
      pass_list.append(file.replace(".py", ""))
    ratio = pass_count / (pass_count + test_err_count)
  info = {"pass_list": pass_list, "test_err_list": test_err_list}
  solved_set_fname = f"./eval_transcrypt_solved_set.ext.json" if is_ext else f"./eval_transcrypt_solved_set.json"
  save_content(solved_set_fname, json.dumps(info, indent=2)) 
  print("ratio:", ratio,  " skipcount:", skipcount, " executor_err_count:", executor_err_count, " test_err_count:", test_err_count)

STEP_FUNC_DICT = {
  "trans": run_step_trans,
  "run": run_step_run,
  "stat": run_step_stat
}

def run_step(step_name, bench_prefix, is_prepend_bef_test, is_showerr, is_allinone, is_ext, gold_cleanup_func, source_path, gold_path, combined_savepath, runoutputpath, additionallogpath, testscript_path, testscript_list):
  if step_name in STEP_FUNC_DICT:
    step_func = STEP_FUNC_DICT[step_name]
    argsdict = {
      "bench_prefix": bench_prefix,
      "is_prepend_bef_test": is_prepend_bef_test, 
      "is_showerr": is_showerr,
      "is_allinone": is_allinone,
      "is_ext": is_ext,
      "source_path": source_path,
      "gold_path": gold_path,
      "combined_savepath": combined_savepath,
      "runoutputpath": runoutputpath,
      "additionallogpath": additionallogpath,
      "testscript_path": testscript_path
    }
    print(f"\n\n------------------------------- Run steps {step_name} argsdict: -------------------------------")
    print(json.dumps(argsdict, indent=2))
    argsdict["testscript_list"] = testscript_list
    argsdict["gold_cleanup_func"] = gold_cleanup_func
    return step_func(**argsdict)
  else:
    raise Exception("Unknown step name: " + step_name)