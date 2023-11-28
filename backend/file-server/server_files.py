from genericpath import isdir
import json
import os
import flask
from flask import request, jsonify, redirect, send_from_directory
from flask_cors import CORS
from pathlib import Path


print("=============== file-server INIT ===============")

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True   # True
data_path = os.path.abspath(os.path.join(app.root_path, "../../data"))

def read_json(fname):
  with open(fname, 'r') as f:
    return json.load(f)

def read_text(fname):
  with open(fname, 'r') as f:
    return f.read()

@app.route('/echo/<path:msg>')
def echo(msg):
  response = app.response_class(response=msg, status=200, mimetype='text/plain')
  return response

@app.route('/anyfile/<path:filename>')
def get_anyfile(filename):
  fullpath = os.path.join(data_path, filename)
  try:
    with open(fullpath, 'r') as f:
      content = f.read()
    response = app.response_class(response=content, status=200, mimetype='text/plain')
    return response
  except:
    flask.abort(404)

@app.route('/anybinfile/<path:filename>')
def get_anybinfile(filename):
  fullpath = os.path.join(data_path, filename)
  try:
    with open(fullpath, 'rb') as f:
      content = f.read()
    response = app.response_class(response=content, status=200, mimetype='application/octet-stream')
    return response
  except:
    flask.abort(404)

POST_ALLOWED_PATHS = [data_path]
@app.route('/ensurepath/<path:dirpath>')
def get_ensure_path(dirpath):
  fullpath = os.path.join(data_path, dirpath)
  pathstart = lambda x: os.path.abspath(fullpath).startswith(x)
  if not any([pathstart(x) for x in POST_ALLOWED_PATHS]):
    return jsonify({"error_msg": "path not allowed for safety reasons (should fall in data folder): " + fullpath})
  try:
    os.makedirs(fullpath, exist_ok=True)
    return jsonify({"result": "OK"})
  except Exception as e:
    return jsonify({"error_msg": str(e)})

@app.route('/postanybinfile/<path:filename>', methods=["POST"])
def post_anybinfile(filename):
  fullpath = os.path.join(data_path, filename)
  pathstart = lambda x: os.path.abspath(fullpath).startswith(x)
  if not any([pathstart(x) for x in POST_ALLOWED_PATHS]):
    return jsonify({"error_msg": "path not allowed for safety reasons (should fall in data folder): " + fullpath})
  raw_data = request.get_data()
  try:
    with open(fullpath, 'wb') as f:
      f.write(raw_data)
    return jsonify({"result": "OK"})
  except Exception as e:
    return jsonify({"error_msg": str(e)})

@app.route('/postanytextfile/<path:filename>', methods=["POST"])
def post_anytextfile(filename):
  fullpath = os.path.join(data_path, filename)
  pathstart = lambda x: os.path.abspath(fullpath).startswith(x)
  if not any([pathstart(x) for x in POST_ALLOWED_PATHS]):
    return jsonify({"error_msg": "path not allowed for safety reasons (should fall in data folder): " + fullpath})
  try:
    content = request.get_data().decode('utf-8')
    with open(fullpath, 'w') as f:
      f.write(content)
    return jsonify({"result": "OK"})
  except Exception as e:
    return jsonify({"error_msg": str(e)})

@app.route('/postanytextfile_makedirs/<path:filename>', methods=["POST"])
def post_anytextfile_makedirs(filename):
  fullpath = Path(os.path.join(data_path, filename))

  # NOTE this is very dangerous
  os.makedirs(fullpath.parent, exist_ok=True)

  pathstart = lambda x: os.path.abspath(fullpath).startswith(x)
  if not any([pathstart(x) for x in POST_ALLOWED_PATHS]):
    return jsonify({"error_msg": "path not allowed for safety reasons (should fall in data folder): " + fullpath})
  try:
    content = request.get_data().decode('utf-8')
    with open(fullpath, 'w') as f:
      f.write(content)
    return jsonify({"result": "OK"})
  except Exception as e:
    return jsonify({"error_msg": str(e)})

@app.route('/getmultipletextfile', methods=["POST"])
def post_getmultipletextfile():
  filepaths = request.json["filepaths"]
  results = {}
  disallowed_list = []
  failed_list = []
  for filepath in filepaths:
    fullpath = os.path.join(data_path, filepath)
    pathstart = lambda x: os.path.abspath(fullpath).startswith(x)
    if not any([pathstart(x) for x in POST_ALLOWED_PATHS]):
      results[filepath] = None
      disallowed_list.append(filepath)
    else:
      try:
        with open(fullpath, 'r') as f:
          content = f.read()
          results[filepath] = content
      except Exception as e:
        results[filepath] = None
        failed_list.append(filepath)
  return jsonify({
    "filecontents": results,
    "disallowed_list": disallowed_list,
    "failed_list": failed_list
  })

@app.route('/removemultiplefile', methods=["POST"])
def post_removemultiplefile():
  filepaths = request.json["filepaths"]
  limiting_folder = request.json["limiting_folder"]
  removed_list = []
  disallowed_list = []
  failed_list = []
  for filepath in filepaths:
    fullpath = os.path.join(data_path, filepath)
    pathstart = lambda x: os.path.abspath(fullpath).startswith(x)
    if not any([pathstart(x) for x in POST_ALLOWED_PATHS]):
      disallowed_list.append(filepath)
    elif not pathstart(limiting_folder):
      disallowed_list.append(filepath)
    elif not os.path.isfile(fullpath):
      disallowed_list.append(filepath)
    try:
      os.remove(fullpath)
      removed_list.append(filepath)
    except Exception as e:
      failed_list.append(filepath)
  return jsonify({
    "removed_list": removed_list,
    "disallowed_list": disallowed_list,
    "failed_list": failed_list
  })

@app.route('/postappendanytextfile/<path:filename>', methods=["POST"])
def postappend_anytextfile(filename):
  fullpath = os.path.join(data_path, filename)
  pathstart = lambda x: os.path.abspath(fullpath).startswith(x)
  if not any([pathstart(x) for x in POST_ALLOWED_PATHS]):
    return jsonify({"error_msg": "path not allowed for safety reasons (should fall in data folder): " + fullpath})
  try:
    content = request.get_data().decode('utf-8')
    with open(fullpath, 'a') as f:
      f.write(content)
    return jsonify({"result": "OK"})
  except Exception as e:
    return jsonify({"error_msg": str(e)})

def save_to_path_autodir(filepath, content):
  dirpath = os.path.dirname(filepath)
  os.makedirs(dirpath, exist_ok=True)
  with open(filepath, 'w') as f:
    f.write(content)

import glob
@app.route("/listglob", methods=['POST'])
def get_listglob():
  if request.json is None:
    return jsonify({"error_msg": "No posted data"})
  glob_query = data_path + "/" + request.json["glob"]
  recursive = False
  if "recursive" in request.json: recursive = request.json["recursive"]
  glob_result = glob.glob(glob_query, recursive=recursive)
  return jsonify({"glob_expand": glob_result})


@app.route("/listdir", methods=['POST'])
def get_listdir():
  if request.json is None:
    return jsonify({"error_msg": "No posted data"})
  lang = request.json["language"]
  dirpath = request.json["dirpath"]
  try:
    filepaths = []
    dirpaths = []
    fullpath = os.path.join(data_path, dirpath)
    for x in sorted(list(os.listdir(fullpath))):
      joined_path = os.path.join(fullpath, x)
      relpath = os.path.join(dirpath, x)
      if isdir(joined_path):
        dirpaths.append(relpath + "/")
      elif lang is None or joined_path.endswith("." + lang):
        filepaths.append(relpath)
    return jsonify({"filepaths": filepaths, "dirpaths": dirpaths})
  except Exception as e:
    return jsonify({"error_msg": str(e)})

@app.route("/listdirtree", methods=["POST"])
def get_listdirtree():
  if request.json is None:
    return jsonify({"error_msg": "No posted data"})
  lang = request.json["language"]
  hdirpath = request.json["dirpath"]
  try:
    filepaths = []
    dirpaths = []
    def process_dir(mdirpath):
      fullpath = os.path.join(data_path, mdirpath)
      for x in sorted(list(os.listdir(fullpath))):
        joined_path = os.path.join(fullpath, x)
        relpath = os.path.join(mdirpath, x)
        if isdir(joined_path):
          dirpaths.append(relpath + "/")
          process_dir(joined_path)
        elif lang is None or joined_path.endswith("." + lang):
          filepaths.append(relpath)
    process_dir(hdirpath)
    return jsonify({"filepaths": filepaths, "dirpaths": dirpaths})
  except Exception as e:
    return jsonify({"error_msg": str(e)})

@app.route("/listdirtreenested", methods=["POST"])
def get_listdirtreenested():
  if request.json is None:
    return jsonify({"error_msg": "No posted data"})
  lang = request.json["language"]
  hdirpath = request.json["dirpath"]
  fullpath = os.path.join(data_path, hdirpath)
  try:
    result = {
      "files": [],
      "dirs": {}
    }
    def process_dir(mdirpath, res):
      for x in sorted(list(os.listdir(mdirpath))):
        joined_path = os.path.join(mdirpath, x)
        if isdir(joined_path):
          res["dirs"][x] = {"files": [], "dirs": {}}
          process_dir(joined_path, res["dirs"][x])
        elif lang is None or joined_path.endswith("." + lang):
          res["files"].append(x)
    process_dir(fullpath, result)
    return jsonify(result)
  except Exception as e:
    return jsonify({"error_msg": str(e)})

import util_hash
@app.route("/listdirallmeta", methods=['POST'])
def get_listdirallmeta():
  if request.json is None:
    return jsonify({"error_msg": "No posted data"})
  # include_pattern = request.json["include_pattern"]
  # ignore_pattern = request.json["ignore_pattern"] # TODO
  dirpath = request.json["dirpath"]
  fullpath = os.path.join(data_path, dirpath)
  try:
    fileids = []
    file_meta_dict = {}
    for x in sorted(list(os.listdir(fullpath))):
      joined_path = os.path.join(fullpath, x)
      if isdir(joined_path):
        pass
      else:
        # TODO: check against pattern
        fileids.append(x)
        if x not in file_meta_dict:
          file_meta_dict[x] = {}
          file_meta_dict[x]["path"] = joined_path
    for fileid in file_meta_dict:
      file_meta = file_meta_dict[fileid]
      filepath = file_meta["path"]
      file_meta["size"] = os.stat(filepath).st_size
      file_meta["sha256"] = util_hash.file_sha256(filepath)
    return jsonify({"fileids": fileids, "file_meta_dict": file_meta_dict})
  except Exception as e:
    return jsonify({"error_msg": str(e)})


@app.route("/gitstatus")
def get_gitstatus():
  content = read_text("/tmp/__gitstatus")
  return jsonify({"content": content})

import argparse
parser = argparse.ArgumentParser(description='File Server')
parser.add_argument('--host', type=str, default="0.0.0.0", help='Host to use')
parser.add_argument('--port', type=int, default=8777, help='Port to use')
parser.add_argument('--reloader', type=bool, default=False, help='Using reloader')
args = parser.parse_args()

if __name__ == '__main__':
    app.run(host=args.host, port=int(args.port), use_reloader=args.reloader)