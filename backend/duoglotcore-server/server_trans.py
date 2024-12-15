import sys
import os
import logging
import p_consts

# TODO parametrize in consts
logging.basicConfig(
  filename=p_consts.LOG_FPATH,
  filemode=p_consts.LOG_FMODE,
  format=p_consts.LOG_FORMAT,
  datefmt=p_consts.LOG_DATE_FORMAT,
  level=p_consts.LOG_LEVEL
)
logger = logging.getLogger(__name__)

# update logging levels for used modules (debug, info, warning, error, critical)
for _tpm in p_consts.LOG_3RDPARTY_MODULES:
  logging.getLogger(_tpm).setLevel(p_consts.LOG_3RDPARTY_LEVEL)


# ~~~ for debugging, can be removed later
import debugpy
def _breakpoint():
  debugpy.listen(('0.0.0.0', 4444))
  debugpy.wait_for_client()
  debugpy.breakpoint()

# uncomment when need debugging
# if not debugpy.is_client_connected():
#   _breakpoint()

logger.debug(f"DuoGlotCore Start in {'INTERPRETED' if p_consts.INTERPRET_MODE else 'COMPILED'} mode")
if p_consts.INTERPRET_MODE: os.system("rm -rf ./*cpython-*.so")
else: os.system("python3 ./setup_build.py build_ext --inplace")


import gc
import argparse
import json
import flask
from flask import request, jsonify
from flask_cors import CORS
import timeit
from tree_sitter import Language, Node, Parser
import grammar
import ast_parse
import ast_pretty
import ast_match
import grammar_expand
import grammar_rules
import code_beautify
import util_hash
import p_post_process_translation_rule
import traceback
import p_utils
import p_translators
import p_pirel

# for profiling
import cProfile, pstats, io
from pstats import SortKey
from consts import PROFILING_TYPE, PROFILING_OUTPUT_STYLE, ENABLE_CYTHON_PROFILE


if PROFILING_TYPE is not None:
  print("PROFILING tool: " + PROFILING_TYPE, file=sys.stderr)
  print("PROFILING cython: " + str(ENABLE_CYTHON_PROFILE), file=sys.stderr)
  print("PROFILING output: " + PROFILING_OUTPUT_STYLE, file=sys.stderr)


app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True   # True (set to false will auto minify json response)
app.config['MAX_CONTENT_LENGTH'] = 67108864
logger.debug('DuoGlot initialization complete')


@app.route("/postprocess-translation-rule", methods=['POST'])
def pirel_postprocess_translation_rule():
  '''
  added by @satbekmyrza
  this method is used to post-process generated patterns in translation rules
  '''
  if request.json is None:
    return jsonify({"result": None, "error_msg": "No posted data"})

  # data from frontend
  source_pattern = request.json["source_pattern"]
  target_pattern = request.json["target_pattern"]
  context = request.json["context"]
  templatized_nodes_replace_dws = request.json['templatized_nodes_replace_dws']
  templatized_node_ids = request.json['templatized_node_ids']
  is_insert_secret_fn = request.json['is_insert_secret_fn']
  kwargs = request.json["kwargs"]

  _subject_name = kwargs["subject_name"]
  p_utils.log_json_time(f'{_subject_name}_context_clean_pptr.json', context)
  p_utils.log_json_time(f'{_subject_name}_templatized_nodes_replace_dws_pptr.json', templatized_nodes_replace_dws)
  p_utils.log_json_time(f'{_subject_name}_templatized_node_ids_pptr.json', templatized_node_ids)

  if context is None:
    return jsonify({
      "patterns": [{"source": source_pattern, "target": target_pattern}],
      "success": True
    })

  try:
    translation_rule = p_post_process_translation_rule.TranslationRule(source_pattern, target_pattern)
    result = translation_rule.trim_context_v2(context, templatized_node_ids, templatized_nodes_replace_dws)
    if result is None:
      return jsonify({
        "success": False,
        "error_message": "context not found"
      })
    mod_source_s_expr, mod_target_s_expr = result
    if is_insert_secret_fn:
      translation_rule = p_post_process_translation_rule.TranslationRule(mod_source_s_expr, mod_target_s_expr)
      translation_rule.replace_secret_with_placeholder(p_consts.GENERIC_SECRET_FN)  # TODO re-implement hard-coded version
      return jsonify({
        "source": translation_rule.src_as_s_expression(),
        "target": translation_rule.tar_as_s_expression(),
        "success": True
      })

    return jsonify({
      "source": mod_source_s_expr,
      "target": mod_target_s_expr,
      "success": True
    })

  except Exception as exc:
    return jsonify({
      "success": False,
      "error_message": str(exc),
      "traceback": traceback.format_exc()
    })


@app.route("/nts")
def get_nts():
  return jsonify({
    "py_not_inlined_NTs": p_consts.PY_NOT_INLINED_NTS,
    "js_not_inlined_NTs": p_consts.JS_NOT_INLINED_NTS,
  })

@app.route("/parse", methods=['POST'])
def parse():
  if request.json is None:
    return jsonify({"result": None, "error_msg": "No posted data"})
  lang = request.json["language"]
  text = request.json["text"]
  result_ast, result_ann = ast_parse.parse_text_dbg(text, lang)
  return jsonify({"result": result_ast, "ann": result_ann})

@app.route("/matchcombo", methods=['POST'])
def matchcombo():
  if request.json is None:
    return jsonify({"result": None, "error_msg": "No posted data"})
  ast1 = request.json["ast1"]
  ast2 = request.json["ast2"]
  combo1 = request.json["combo1"]
  combo2 = request.json["combo2"]
  algo_name = request.json["algorithm"]
  match_result, typematch = ast_match.match_combo_with_AST(ast1, combo1, ast2, combo2, algo_name)
  return jsonify({"result": match_result, "typematch": typematch})

@app.route("/pairwisedist", methods=['POST'])
def pairwisedist():
  if request.json is None:
    return jsonify({"result": None, "error_msg": "No posted data"})
  trees1 = request.json["trees1"]
  trees2 = request.json["trees2"]
  algo_name = request.json["algorithm"]
  dists = []
  for i in range(len(trees2)):
    rowdist = []
    for j in range(len(trees1)):
      rowdist.append(ast_match.distance_of_AST_frags(trees2[i], trees1[j], algo_name))
    dists.append(rowdist)
  return jsonify({"result": dists})


# TODO what these are for?
optional_dbg_info_dict = {}
def _optional_dbg_info_save_func(obj, func):
  idobj = id(obj)
  assert idobj not in optional_dbg_info_dict
  optional_dbg_info_dict[idobj] = (obj, func)
  return idobj
def _optional_dbg_info_read_func(info_id):
  if info_id in optional_dbg_info_dict:
    data, func = optional_dbg_info_dict[info_id]
    return func(data)
  return None


# ~~~ entry point for DuoGlot translation
@app.route("/translate", methods=['POST'])
def translate():
  '''
  This function is invoked from frontend
  Use request object for the data sent from frontend
  request.json:
    source_code
    source_language - e.g. `py`
    target_language - e.g. `js`
    trans_program_str - rules
    choices - not sure yet
    auto_backward - not sure yet
  '''

  if request.json is None:
    return jsonify({"result": None, "error_msg": "No posted data"})

  src_code = request.json["source_code"]
  src_lang = request.json["source_lang"]
  tar_lang = request.json["target_lang"]
  trans_rules = request.json["translation_rules"]
  choices = request.json["choices"]
  auto_backward = request.json["autoback_enabled"]
  kwargs = request.json["kwargs"]

  # sanity check of kwargs
  assert 'subject_name' in kwargs, 'subject_name is missing in kwargs'
  assert 'pirel_enabled' in kwargs, 'pirel_enabled is missing in kwargs'

  _subject_name = kwargs["subject_name"]
  logger.info(f'{_subject_name} server_trans.translate(): Starting translation of "{_subject_name}" on the backend.')

  try:
    translation_result = p_pirel.translate(
      src_code,
      src_lang,
      tar_lang,
      trans_rules,
      auto_backward,
      choices,
      _optional_dbg_info_save_func,
      **kwargs
    )
    return jsonify(translation_result)
  except:
    traceback_str = traceback.format_exc()
    logger.critical(f'{_subject_name} Error on backend:\n{traceback_str}')
    print(f'\n\n{_subject_name} CRITICAL ERROR ON BACKEND:\n{traceback_str}', file=sys.stderr)
    return jsonify({"error_info": {"msg": f"{_subject_name} traceback: {traceback_str}"}})


parserule_cache = {}
@app.route("/parserules", methods=['POST'])
def parserules():
  if request.json is None:
    return jsonify({"result": None, "error_msg": "No posted data"})
  transprog = request.json["trans_program_str"]
  parserule_key = util_hash.strings_sha256([transprog])

  expansion_programs, dbg_info, error_msg = None, None, None
  if parserule_key in parserule_cache:
    expansion_programs, dbg_info, error_msg = parserule_cache[parserule_key]
  else:
    try:
      expansion_programs, dbg_info = grammar_rules.parse_analyze_rules(transprog, show_disable=True)
    except Exception as e:
      error_msg = str(e)
      print("Rule parse ERROR:", e)
    parserule_cache[parserule_key] = [expansion_programs, dbg_info, error_msg]

  if error_msg is not None:
    return jsonify({"error_msg": error_msg})
  else:
    return jsonify({
      "expansion_programs": expansion_programs,
      "dbg_info": dbg_info,
    })

@app.route("/statrules", methods=['POST'])
def statrules():
  if request.json is None:
    return jsonify({"result": None, "error_msg": "No posted data"})
  transprog = request.json["trans_program_str"]
  parserule_key = util_hash.strings_sha256([transprog])

  expansion_programs, dbg_info, error_msg = None, None, None
  if parserule_key in parserule_cache:
    expansion_programs, dbg_info, error_msg = parserule_cache[parserule_key]
  else:
    try:
      expansion_programs, dbg_info = grammar_rules.parse_analyze_rules(transprog, show_disable=True)
    except Exception as e:
      error_msg = str(e)
      print("Rule parse ERROR:", e)
    parserule_cache[parserule_key] = [expansion_programs, dbg_info, error_msg]

  if error_msg is not None:
    return jsonify({"error_msg": error_msg})
  else:
    return jsonify({
      "stated_rules": [{"type": x["type"]} for x in expansion_programs],
    })

@app.route("/optdbginfo/<path:info_id>")
def optdbginfo(info_id):
  dbginfo = _optional_dbg_info_read_func(int(info_id))
  return jsonify({"is_found": dbginfo is not None, "result": dbginfo})

@app.route("/elemlist2code", methods=['POST'])
def elemlist2code():
  tarlang = request.json["target_language"]
  elem_list = request.json["elem_list"]
  ast = ast_pretty.elem_list_to_mapanno_ast(elem_list)
  code, map_by_exid = ast_pretty.ast_to_code(ast, tarlang)
  return jsonify({
    "result": code,
    "map_by_exid": map_by_exid
  })

@app.route("/clearmemcache")
def clearmemcache():
  optional_dbg_info_dict.clear()
  parserule_cache.clear()
  gc.collect()
  gc_stats = gc.get_stats()
  garbage_len = len(gc.garbage)
  del gc.garbage[:]
  return jsonify({
    "result": "Mem Cache Cleared",
    "gc_stats": gc_stats,
    "garbage_len": garbage_len
  })

@app.route("/updateconstsreload", methods=['POST'])
def updateconstreload():
  constdict = request.json["consts"]
  def replace_line_startswith(text, prefix, replacement):
    lines = text.split("\n")
    return "\n".join([(replacement if x.startswith(prefix) else x) for x in lines])
  const_text = p_utils.read_text("./consts.py")
  for k in constdict:
    if k in ["DEBUG_VERBOSE", "PROFILING_TYPE", "PROFILING_OUTPUT_STYLE", "ENABLE_CYTHON_PROFILE"]:
      pyval = json.dumps(constdict[k]).replace("null", "None").replace("true", "True").replace("false", "False")
      const_text = replace_line_startswith(const_text, F"{k} =", f"{k} = {pyval}")
    else: return jsonify({"error_msg": "Unknown const key: " + k})
  p_utils.write_text("./consts.py", const_text)
  return jsonify({"result": "OK"})


parser = argparse.ArgumentParser(description='CERTainly Core Trans Server')
parser.add_argument('--host', type=str, default="0.0.0.0", help='Host to use')
parser.add_argument('--port', type=int, default=8778, help='Port to use')
parser.add_argument('--reloader', type=bool, default=False, help='Using reloader')
args = parser.parse_args()

if __name__ == '__main__':
  # https://werkzeug.palletsprojects.com/en/3.0.x/serving/#werkzeug.serving.run_simple
  app.run(host=args.host, port=int(args.port), use_reloader=args.reloader, debug=True, threaded=True)
