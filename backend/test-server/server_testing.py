from genericpath import isdir
import json
import os
import flask
from flask import request, jsonify
from flask_cors import CORS
import timeit
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import traceback
def exception_to_string(excp):
   stack = traceback.extract_tb(excp.__traceback__)  # add limit=??  traceback.extract_stack()[:-3] +
   pretty = traceback.format_list(stack)
   return ''.join(pretty) + '\n  {} {}'.format(excp.__class__,excp)


print("=============== testing server INIT ===============")
app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = False # True
app.config['MAX_CONTENT_LENGTH'] = 67108864

data_path = os.path.abspath(os.path.join(app.root_path, "../../data"))

def read_json(fname):
  with open(fname, 'r') as f:
    return json.load(f)

def read_text(fname):
  with open(fname, 'r') as f:
    return f.read()

import code_runner

@app.route("/stapairrun", methods=['POST'])
def stapairrun():
  if request.json is None:
    return jsonify({"result": None, "error_msg": "No posted data"})
  source_code = request.json["source_code"]
  target_code = request.json["target_code"]
  source_lang = request.json["source_language"]
  target_lang = request.json["target_language"]
  is_dryrun = request.json["is_dryrun"]
  try:
    ts1 = timeit.default_timer()
    srclog, srcerror = code_runner.run_code_with_mylog(source_code, source_lang)
    ts2 = timeit.default_timer()
    assert srcerror is None
    tt1 = timeit.default_timer()
    tarcode, tarlog, tarerror = code_runner.run_code_until_mylog_mismatch(target_code, target_lang, srclog, is_dryrun)
    tt2 = timeit.default_timer()
    timespan_s = ts2 - ts1
    timespan_t = tt2 - tt1
  except Exception as e:
    return jsonify({"error_msg": "failed to run code pair: " + exception_to_string(e)})
  return jsonify({"target_code": tarcode, "target_log": tarlog, "target_error": tarerror, "timespan_s": timespan_s, "timespan_t": timespan_t})

@app.route("/starun", methods=['POST'])
def starun():
  if request.json is None:
    return jsonify({"result": None, "error_msg": "No posted data"})
  code = request.json["code"]
  lang = request.json["lang"]
  detail = "detail" in request.json and request.json["detail"] is True
  error = None
  try:
    ts1 = timeit.default_timer()
    error, stdo, stde = code_runner.run_standalone_code(code, lang)
    ts2 = timeit.default_timer()
    timespan = ts2 - ts1
  except Exception as e:
    return jsonify({"error_msg": "failed to run code: " + exception_to_string(e)})
  ret_data = {"is_success": error is None, "error": error, "timespan": timespan}
  if detail:
    ret_data["stdout"] = stdo
    ret_data["stderr"] = stde
  return jsonify(ret_data)


@app.route("/nodemodulerun", methods=["POST"])
def nodemodulerun():
  if request.json is None:
    return jsonify({"result": None, "error_msg": "No posted data"})
  cwd = os.path.join(data_path, request.json["cwd"])
  main = request.json["main"]
  try:
    run_stdout, run_stderr = code_runner.run_node_module(cwd, main)
  except Exception as e:
    return jsonify({"error_msg": "failed to run node module: " + exception_to_string(e)})
  return jsonify({"run_stdout": run_stdout, "run_stderr": run_stderr})

@app.route("/anycmdrun", methods=["POST"])
def anycmdrun():
  if request.json is None:
    return jsonify({"result": None, "error_msg": "No posted data"})
  cwd = os.path.join(data_path, request.json["cwd"])
  cmd = request.json["cmd"]
  try:
    run_stdout, run_stderr, run_retcode = code_runner.run_any_cmd(cwd, cmd)
  except Exception as e:
    return jsonify({"error_msg": "failed to run any command: " + exception_to_string(e)})
  # retcode not implemented. TODO
  return jsonify({"run_stdout": run_stdout, "run_stderr": run_stderr, "run_retcode": run_retcode})


from _common.shared import gettmpfile_gen
app.route("/gettmpfile/<path:filename>")(
  gettmpfile_gen("/tmp/codesnart_runner", app)
)

@app.route("/checkver")
def get_versions():
  node1615_version = subprocess.check_output("/root/.nvm/versions/node/v16.15.1/bin/node --version", shell=True).decode('utf-8').strip()
  node_version = subprocess.check_output("node --version", shell=True).decode('utf-8').strip()
  python3_version = subprocess.check_output("python3 --version", shell=True).decode('utf-8').strip()
  return jsonify({"node1615_version": node1615_version, "node_version": node_version, "python3_version": python3_version})

@app.route("/checkenv")
def get_envs():
  path = subprocess.check_output("echo $PATH", shell=True).decode('utf-8').strip()
  return jsonify({"path": path})


import subprocess

import argparse
parser = argparse.ArgumentParser(description='Test Server')
parser.add_argument('--host', type=str, default="0.0.0.0", help='Host to use')
parser.add_argument('--port', type=int, default=8776, help='Port to use')
parser.add_argument('--reloader', type=bool, default=False, help='Using reloader')
args = parser.parse_args()

if __name__ == '__main__':
    app.run(host=args.host, port=int(args.port), use_reloader=args.reloader)