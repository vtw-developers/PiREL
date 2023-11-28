MYLOG_IMPL_JS = """NOT_IMPLEMENTED"""
# MYLOG_IMPL_JS_TODO = """
# "use strict";
# function mylog_obj_to_comp(arg) {
#   let typearg = typeof arg;
#   if (arg === true || arg === false) return ["bool", arg];
#   else if (typearg === "number") return ["num", arg];
#   else if (typearg === "string") return ["string", arg.length, arg.length < 10 ? arg : arg.slice(0,10)];
#   else if (Array.isArray(arg)) return ["list", arg.length, arg.length > 0 ? mylog_obj_to_comp(arg[0]) : "EMPTY", arg.length > 1 ? mylog_obj_to_comp(arg[1]) : "EMPTY"];
#   else if (arg === null || arg === undefined) return ["none"];
#   else return ["Unknown"];
# }
# function mylog() {
#   let info_list = ["MYLOG:" + arguments[0]];
#   for (let i = 1; i < arguments.length; i++) {
#     info_list.push(mylog_obj_to_comp(arguments[i]));
#   }
#   console.log("\\n" + JSON.stringify(info_list));
# }
# function myexactlog() {
#   mylog(...arguments);
# }

# """

MYLOG_MATCH_IMPL_JS = """
"use strict";
const SKIP_LOGGING = false;
const MYLOG_LIST = {MYLOG_LIST};
let _console_log = console.log;
let mylog_callcount = 0;
function _list_compare(ls1, ls2) {
  if (ls1.length !== ls2.length) return false;
  if (ls1.length > 0 && ls1[0] === "num" && ls2.length > 0 && ls2[0] === "num") {
    if (ls1[1] === ls2[1]) return true;
    else {
      try {
        if (Math.abs(ls1[1]) > 1e-6 && Math.abs(ls2[1]) > 1e-6) {
          if (Math.abs(ls1[1]) > 2 * Math.abs(ls2[1])) return false;
          else if (2 * Math.abs(ls1[1]) < Math.abs(ls2[1])) return false;
          else if (Math.abs(Math.abs(ls1[1] / ls2[1]) - 1) > 1e-6) return false;
          else return true;
        } 
        else if (Math.abs(ls1[1]) <= 1e-6 && Math.abs(ls2[1]) <= 1e-6) return true;
        else return false;
      } catch (e) {
        throw Error("MyLogError _list_compare num error: " + ls1 + " <==> " + ls2 + " " + e);
      }
    }
  }
  else if (ls1.length > 0 && ls1[0] === "string" && ls2.length > 0 && ls2[0] === "Unknown") {
    return ls1[2] === ls2[2];
  }
  let anyDiff = false;
  for (let i = 0; i < ls1.length; i++) {
    let ls1e = ls1[i], ls2e = ls2[i];
    if (Array.isArray(ls1e) && Array.isArray(ls2e)) {
      let elem_anydiff = !_list_compare(ls1e, ls2e);
      anyDiff = anyDiff || elem_anydiff;
    }
    else anyDiff = anyDiff || (ls1e !== ls2e);
    if (anyDiff) break;
  }
  return !anyDiff;
}
function mylog_obj_to_comp(is_exact, arg) {
  let typearg = typeof arg;
  if (arg === true || arg === false) return ["bool", arg];
  else if (typearg === "number") return ["num", arg];
  else if (typearg === "string") {
    if (is_exact) return ["string", arg.length, arg];
    else return ["string", arg.length, arg.length < 10 ? arg : arg.slice(0,10)];
  }
  else if (Array.isArray(arg)) {
    if (is_exact) return ["list", arg.length, arg.map(x => mylog_obj_to_comp(is_exact, x))];
    else return ["list", arg.length, arg.length > 0 ? mylog_obj_to_comp(is_exact, arg[0]) : "EMPTY", arg.length > 1 ? mylog_obj_to_comp(is_exact, arg[1]) : "EMPTY"];
  }
  else if (arg === null || arg === undefined) return ["none"];
  else {
    let str_result = String(arg);
    return ["Unknown", str_result.length, str_result];
  }
}
function _mylog() {
  let is_exact = arguments[0];
  let prefix = is_exact ? "MYLOGEX:" : "MYLOGAP:";
  let info_list = [prefix + arguments[1]];
  if (SKIP_LOGGING === true && arguments[1] === -1) return;
  for (let i = 2; i < arguments.length; i++) {
    info_list.push(mylog_obj_to_comp(is_exact, arguments[i]));
  }
  _console_log("\\n" + JSON.stringify(info_list));
  while (SKIP_LOGGING === true && mylog_callcount < MYLOG_LIST.length && MYLOG_LIST[mylog_callcount][0].endsWith(":-1")) {
    mylog_callcount += 1;
  }
  if (mylog_callcount >= MYLOG_LIST.length) {
    throw Error("MyLogError MYLOG_LENGTH_EXCEEDED COUNT:" + String(mylog_callcount) + " CALL_ID:" + String(arguments[0]));
  }
  else {
    if (_list_compare(info_list, MYLOG_LIST[mylog_callcount])) {
      mylog_callcount += 1;
      return;
    } else {
      throw Error("MyLogError MISMATCH CALL_ID:" + String(arguments[1]) 
        + " MISMATCH_IDX:" + String(mylog_callcount) 
        + " OBSERVED:" + JSON.stringify(info_list) 
        + " EXPECTED:" + JSON.stringify(MYLOG_LIST[mylog_callcount]));
    }
  }
}
function mylog() {
  _mylog(false, ...arguments);
}
function myexactlog() {
  _mylog(true, ...arguments);
}
console.log = function () {
  myexactlog(-1, [...arguments]);
  _console_log(...arguments);
}
"""

MYLOG_IMPL_PY = """
import json
_default_print = print
def mylog_obj_to_comp(is_exact, arg):
  if isinstance(arg, bool): return ["bool", arg]
  elif isinstance(arg, str): 
    if is_exact:
      return ["string", len(arg), arg]
    else:
      return ["string", len(arg), arg if len(arg) < 10 else arg[0:10]]
  elif isinstance(arg, int) or isinstance(arg, float): return ["num", arg]
  elif isinstance(arg, list) or isinstance(arg, tuple): 
    if is_exact:
      return ["list", len(arg), [mylog_obj_to_comp(is_exact, x) for x in arg]]
    else:
      return ["list", len(arg), mylog_obj_to_comp(is_exact, arg[0]) if len(arg) > 0 else "EMPTY", mylog_obj_to_comp(is_exact, arg[1]) if len(arg) > 1 else "EMPTY"]
  elif arg is None: return ["none"]
  else: 
    str_result = str(arg)
    return ["Unknown", len(str_result), str_result]
def _mylog(is_exact, *args):
  prefix = "MYLOGEX:" if is_exact else "MYLOGAP:"
  info_list = [prefix + str(args[0])]
  for arg in args[1:]:
    info_list.append(mylog_obj_to_comp(is_exact, arg))
  _default_print("\\n" + json.dumps(info_list))
def mylog(*args):
  _mylog(False, *args)
def myexactlog(*args):
  _mylog(True, *args)
def print(*args, **kargs):
  myexactlog(-1, args)
  return _default_print(*args, **kargs)

"""

MYLOG_MATCH_IMPL_PY = """NOT_IMPLEMENTED"""
# MYLOG_MATCH_IMPL_PY_TODO = """
# MYLOG_LIST = {MYLOG_LIST}
# import json
# mylog_callcount = 0
# def _list_compare(ls1, ls2):
#   raise NotImplementedError
# def mylog_obj_to_comp(arg):
#   if isinstance(arg, bool): return ["bool", arg]
#   elif isinstance(arg, str): return ["string", len(arg), arg if len(arg) < 10 else arg[0:10]]
#   elif isinstance(arg, int) or isinstance(arg, float): return ["num", arg]
#   elif isinstance(arg, list) or isinstance(arg, tuple): return ["list", len(arg), mylog_obj_to_comp(arg[0]) if len(arg) > 0 else "EMPTY", mylog_obj_to_comp(arg[1]) if len(arg) > 1 else "EMPTY"]
#   elif arg is None: return ["none"]
#   else: return ["Unknown"]
# def mylog(*args):
#   info_list = ["MYLOG:" + str(args[0])]
#   for arg in args[1:]:
#     info_list.append(mylog_obj_to_comp(arg))
#   print("\\n" + json.dumps(info_list))
#   if _list_compare(info_list, MYLOG_LIST[mylog_callcount]): 
#     mylog_callcount += 1
#     return
#   else:
#     raise Exception("MyLogError CALL_ID:" + str(args[0]) + " MISMATCH_IDX:" + str(mylog_callcount))
# def myexactlog(*args):
#   mylog(*args)

# """

MYLOG_IMPL = {
  "js": MYLOG_IMPL_JS,
  "py": MYLOG_IMPL_PY
}

MYLOG_MATCH_IMPL = {
  "js": MYLOG_MATCH_IMPL_JS,
  "py": MYLOG_MATCH_IMPL_PY
}

import util_hash
import os
import json
import subprocess
import signal
import sys


def _get_temp_filename(code, language):
  hexhash = util_hash.string_sha256(code)[:8]
  return f"/tmp/codesnart_runner/{hexhash}.{language}"

def _save_to_file(filename, content):
  if not os.path.exists("/tmp/codesnart_runner/"):
    os.mkdir("/tmp/codesnart_runner/")
  print("# Write file to:", filename)
  with open(filename, 'w') as f:
    f.write(content)

def _read_file(filename):
  with open(filename, 'r') as f:
    return f.read()

def _get_coderun_command(filename, language):
  if language == "py": return f"python3 {filename}"
  elif language == "js": return f"node {filename}"
  else: raise Exception("Unsupported language: " + language)

def _command_execute(command, timeout=10):
  print("--- Executing command:", command)
  try:
    proc = subprocess.Popen(command, cwd=os.path.dirname(__file__), shell=True, preexec_fn=os.setsid)
    proc.wait(timeout)
  except Exception as e:
    os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
    raise e

def _extract_log_list_from_stdo(stdo, language):
  mylog_lines = [x for x in stdo.split("\n") if x.startswith('["MYLOG')]
  return [json.loads(x) for x in mylog_lines]

def _extract_err_from_stde(stde, language):
  if language == "js" and stde.find("/tmp/codesnart") >= 0:
    splitter = None
    if stde.find("SyntaxError:") >= 0:
      splitter = "SyntaxError:"
    elif stde.find("ReferenceError:") >= 0:
      splitter = "ReferenceError:"
    elif stde.find("Error: MyLogError") >= 0:
      splitter = "Error: MyLogError"
    elif stde.find("Error: MyAssertError") >= 0:
      splitter = "Error: MyAssertError"
    elif stde.find("Error: MyTraceError") >= 0:
      splitter = "Error: MyTraceError"
    elif stde.find("TypeError:") >= 0:
      splitter = "TypeError:"
    elif stde.find("RangeError:") >= 0:
      splitter = "RangeError:"
    elif stde.find("Error: Cannot find module") >= 0:
      splitter = "Error: Cannot find module"
    else:
      print("ERROR: runner stde unknown error type:\n" + stde, file=sys.stderr)
      assert "stde_unknown_error_type" == 0
    splitted = stde.split(splitter)
    assert len(splitted) == 2
    poslines = splitted[0].strip().split("\n")
    if poslines[0].startswith("/tmp/codesnart"):
      linenoraw = poslines[0].split(":")
      assert len(linenoraw) == 2
      lineno = [linenoraw[0], int(linenoraw[1])]
      linecontent = poslines[1].strip()
    else:
      lineno = [poslines[0], -1] # not accurate
      linecontent = "NOT_IMPLEMENTED_DONT_KNOW"

    errorlines = splitted[1].strip().split("\n")
    error_msg = errorlines[0]
    return {"error_type": splitter, "error_msg": error_msg, "lineno": lineno, "line_content": linecontent}
  elif language == "py" and stde.find("/tmp/codesnart") >= 0:
    return {"error_type": "UnknownError (Parser not implemented)"}
  return None

def _run_code(code, language):
  temp_filename = _get_temp_filename(code, language)
  _save_to_file(temp_filename, code)
  runner_command = _get_coderun_command(temp_filename, language)
  tofile_suffix = f" >{temp_filename}.stdout 2>{temp_filename}.stderr"
  if language == "py":
    _command_execute(runner_command + tofile_suffix)
  elif language == "js": 
    _command_execute(runner_command + tofile_suffix)
  else:
    raise Exception("Unsupported language: " + language)
  stdo = _read_file(f"{temp_filename}.stdout")
  stde = _read_file(f"{temp_filename}.stderr")
  return stdo, stde

def comment_out_tester_ph(code, language):
  if language == "py":
    splitter = '\n"+++++++++++++++++"'
    plussplits = code.split(splitter)
    if len(plussplits) == 1: return code
    assert len(plussplits) == 2
    to_comment_out, rest = plussplits
    commented_out = "\n".join(["# " + x for x in to_comment_out.split("\n")])
    return commented_out + splitter + rest
  elif language == "js":
    splitter = '\n"+++++++++++++++++"'
    plussplits = code.split(splitter)
    if len(plussplits) == 1: return code
    assert len(plussplits) == 2
    to_comment_out, rest = plussplits
    commented_out = "\n".join(["// " + x for x in to_comment_out.split("\n")])
    return commented_out + splitter + rest
  else:
    raise Exception("Unsupported language (comment_out_tester_ph): " + language)

# simplest. Just run the code and check for exceptions
def run_standalone_code(code, lang):
  stdo, stde = _run_code(code, lang)
  err = _extract_err_from_stde(stde, lang)
  return err, stdo, stde


# for standalone, reference source. to get log.
_run_code_with_mylog_last_run = None
def run_code_with_mylog(code, language):
  global _run_code_with_mylog_last_run
  if _run_code_with_mylog_last_run is not None and _run_code_with_mylog_last_run[0] == code and _run_code_with_mylog_last_run[1] == language:
    return _run_code_with_mylog_last_run[2], _run_code_with_mylog_last_run[3]
  if language not in MYLOG_IMPL:
    raise Exception(f"mylog for {language} is not implemented.")
  concatenated_code = MYLOG_IMPL[language] + comment_out_tester_ph(code, language)
  stdo, stde = _run_code(concatenated_code, language)
  exec_log_list, exec_error = _extract_log_list_from_stdo(stdo, language), _extract_err_from_stde(stde, language)
  _run_code_with_mylog_last_run = (code, language, exec_log_list, exec_error)
  return exec_log_list, exec_error

# for standalone, translated target. to match against log.
def run_code_until_mylog_mismatch(code, language, log_list, is_dryrun):
  if language not in MYLOG_MATCH_IMPL:
    raise Exception(f"mylog (match) for {language} is not implemented.")
  concode_prepart = MYLOG_MATCH_IMPL[language].replace("{MYLOG_LIST}", json.dumps(log_list))
  prepart_linecount = len(concode_prepart.split("\n")) - 1
  concatenated_code = concode_prepart + comment_out_tester_ph(code, language)
  if is_dryrun: 
    exec_loglist = None
    exec_error = None
  else:
    stdo, stde = _run_code(concatenated_code, language)
    exec_loglist = _extract_log_list_from_stdo(stdo, language)
    exec_error = _extract_err_from_stde(stde, language)
    if exec_error is not None and "lineno" in exec_error: exec_error["lineno"][1] -= prepart_linecount
  return concatenated_code, exec_loglist, exec_error



# ////////////////// logically seperated runners //////////////////

def _command_execute_with_cwd(command, timeout=10, cwd=os.path.dirname(__file__)):
  print("--- Executing command:", command)
  try:
    proc = None
    proc = subprocess.Popen(command, cwd=cwd, shell=True, preexec_fn=os.setsid)
    proc.wait(timeout)
    return proc.returncode
  except Exception as e:
    if proc is None: raise e
    os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
    raise e

def run_node_module(cwd, main):
  _command_execute_with_cwd(f"node {main} 2>./{main}.stderr 1>./{main}.stdout", cwd=cwd)
  path_prefix = os.path.join(cwd, main)
  stdo = _read_file(f"{path_prefix}.stdout")
  stde = _read_file(f"{path_prefix}.stderr")
  return stdo, stde

def run_any_cmd(cwd, cmd):
  hexhash = util_hash.string_sha256(cwd + cmd)[:8]
  retcode = _command_execute_with_cwd(f"{cmd} 2>./{hexhash}.stderr 1>./{hexhash}.stdout", cwd=cwd)
  path_prefix = os.path.join(cwd, hexhash)
  stdo = _read_file(f"{path_prefix}.stdout")
  stde = _read_file(f"{path_prefix}.stderr")
  return stdo, stde, retcode