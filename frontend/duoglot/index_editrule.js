"use strict";

document.body.style.zoom = "90%";

require.config({ paths: { vs: '../_common/monaco/node_modules/monaco-editor/min/vs' } });

let monaco_language_name_dict = {
  "js": "javascript",
  "py": "python",
  "java": "java",
  "cs": "csharp",
  "cpp": "cpp",
  "snart": "scheme",
  "log": "log",
};

let load_btn = document.getElementById("load-btn");
let save_btn = document.getElementById("save-btn");
let copyurl_btn = document.getElementById("copyurl-btn");
let edit_in_raw_btn = document.getElementById("code-viewer0-edit-btn");

let codepath_input0_elem = document.getElementById("codepath-input0");
let monaco_rule_viewer_elem = document.getElementById("code-viewer0");
let monaco_rule_editor_elem = document.getElementById("code-editor0");
let monaco_example_editor_elem = document.getElementById("code-viewer1");
let monaco_rule_diff_viewer_elem = document.getElementById("code-viewer-diff0");
let fullscreen_editor_elem = document.getElementById("fullscreen-editor");
let fullscreen_editor_discard_btn = document.getElementById("fullscreen-editor-discard-btn");
let fullscreen_editor_savereload_btn = document.getElementById("fullscreen-editor-savereload-btn");
let monaco_rule_viewer_obj = null;
let monaco_rule_editor_obj = null;
let monaco_rule_diff_editor_obj = null;
let monaco_example_editor_obj = null;

let rule_visual_list_wrapper_elem = document.getElementById("rule-visual-list-wrapper");
let single_rule_visual_wrapper_elem = document.getElementById("single-rule-visual-wrapper");

let status_labels_elem_dict = {
  "status-bar-error-msg": null
}

//////////////// api /////////////////////
window.externalListeners = {
  onSaveAsync: null
};

window.externalFunctions = {};

window.setExternalListener = function (eventname, handler) {
  if (!(eventname in window.externalListeners)) throw Error("setExternalListener Unknown event: " + eventname);
  window.externalListeners[eventname] = handler;
}

window.setExternalFunction = function (functionName, func) {
  window.externalFunctions[functionName] = func;
}

window.getAllRuleQueries = function (basedepth=2) {
  return get_rules_queries(window._rules, basedepth)
}

window.queryRuleIdxs = function (rule_query) {
  return query_rule_idxs_from_rules(window._rules, rule_query);
}

window.getRuleByIdx = function (idx) {
  return window._rules[idx];
}

window.getRuleStat = function (initialqueries=[]) {
  return calculate_rule_stat(window._rules, initialqueries);
}

window.getRuleSnippetStat = function () {
  return calculate_rule_snippet_stat(window._rules);
}

window.API = {
  loadFileAsync: _loadFileAsync,
  queryRuleIdxs: window.queryRuleIdxs,
  getAllRuleQueries: window.getAllRuleQueries,
  getRuleByIdx: window.getRuleByIdx,
  getRuleStat: window.getRuleStat,
  getRuleSnippetStat: window.getRuleSnippetStat
};

window.help = function() {
  console.log(`
  getAllRuleQueries(basedepth=2)
  queryRuleIdxs(rule_query)
  getRuleByIdx(idx)
  getRuleStat()
  getRuleSnippetStat()
  `)
};

////////////////// utils ///////////////////
window._getExternalFunction = function (functionName) {
  if (!(functionName in window.externalFunctions)) throw Error("_getExternalFunction not found: " + functionName);
  return window.externalFunctions[functionName];
}

async function _loadFileAsync(filepath) {
  codepath_input0_elem.value = filepath;
  await loadHandlerAsync();
}

function toast_info(infostr) {
  Toastify({
    text: infostr,
    gravity: "bottom",
    position: "center",
    className: "toast-info",
    duration: 3000
  }).showToast();
}

//////////////// internal ////////////////
for (let idkey in status_labels_elem_dict) status_labels_elem_dict[idkey] = document.getElementById(idkey);
function update_status_label(key, val, infotype = "INFO") {
  status_labels_elem_dict[key].innerText = val;
  if (infotype === "INFO") status_labels_elem_dict[key].style.backgroundColor = "white";
  else if (infotype === "WARNING") status_labels_elem_dict[key].style.backgroundColor = "orange";
  else if (infotype === "ERROR") status_labels_elem_dict[key].style.backgroundColor = "red";
  else if (infotype === "OK") status_labels_elem_dict[key].style.backgroundColor = "white";
  else status_labels_elem_dict[key].style.backgroundColor = "purple";
}

window._IS_AUTOLOAD = false;
function readUrlHandler() {
  const urlParams = new URLSearchParams(window.location.search);
  console.log("readUrlHandler:", window.location.search);
  let setted_vals = [];
  if (urlParams.has("codepath0")) {setted_vals.push("codepath0"); codepath_input0_elem.value = urlParams.get("codepath0");}
  if (urlParams.has("autoload")) {setted_vals.push("autoload"); window._IS_AUTOLOAD = urlParams.get("autoload") === "true";}
  console.log("readUrlHandler setting:", setted_vals);
}

function copyUrlHandler() {
  let codepath0 = codepath_input0_elem.value;
  let urlparams = {
    "codepath0": codepath0,
    "autoload": true,
  };
  let url = new URL(document.URL);
  url.search = new URLSearchParams(urlparams); 
  window.history.pushState(null, "history_url", url);
  navigator.clipboard.writeText(url.toString());
  console.log("copyUrlHandler:", url.toString());
}


require(['vs/editor/editor.main'], async function () {
  monaco_register_language_log();
  readUrlHandler();
  createMonacoEditors();
  makeInputAutoComplete("codepath-input0");
  load_btn.addEventListener("click", loadHandlerAsync);
  save_btn.addEventListener("click", saveHandlerAsync);
  edit_in_raw_btn.addEventListener("click", editInRaw);
  fullscreen_editor_discard_btn.addEventListener("click", fullscreenDiscard);
  fullscreen_editor_savereload_btn.addEventListener("click", fullscreenSaveReload);
  fullscreen_editor_elem.style.display = "none";
  copyurl_btn.addEventListener("click", copyUrlHandler);
  if (window._IS_AUTOLOAD) await loadHandlerAsync();
});

let EXAMPLE_EMPTY = `
##### Translate this function from Python into JavaScript
### Python



### JavaScript



`;

// let EXAMPLE_EXAMPLE_PY_JS = `
// ##### Translate this function from Python into JavaScript
// ### Python

// print(math.sin(1.5))
// print(math.sin(x))

// ### JavaScript

// console.log(Math.sin(1.5))
// console.log(Math.sin(x))

// `;

let SOURCE_LANGUAGE = "py";
let TARGET_LANGUAGE = "js";
let IS_PARNAME_VALCHILD = (parname) => {
  if (parname.indexOf("py.comment") >= 0) return true;
  if (parname.indexOf("py.string_content") >= 0) return true;
  if (parname.indexOf("identifier") > 0) return true;
  if (parname.indexOf("string_fragment") > 0) return true;
  if (parname.indexOf("number") > 0 || parname.indexOf("integer") > 0) return true;
  if (parname.indexOf("regex_pattern") > 0) return true;
  if (parname.indexOf("regex_flags") > 0) return true;
  return false;
}

let SHOULD_INSERT_NOSTR_AFTER_STRS = (nt_name, elem_2nd) => {
  if (nt_name === "js.arrow_function") return true;
  if (nt_name === "js.method_definition"){
    console.log("SHOULD_INSERT_NOSTR_AFTER_STRS: js.method_definition elem_2nd =", elem_2nd);
    if(typeof(elem_2nd) !== "string") return true;
    else return false; //however, now it need to be inserted after static!
    //it should be: insert after all str children.
  } 
  return false;
}


function ast_to_s_expr(ast_node, depth_val, is_ignore_str) {
  if (ast_node === null)
    return ["null", ["input is null."]];

  let logs = [];
  function _log() { logs.push(Array.from(arguments).join(" ")); }
  _log("depth_val:", depth_val, " is_ignore_str:", is_ignore_str);

  function _s_expr_rec(ast_node, parname, depth) {
    if (depth >= depth_val) {
      _log("ignoring node at", depth)
      return "...";
    }
    if (Array.isArray(ast_node)) {
      if (ast_node[0] === "anno") {
        let ret_arr = ['anno '];
        for (let i = 1; i < ast_node.length; i++) {
          ret_arr.push([ast_node[i][0], ast_node[i][1]]);
        }
        return ret_arr;
      } else if (ast_node[0] === "fragment") {
        let ret_arr = ["fragment"];
        for (let i = 1; i < ast_node.length; i++) {
          ret_arr.push(_s_expr_rec(ast_node[i], ast_node[0], depth + 1));
        }
        return ret_arr;
      } else {
        let ret_arr = ['"' + ast_node[0] + '"'];
        let nostr_tbd = false;
        if (SHOULD_INSERT_NOSTR_AFTER_STRS(ast_node[0])) {
          nostr_tbd = true;
        } 
        for (let i = 2; i < ast_node.length; i++) {
          if (nostr_tbd && typeof(ast_node[i]) !== "string") {
            ret_arr.push(["nostr"]);
            nostr_tbd = false;
          }
          ret_arr.push(_s_expr_rec(ast_node[i], ast_node[0], depth + 1));
        }
        if (nostr_tbd === true) alert("What the hell? inserting nostr");
        return ret_arr;
      }
    }
    else if (typeof (ast_node) == "number") {
      _log("WARN Unexpected ast_node:", ast_node);
    }
    else {
      if (IS_PARNAME_VALCHILD(parname)) {
        return ['val', ast_node];
      } else {
        if (is_ignore_str) {
          _log("str node (ignored):", ast_node);
          return "";
        }
        return ['str', ast_node];
      }
    }
  }
  return [_s_expr_rec(ast_node, ast_node[0], 0), logs];
}

function rule_update_aggregate(rule_data) {
  rule_data["total_lc"] = rule_data["anno_ls"].length + rule_data["main_ls"].length + rule_data["blank_ls"].length;
  let total_code = rule_data["anno_ls"].concat(rule_data["main_ls"]).concat(rule_data["blank_ls"]).join("\n")
  rule_data["total_code"] = total_code;
  rule_data["summary"] = rule_data["main_ls"].join("\n");// JSON.stringify(rule_data.match) + " => " + JSON.stringify(rule_data.expand);
}

function jsonml_rulevis(rule, is_editing, modify_ui_reload_callback) {
  let rule_type = rule.type;
  let rule_match = rule.match;
  let rule_expand = rule.expand;
  
  let wildcard_refs = [];
  function push_wildcard_idx(wildcard) {
    if (wildcard === '"."') wildcard_refs.push('".' + (wildcard_refs.length + 1) + '"');
    else if (wildcard === '"*"') wildcard_refs.push('"*' + (wildcard_refs.length + 1) + '"');
    else return "UNKNOWN";
    return wildcard_refs.length;
  }
  let phstr_refs = [];
  function push_str_idx(ph) {
    if (ph === '"_str_"') phstr_refs.push('"_str' + (phstr_refs.length + 1) + '_"');
    else return "UNKNOWN";
    return phstr_refs.length;
  }
  let phval_refs = [];
  function push_val_idx(ph) {
    if (ph === '"_val_"') phval_refs.push('"_val' + (phval_refs.length + 1) + '_"');
    else return "UNKNOWN";
    return phval_refs.length;
  }

  function no_propagation_handler(e) {
    e.stopPropagation();
  }

  function _rulevis_alt_handler_gen(refarray) {
    function alt_handler(e) {
      //change rule's match/expand according to alt_key
      e.stopPropagation();
      let edit_key = e.target.__altering_keys;
      console.log("_rulevis_alt_handler:", edit_key);
      let focus_parent = rule;
      for (let i = 0; i < edit_key.length - 1; i++) focus_parent = focus_parent[edit_key[i]];
      let modifying_key = edit_key[edit_key.length - 1];
      let current = focus_parent[modifying_key];
      let match_idx = -1;
      for (let i = 0; i < refarray.length; i++) {
        if (current === refarray[i]) {match_idx = i; break;}
      }
      let new_idx = (match_idx + 1) % refarray.length;
      focus_parent[modifying_key] = refarray[new_idx];
      if(modify_ui_reload_callback) modify_ui_reload_callback();
    }
    return alt_handler;
  }
  
  let rulevis_wildcard_alt_handler = _rulevis_alt_handler_gen(wildcard_refs);
  let rulevis_str_alt_handler = _rulevis_alt_handler_gen(phstr_refs);
  let rulevis_val_alt_handler = _rulevis_alt_handler_gen(phval_refs);

  function inplace_edit_handler(e) {
    e.stopPropagation();
    console.log("inplace_edit_handler:", e.currentTarget.__altering_keys, e.currentTarget.__pattern);
    let edit_key = e.currentTarget.__altering_keys;
    let edit_string = JSON.stringify(e.currentTarget.__pattern);
    let modified_string = prompt("Edit rule segment at " + edit_key, edit_string);
    if (modified_string === null) return;
    let result = null;
    try {
      result = JSON.parse(modified_string);
    } catch (e) {
      alert("Not valid JSON. Modification not applied");
      console.warn(modified_string);
    }
    if (result !== null) {
      let focus_parent = rule;
      for (let i = 0; i < edit_key.length - 1; i++) focus_parent = focus_parent[edit_key[i]];
      let modifying_key = edit_key[edit_key.length - 1];
      focus_parent[modifying_key] = result;
      if(modify_ui_reload_callback) modify_ui_reload_callback();
    }
  }

  function _pattern_vis(pattern, is_src, depth, is_str, is_val, altering_keys) {
    if (Array.isArray(pattern)) {
      let result = ['div.rulevis-list', is_editing ? {__pattern: pattern, __altering_keys: altering_keys, ondblclick: inplace_edit_handler} : {}];
      if (depth > 1) {
        let classes = ['rulevis-hovershow'];
        if (pattern[0] === "nostr") classes.push("rulevis-nostr");
        let classes_str = classes.join(".");
        result.push(['div.' + classes_str, pattern[0]]);
        if (pattern[0] === "nostr") result.push(['div.rulevis-nostr-child']);
        for (let i = 1; i < pattern.length; i++) {
          result.push(_pattern_vis(pattern[i], is_src, depth + 1, pattern[0] === "str", pattern[0] === "val", altering_keys.concat([i])));
        }
      } else {
        for (let i = 0; i < pattern.length; i++) {
          result.push(_pattern_vis(pattern[i], is_src, depth + 1, pattern[0] === "str", pattern[0] === "val", altering_keys.concat([i])));
        }
      }
      return result;
    }
    if (is_str) {
      return [
        'div.rulevis-str', String(pattern)
      ];
    } else if (is_val) {
      return [
        'div.rulevis-val', String(pattern)
      ];
    } else {
      if (pattern === '"."') {
        return ['div.rulevis-wildcarddot', '"."', ['div.rulevis-wildcardidx', push_wildcard_idx('"."')]];
      } 
      else if (pattern === '"*"') {
        return ['div.rulevis-wildcardstar', '"*"', ['div.rulevis-wildcardidx', push_wildcard_idx('"*"')]];
      } 
      else if (pattern === '"_str_"') {
        return ['div.rulevis-phmatchstr', pattern, ['div.rulevis-stridx', push_str_idx(pattern)]]; 
      }
      else if (pattern === '"_val_"') {
        return ['div.rulevis-phmatchval', pattern, ['div.rulevis-validx', push_val_idx(pattern)]]; 
      }
      else if ((pattern.startsWith('".') || pattern.startsWith('"*')) && pattern.endsWith('"')) {
        if (is_editing) {
          return ['button.rulevis-wildref', {__altering_keys: altering_keys, onclick: rulevis_wildcard_alt_handler, ondblclick: no_propagation_handler}, pattern];
        } else {
          return ['div.rulevis-wildref', pattern];
        }
      } 
      else if (pattern.startsWith('"_str')) {
        if (is_editing) {
          return ['button.rulevis-phstrref', {__altering_keys: altering_keys, onclick: rulevis_str_alt_handler, ondblclick: no_propagation_handler}, pattern];
        } else {
          return ['div.rulevis-phstrref', pattern];
        }
      }
      else if (pattern.startsWith('"_val')) {
        if (is_editing) {
          return ['button.rulevis-phvalref', {__altering_keys: altering_keys, onclick: rulevis_val_alt_handler, ondblclick: no_propagation_handler}, pattern];
        } else {
          return ['div.rulevis-phvalref', pattern];
        }
      }
      return [
        'div.rulevis-string', String(pattern)
      ];
    }
  }
  return [
    'div.rulevis-wrapper',
    ['div.rulevis-type', rule_type],
    ['div.rulevis-match', _pattern_vis(rule_match, true, 0, false, false, ["match"])],
    ['div.rulevis-expand', _pattern_vis(rule_expand, false, 0, false, false, ["expand"])]
  ];
}


let selected_range_language = null;
let selected_range = null;
let including_fragment_infos = null;
let query_range_func = null;
let get_auto_marks_func = null;

// ~~~ contains important functions for ruleInferenceHandler()
function createMonacoEditors() {
  monaco_rule_viewer_obj = monaco.editor.create(monaco_rule_viewer_elem, {
    value: [''].join('\n'),
    language: 'scheme',
    wordWrap: "on",
    readOnly: true,
    automaticLayout: true
  });
  monaco_rule_editor_obj = monaco.editor.create(monaco_rule_editor_elem, {
    value: [''].join('\n'),
    language: 'scheme',
    wordWrap: "on",
    automaticLayout: true
  });
  monaco_example_editor_obj = monaco.editor.create(monaco_example_editor_elem, {
    value: [''].join('\n'),
    language: 'text',
    wordWrap: "on",
    automaticLayout: true
  });

  monaco_example_editor_obj.onDidChangeCursorSelection((e) => {
    let line_idx = e.selection.startLineNumber - 1;
    let language = line_idx >= source_line_offset && line_idx < target_line_offset ? SOURCE_LANGUAGE : TARGET_LANGUAGE;
    let { startLineNumber, startColumn, endLineNumber, endColumn } = e.selection;
    let list_range = [startLineNumber - 1, startColumn - 1, endLineNumber - 1, endColumn - 1];
    [selected_range, including_fragment_infos] = query_range(list_range, language); //TODO
    selected_range_language = language;
    console.log("onDidChangeCursorSelection selected_range:", selected_range);
  });

  // this block of code is presumably not used
  let is_example_editor_dirty = false;
  monaco_example_editor_obj.getModel().onDidChangeContent((event) => {
    is_example_editor_dirty = true;
  });

  let last_code = null;
  let source_ann_dict = null;
  let target_ann_dict = null;
  let source_ast_dict = null;
  let target_ast_dict = null;
  let source_line_offset = null;
  let target_line_offset = null;
  let source_segment = null;
  let target_segment = null;

  // ~~~ function for `AutoMark`
  // createMonacoEditors().get_auto_marks()
  function get_auto_marks() {
    let src_lines = source_segment.split("\n");
    let tar_lines = target_segment.split("\n");
    console.log(src_lines, source_line_offset);
    console.log(tar_lines, target_line_offset);
    let src_marks = [];
    let tar_marks = [];
    function _collect_marks(lines, adder_func) {
      for (let i = 0; i < lines.length; i++) {
        let line_trim = lines[i].trim();
        if(line_trim === "") continue;
        let col_start = 0;
        let col_end = line_trim.length;
        if(line_trim.endsWith(";")) col_end = line_trim.length - 1;
        adder_func(i, col_start, col_end);
      }
    }
    _collect_marks(src_lines, (i, col_start, col_end) => {
      src_marks.push([i + source_line_offset, col_start, i + source_line_offset, col_end])
    });
    _collect_marks(tar_lines, (i, col_start, col_end) => {
      tar_marks.push([i + target_line_offset, col_start, i + target_line_offset, col_end])
    });
    console.log("auto src_marks:", src_marks);
    console.log("auto tar_marks:", tar_marks);
    return [src_marks, tar_marks];
  }

  // set the global value
  get_auto_marks_func = get_auto_marks;

  // ~~~ this function is called inside ruleInferenceHandler()
  // createMonacoEditors().query_range()
  // PRE:
  // source_ast_dict, source_ann_dict, source_line_offset
  // target_ast_dict, target_ann_dict, target_line_offset
  function query_range(list_range, lang) {
    console.log("query_range:", list_range, lang);

    let [ast_dict, ann_dict, line_offset] = [null, null, null];

    function is_included(par_range, child_range) {
      let [psl, psc, pel, pec] = par_range;
      let [csl, csc, cel, cec] = child_range;
      if ((csl > psl || (csl == psl && csc >= psc))
        && (cel < pel || (cel == pel && cec <= pec))) return true;
      return false;
    }

    function get_range() {
      //console.log("get_range in:", ast_dict, ann_dict, line_offset);
      let included_range_info = [];
      let offsetted_list_range = [list_range[0] - line_offset, list_range[1], list_range[2] - line_offset, list_range[3]];
      for (let ast_id in ann_dict) {
        let ast_node_ann = ann_dict[ast_id];
        let ast_range = [...ast_node_ann[2], ...ast_node_ann[3]];
        //console.log("get_range check:", ast_range, offsetted_list_range);
        let check_is_included = is_included(ast_range, offsetted_list_range);
        if (check_is_included) {
          included_range_info.push([ast_id, [ast_dict[ast_id]], ast_node_ann]);
        }
      }
      console.log("get_range included_range_info:", included_range_info);
      return [list_range, included_range_info];
    }

    if (lang === SOURCE_LANGUAGE) {
      [ast_dict, ann_dict, line_offset] = [source_ast_dict, source_ann_dict, source_line_offset];
      return get_range();

    } else if (lang === TARGET_LANGUAGE) {
      [ast_dict, ann_dict, line_offset] = [target_ast_dict, target_ann_dict, target_line_offset];
      return get_range();

    } else {
      throw Error("Unsupported Language: " + lang);
    }
  }

  // set the global value
  query_range_func = query_range;

  // ~~~ this is the block of code that is run every 1000ms to parse py/js code in `monaco_example_editor_obj`
  setInterval(async () => {
    let code = monaco_example_editor_obj.getValue();
    if (last_code === code) return;
    last_code = code;
    console.log("example code has changed.");

    update_example_code_of_editing_rule(code);

    let codesegs = code.split(/\n### (.*?)\n/);
    if (codesegs.length !== 5) {
      console.warn("example code not in expected format.");
      return;
    }

    let [beforestuff, lang1, source_segment_m, lang2, target_segment_m] = codesegs;
    [source_segment, target_segment] = [source_segment_m, target_segment_m];

    let lang_dict = {"Python": "py", "JavaScript": "js"};
    if ((!(lang1 in lang_dict)) || (!(lang2 in lang_dict))) {
      console.warn("example code not in expected language: Python or JavaScript");
      return;
    }

    source_line_offset = beforestuff.split("\n").length + 1;
    target_line_offset = source_segment.split("\n").length + source_line_offset + 1;

    console.log("----- new source_segment offset:" + source_line_offset + " -----");
    console.log(source_segment);
    console.log("----- new target_segment offset:" + target_line_offset + " -----");
    console.log(target_segment);

    let astToDictRec = (ast, thedict) => {
      if (Array.isArray(ast)) {
        if (ast.length >= 1 && ast[0] === "anno") return; //this is anno
        if (ast.length <= 2) throw "ast_node_length_should_g2";
        thedict[ast[1]] = ast;
        if (ast.length > 2) {
          for (let i = 2; i < ast.length; i++) astToDictRec(ast[i], thedict);
        }
      }
    };

    // call to backend for parsing source_segment
    let [source_ast, source_ann] = await parseAsync(source_segment, lang_dict[lang1]);

    console.log("source_ast:", source_ast);
    console.log("source_ann:", source_ann);
    source_ann_dict = source_ann;
    source_ast_dict = {};
    astToDictRec(source_ast, source_ast_dict);

    // call to backend for parsing target_segment
    let [target_ast, target_ann] = await parseAsync(target_segment, lang_dict[lang2]);

    console.log("target_ast:", target_ast);
    console.log("target_ann:", target_ann);
    target_ann_dict = target_ann;
    target_ast_dict = {};
    astToDictRec(target_ast, target_ast_dict);

  }, 1000);

  monaco_rule_diff_editor_obj = null;
}

function makeInputAutoComplete(elem_id) {
  let codepath_input_elem = document.getElementById(elem_id);
  let _autocomplete_list_cache = {};
  async function _query_autocomplete_list(query) {
    let q = codepath_input_elem.value;
    let normalized_q = q.indexOf("/") >= 0 ? q.split("/").slice(0, -1).join("/") : "";
    if (normalized_q in _autocomplete_list_cache) return _autocomplete_list_cache[normalized_q];
    let resp_dict = await listDirAsync(null, normalized_q);
    let ac_list = [];
    if ("filepaths" in resp_dict) ac_list = ac_list.concat(resp_dict["filepaths"]);
    if ("dirpaths" in resp_dict) ac_list = ac_list.concat(resp_dict["dirpaths"]);
    if ("error_msg" in resp_dict) ac_list = ["NOT_VALID_FILE_PATH"];
    console.log("# _query_autocomplete_list new query:", normalized_q, resp_dict, ac_list)
    _autocomplete_list_cache[normalized_q] = ac_list;
    return _autocomplete_list_cache[normalized_q];
  }
  let filepath_autocomplete_obj = new autoComplete({
    selector: "#" + elem_id,
    placeHolder: "input filename...",
    data: {
      src: _query_autocomplete_list
    },
    resultItem: {
      highlight: {
        render: true
      }
    },
    resultsList: {
      maxResults: 3000,
      tabSelect: true
    }
  });
  console.log(
    "create filepath_autocomplete_obj:",
    filepath_autocomplete_obj);
  codepath_input_elem.addEventListener("selection", function (event) {
    // "event.detail" carries the autoComplete.js "feedback" object
    let selected_value = event.detail.selection.value;
    console.log("codepath_input_elem selection Event:", selected_value);
    codepath_input_elem.value = selected_value;
    filepath_autocomplete_obj.start(selected_value);
  });
}

function expansion_programs_to_data_list_for_sortable_elems_inplace(raw_codestr, expansion_programs, dbg_info) {
  let posfunc = string_idx_to_line_column_func_gen(raw_codestr);
  let code_lines = raw_codestr.split("\n");
  let expansion_programs_dict = {};
  let initial_rule_id_list = [];
  let initial_rule_list = [];
  for (let i = 0; i < expansion_programs.length; i++) {
    let rule_id = dbg_info["rule_ids"][i];
    expansion_programs_dict[rule_id] = expansion_programs[i];
    initial_rule_id_list.push(rule_id);
    let rule_data = expansion_programs_dict[rule_id];
    initial_rule_list.push(rule_data);
    rule_data["rule_id"] = rule_id;
    rule_data["rule_loc"] = dbg_info["rule_loc_dict"][rule_id];
    let [start_row, start_col] = posfunc(rule_data["rule_loc"][0]);
    let [end_row, end_col] = posfunc(rule_data["rule_loc"][1]);
    if (!code_lines[start_row].trim().startsWith("(")) {
      alert("File Format Not Supported by Frontend Editor: " + code_lines[start_row]);
      throw Error("Unexpected Rule Line:" + code_lines[start_row]);
    }
    start_col = 0;
    if (code_lines.length > end_row + 1 && code_lines[end_row + 1].trim() === ")") {
      end_row = end_row + 1;
      end_col = code_lines[end_row + 1] !== undefined? code_lines[end_row + 1].length - 1 : 0;
    }
    let [anno_lines, anno_start_row] = collect_dec_until(code_lines, start_row - 1, (x) => x.trim() !== "");
    let [blank_lines, blank_lines_end_row] = collect_inc_until(code_lines, end_row + 1, (x) => x.trim() === "");
    anno_lines.reverse();

    rule_data["anno_ls"] = anno_lines;
    rule_data["main_ls"] = code_lines.slice(start_row, end_row + 1);
    rule_data["blank_ls"] = blank_lines;
    rule_data["offset"] = 0;
    rule_update_aggregate(rule_data);
  }
  //return [expansion_programs_dict, initial_rule_id_list];
  return initial_rule_list;
}

function calculate_rule_snippet_stat(rules) {
  let snippets = [];
  for (let i = 0; i < rules.length; i++) {
    let rule = rules[i];
    let code = rule.total_code.split("\n").filter(x => x.startsWith("; examples:")).map(x => x.replace("; examples:", ""));
    if (code.length === 1) snippets.push(JSON.parse(code[0]));
    else if (code.length !== 0) {
      console.warn("Result not accurate. Multiple examples found:", code);
    }
  }
  let stripped_snippets = [];
  for (let snippet of snippets) {
    let afterpy = snippet.trim().split("Translate this")[1].split("### Python")[1];
    let [pycode, jscode] = afterpy.split("### JavaScript");
    if (pycode.length > 0 && jscode.length > 0) {
      pycode = pycode.trim();
      jscode = jscode.trim();
      console.log(pycode);
      console.log(jscode);
      let pylines = pycode.split("\n").filter(x => x.trim() !== "");
      let jslines = jscode.split("\n").filter(x => x.trim() !== "");
      console.log(pylines);
      console.log(jslines);
      stripped_snippets.push({
        "pylines": pylines,
        "jslines": jslines,
        "linecount": pylines.length + jslines.length
      })
    } else {
      throw Error("Unexpected snippet length:", pycode.length, jscode.length);
    }
  }
  console.log(stripped_snippets);
  let total_stats = {
    "lc": 0,
    "wc": 0,
  };
  for (let stripped of stripped_snippets) {
    let {pylines, jslines, linecount} = stripped;
    total_stats["lc"] += linecount;
    for (let c of pylines.map(x => x.replaceAll(" ", "").length)) total_stats["wc"] += c;
    for (let c of jslines.map(x => x.replaceAll(" ", "").length)) total_stats["wc"] += c;
  }
  console.log(total_stats);
}

function calculate_rule_stat(rules, initqueries=[]) {
  function scount(text, substr) {
    return text.split(substr).length - 1;
  } 
  let initrules = initqueries.map(x => window.queryRuleIdxs(x));
  let initidxs = [];
  for (let init_idxs of initrules) {
    if (init_idxs.length !== 1) console.warn("# initial rule not found or multiple:", init_idxs);
    else initidxs.push(init_idxs[0]);
  }
  let stats = [];
  for (let i = 0; i < rules.length; i++) {
    if (initidxs.indexOf(i) >= 0) continue;
    let rule = rules[i];
    let code = rule.total_code;
    let [head, srcpart, tarpart] = code.split("fragment");
    let src_star_count = scount(srcpart, '"*"') - scount(srcpart, 'str "*"') - scount(srcpart, 'str  "*"');
    let src_dot_count = scount(srcpart, '"."') - scount(srcpart, 'str "."') - scount(srcpart, 'str  "."');
    let dest_star_count = scount(tarpart, '"*') - scount(tarpart, '"."');
    let dest_dot_count = scount(tarpart, '".') - scount(tarpart, '"."');
    let src_val_count = scount(srcpart, '"_val_"');
    let src_str_count = scount(srcpart, '"_str_"');
    let dest_val_count = scount(tarpart, '"_val');
    let dest_str_count = scount(tarpart, '"_str');
    let any_liststr = scount(code, '"_liststr') > 0;
    let any_nostr = scount(code, '(nostr)') > 0;
    stats.push({
      "idx": i,
      "src_star": src_star_count,
      "src_dot": src_dot_count,
      "dest_star": dest_star_count,
      "dest_dot": dest_dot_count,
      "src_val": src_val_count,
      "src_str": src_str_count,
      "dest_val": dest_val_count,
      "dest_str": dest_str_count,
      "src_total": src_star_count + src_dot_count + src_val_count + src_str_count,
      "dest_total": dest_star_count + dest_dot_count + dest_val_count + dest_str_count,
      "any_liststr": any_liststr,
      "any_nostr": any_nostr
    });
  }
  let stat_count = {
    "simple": 0,
    "medium": 0,
    "complex": 0,
    "no_auto": 0,
    "checksum": 0
  };
  let stat_groups = {
    "simple": [],
    "medium": [],
    "complex": [],
    "no_auto": [],
    "checksum": null,
  };
  for (let stat of stats) {
    let hole_count = stat["src_total"] + stat["dest_total"];

    if (stat["any_liststr"] || stat["any_nostr"]) { stat_count["no_auto"] += 1; stat_groups["no_auto"].push(stat["idx"]);}
    //no auto rule will also be counted into simple medium and complex.
    if (hole_count <= 6) {stat_count["simple"] += 1; stat_groups["simple"].push(stat["idx"]);}
    else if (hole_count <= 9) {stat_count["medium"] += 1; stat_groups["medium"].push(stat["idx"]);}
    else {stat_count["complex"] += 1; stat_groups["complex"].push(stat["idx"]);}
    
  }
  stat_count["checksum"] = stat_count["simple"] + stat_count["medium"] + stat_count["complex"]; // + stat_count["no_auto"];
  return [stat_count, stats, stat_groups];
}

async function onRulesEditorChangeViewUpdateAsync() {
  let codestr = monaco_rule_viewer_obj.getValue();
  let [expansion_programs, dbg_info, error_msg] = await parseRulesAsync(codestr);
  console.log("rule_parse_async:", expansion_programs, dbg_info, error_msg);
  if (error_msg !== null && error_msg !== undefined) {
    update_status_label("status-bar-error-msg", error_msg, "ERROR");
  } else {
    update_status_label("status-bar-error-msg", "OK. #Rules=" + expansion_programs.length, "OK");
    let expansion_programs_list = expansion_programs_to_data_list_for_sortable_elems_inplace(codestr, expansion_programs, dbg_info);
    let [rule_stat, detailed_stats, stat_groups] = calculate_rule_stat(expansion_programs_list);
    window._rules = expansion_programs_list;
    window._rule_stat = rule_stat;
    window._rule_stat_detailed = detailed_stats;
    console.log("rule_stat_result:", rule_stat, detailed_stats);
    update_status_label("status-bar-error-msg", "OK. #Rules=" + expansion_programs.length + " stat:" + JSON.stringify(rule_stat), "OK");
    initialize_rule_visual_list(expansion_programs_list);
    
    ///// additional info output /////
    console.log("stat_groups:", stat_groups);
    let joined_stat_query_dict = {};
    for (let stat_key in stat_groups) {
      if (!Array.isArray(stat_groups[stat_key])) continue;
      let stat_rules = stat_groups[stat_key].map(x => window._rules[x]);
      let default_depth = 2; 

      try {
        let [queries, real_depths] = get_rules_queries(stat_rules, default_depth);
        for (let i = 0; i < real_depths.length; i++) {
          if (real_depths[i] !== default_depth) {
            console.warn("Inceased-depth to " + real_depths[i] + " for query:", queries[i]);
          }
        }
        joined_stat_query_dict[stat_key] = queries;
      } catch (e) {
        console.warn("Failed to generate unique rule queries.");
        console.warn(e);
      }
    }
    console.log("joined_stat_query_dict:", joined_stat_query_dict);
    console.log(JSON.stringify(joined_stat_query_dict, null, 2));
  }
}

function update_rules_code_str(codestr) {
  let editor_obj = monaco_rule_viewer_obj;
  //let lang = "scheme";
  //let codeModel = editor_obj.getModel();
  editor_obj.setValue(codestr);
  //console.log(codestr.slice(0, 400));
}

function update_example_str(example_str) {
  monaco_example_editor_obj.setValue(example_str);
}

async function saveHandlerAsync() {
  let editor_obj = monaco_rule_viewer_obj;
  let current_code = editor_obj.getValue();
  let current_path = codepath_input0_elem.value;
  Toastify({
    text: "Saving current rules to " + current_path + " ...",
    gravity: "bottom",
    position: "center",
    className: "toast-info",
    duration: 3000
  }).showToast();
  let result = await saveAnyTextfileAsync(current_path, current_code);
  Toastify({
    text: "Saving response: " + result,
    gravity: "bottom",
    position: "center",
    className: "toast-info",
    duration: 3000
  }).showToast();
  if (window.externalListeners.onSaveAsync) {
    await window.externalListeners.onSaveAsync();
  }
}

function editInRaw() {
  let rulecode = monaco_rule_viewer_obj.getValue();
  monaco_rule_editor_obj.setValue(rulecode);
  document.getElementById("fullscreen-editor").style.display = "block";
}

function fullscreenDiscard() {
  document.getElementById("fullscreen-editor").style.display = "none";
}

function fullscreenSaveReload () {
  let rulecode = monaco_rule_editor_obj.getValue();
  monaco_rule_viewer_obj.setValue(rulecode);
  (async function () {
    await saveHandlerAsync();
    await loadHandlerAsync();
    document.getElementById("fullscreen-editor").style.display = "none";
  })();
}

async function loadHandlerAsync() {
  async function _loadHandleAsync() {
    let codepath_elem = codepath_input0_elem;
    let anyfile_path = codepath_elem.value.trim();
    if (anyfile_path === "") {
      console.log("_loadHandleAsync empty path:", idx);
      return;
    }
    toast_info("Load code file " + anyfile_path + "...")
    let codestr = null;
    try {
      codestr = await anyfileAsync(anyfile_path);
    } catch (e) {
      codestr = "FAILED_TO_LOAD\n" + e;
      alert(codestr);
    }
    update_rules_code_str(codestr);
    await onRulesEditorChangeViewUpdateAsync();
    initialize_single_rule_visual();
    toast_info("Loaded. length: " + codestr.length);
    console.log("_loadHandleAsync rules_str_length:", codestr.length);
  }
  _loadHandleAsync();
}

function collect_rules_list() {
  let rules_list = Array.from(rule_visual_list_wrapper_elem.firstChild.children).map(x => x.__data);
  return rules_list;
}

let new_rule_idx = 0;
function fix_rules_list(rules_list) {
  for (let rule of rules_list) {
    if (String(rule.rule_id).endsWith("_editing") || rule.rule_id === "new") {
      rule.rule_id = "new_" + new_rule_idx;
      new_rule_idx += 1;
    }
  }
}

let rule_edit_save_func = null;
let rule_edit_func = null;
function initialize_rule_visual_list(initial_rules_list) {
  // a serializable central state
  let initial_state = initial_rules_list;
  function ruleOnDeleteHandler(e) {
    let deleting_key = e.target.__incrementalDOMData.key;
    let deleting_rule_id = deleting_key.replace("btn_del_", "");
    console.log("ruleOnDeleteHandler:", deleting_rule_id);
    let rule_list = collect_rules_list().filter(x => String(x.rule_id) !== deleting_rule_id);
    updateWithNewRulesList(rule_list);
  }
  function ruleOnEditHandler(e) {
    let edit_key = e.target.__incrementalDOMData.key;
    let editing_rule_id = edit_key.replace("btn_edit_", "");
    console.log("ruleOnEditHandler:", editing_rule_id);
    let rule_list = collect_rules_list().filter(x => String(x.rule_id) === editing_rule_id);
    if (rule_list.length !== 1) {
      throw Error("Unexpected Error. Not 1 rule with id " + editing_rule_id);
    }
    let editing_rule = rule_list[0];
    rule_edit_func(editing_rule);
  }
  rule_edit_save_func = (rule) => {
    let rule_copy = JSON.parse(JSON.stringify(rule));
    console.log("rule_edit_save_func:", rule_copy);
    let rule_id = rule_copy.rule_id;
    if (!rule_id.endsWith("_editing")) throw Error("Unexpected. rule_edit_save_func is not editing.");
    let corres_rule_id = rule_id.replace("_editing", "");
    rule_copy.rule_id = corres_rule_id + "_modified";
    let copy_rule_list = [...collect_rules_list()];
    let is_rule_replaced = false;
    for (let i = 0; i < copy_rule_list.length; i++) {
      let inlist_rule = copy_rule_list[i];
      if (String(inlist_rule.rule_id) === corres_rule_id ||
        String(inlist_rule.rule_id) === corres_rule_id + "_modified") {
        copy_rule_list[i] = rule_copy;
        is_rule_replaced = true;
        break;
      }
    }
    if (!is_rule_replaced) {
      alert("Saving rule failed. doesn't exist.");
    } else {
      updateWithNewRulesList(copy_rule_list);
    }
  }
  // fragments
  function list_item(data) {
    return [
      'div.list-group-item', { key: "item_" + data.rule_id, __data: data },
      ['div.item-right-side',
        ['button.right-side-btn', { key: "btn_edit_" + data.rule_id, onclick: ruleOnEditHandler }, "Edit"],
        ['button.right-side-btn', { key: "btn_del_" + data.rule_id, onclick: ruleOnDeleteHandler }, "(X)"],
        ['span', " (" + (data.offset + 1) + "-" + (data.offset + data.total_lc) + ")"],
        ['span.badge', "id: " + data.rule_id]
      ],
      //['span', data.type],
      jsonml_rulevis(data, false),
    ];
  }

  function list(rules) {
    let offset = 0;
    let result_list = [];
    for (let rule of rules) {
      rule.offset = offset;
      result_list.push(list_item(rule, offset));
      offset = rule.offset + rule.total_lc;
    }
    return result_list;
  }

  function app(s) {
    return ['div#rule-visual-list.list-group', { key: "rule-visual-list" }].concat(list(s))
  }

  function updateWithNewRulesList(new_rules_list) {
    console.log("updateWithNewRulesList:", new_rules_list);
    let rules_codestr = new_rules_list.map(x => x.total_code).join("\n");
    IncrementalDOM.patch(rule_visual_list_wrapper_elem, jsonml2idom, app(new_rules_list));
    update_rules_code_str(rules_codestr);
  }

  // render update
  function update() {
    IncrementalDOM.patch(rule_visual_list_wrapper_elem, jsonml2idom, app(initial_state));
    let rule_visual_list_elem = rule_visual_list_wrapper_elem.firstChild;
    window._rule_visual_list_elem = rule_visual_list_elem;
    Sortable.create(rule_visual_list_elem, {
      // handle: '.handle-move',
      group: {
        name: 'shared',
        pull: 'clone'
      },
      animation: 150,
      onUpdate: function () {
        let new_rules_list = collect_rules_list();
        updateWithNewRulesList(new_rules_list);
      },
      onAdd: function () {
        let new_rules_list = collect_rules_list();
        fix_rules_list(new_rules_list);
        updateWithNewRulesList(new_rules_list);
      },
    });
  }
  console.log("update_rule_visual_list updating...");
  update();
}

function collect_single_rule_list() {
  let single_rule_list = Array.from(single_rule_visual_wrapper_elem.firstChild.children[1].children).map(x => x.__data);
  return single_rule_list;
}

function get_single_rule_data_focused() {
  let single_rule_list = collect_single_rule_list();
  return single_rule_list[0];
}


function get_anno_data(rule, key, defaultval) {
  let lines = rule.anno_ls;
  if (lines === null || lines === undefined) return defaultval;
  let prefix = "; " + key + ":";
  for (let line of lines) {
    if (line.startsWith(prefix)) return JSON.parse(line.replace(prefix, ""));
  }
  return defaultval;
}

function set_anno_data(rule, key, data) {
  if (rule.anno_ls === null || rule.anno_ls === undefined) rule.anno_ls = [];
  let lines = rule.anno_ls;
  let prefix = "; " + key + ":";
  let dataline = prefix + " " + JSON.stringify(data);
  for (let i = 0; i < lines.length; i++) {
    if (lines[i].startsWith(prefix)) {
      lines[i] = dataline;
      rule_update_aggregate(rule);
      return;
    }
  }
  lines.push(dataline);
  rule_update_aggregate(rule);
}

function add_mark(rule_data, mark_range, is_source) {
  let anno_dict = get_anno_data(rule_data, "mark", {});
  if (!("source" in anno_dict)) anno_dict["source"] = [];
  if (!("target" in anno_dict)) anno_dict["target"] = [];
  if (is_source) anno_dict["source"].push(mark_range);
  else anno_dict["target"].push(mark_range);
  set_anno_data(rule_data, "mark", anno_dict);
}

function delete_mark(rule_data, mark_key, mark_idx) {
  let anno_dict = get_anno_data(rule_data, "mark", null);
  anno_dict[mark_key].splice(mark_idx, 1);
  set_anno_data(rule_data, "mark", anno_dict);
}

function set_rule_example_code(rule_data, example_code) {
  set_anno_data(rule_data, "examples", example_code);
  console.log("set_rule_example_code called.", rule_data);
}

function get_rule_example_code_or_default(rule_data) {
  return get_anno_data(rule_data, "examples", EXAMPLE_EMPTY);
}


let updateWithNewSingleRulesList_func = null;
function update_example_code_of_editing_rule(example_code) {
  if (updateWithNewSingleRulesList_func !== null) {
    let focusing_rule = get_single_rule_data_focused();
    set_rule_example_code(focusing_rule, example_code);
    updateWithNewSingleRulesList_func([focusing_rule]);
  }
}


// ~~~ contains important functions for ruleInferenceHandler()
function initialize_single_rule_visual() {
  // a serializable central state
  let placeholder_rule = {
    key: "no_id",
    rule_id: "no_id",
    offset: 0,
    total_lc: 0,
    total_code: "",
    anno_ls: [],
    main_ls: [],
    blank_ls: [],
    type: null,
    summary: null,
    note: "No rule is editing. Please edit an existing rule or create a new rule."
  };

  function get_total_lc(rule_data) {
    return rule_data["anno_ls"].length + rule_data["main_ls"].length + rule_data["blank_ls"].length;
  }
  function get_total_code(rule_data) {
    return rule_data["anno_ls"].concat(rule_data["main_ls"]).concat(rule_data["blank_ls"]).join("\n");
  }

  let new_rule_template = {
    key: "new",
    rule_id: "new",
    offset: 0,
    anno_ls: [],
    match: [],
    expand: [],
    main_ls: ["(match_expand)"],
    blank_ls: [""],
    type: "match_expand",
  };
  new_rule_template["total_lc"] = get_total_lc(new_rule_template);
  new_rule_template["total_code"] = get_total_code(new_rule_template);

  let initial_state = [placeholder_rule];

  // ~~~ "Create New Rule" button handler (STEP 1)
  function newRuleHandler(e) {
    let new_rule = JSON.parse(JSON.stringify(new_rule_template));
    updateWithNewSingleRulesList([new_rule]);
    update_example_str(get_rule_example_code_or_default(new_rule));
  }

  // ~~~ "Mark" button handler
  function onMarkHandler(e) {
    if (selected_range === null || selected_range === undefined) {
      alert("Nothing to mark.");
      return;
    }
    let focused_rule = get_single_rule_data_focused();
    if (focused_rule.rule_id === "no_id") {
      alert("Please edit or create a rule first.");
      return;
    }
    if (selected_range_language === SOURCE_LANGUAGE) {
      add_mark(focused_rule, selected_range, true);
    } else {
      add_mark(focused_rule, selected_range, false);
    }
    updateWithNewSingleRulesList([focused_rule]);
  }

  // ~~~ "AutoMark" button handler (STEP 2)
  function onAutoMarkHandler(e) {
    let focused_rule = get_single_rule_data_focused();
    if (focused_rule.rule_id === "no_id") {
      alert("Please edit or create a rule first.");
      return;
    }
    let [src_selected_ranges, tar_selected_ranges] = get_auto_marks_func();
    for (let src_selected_range of src_selected_ranges) add_mark(focused_rule, src_selected_range, true);
    for (let tar_selected_range of tar_selected_ranges) add_mark(focused_rule, tar_selected_range, false);
    updateWithNewSingleRulesList([focused_rule]);
  }

  function unifying_ast_fragments(ast_fragments, wildcard_ph_func) {
    //TODO
    let fragments = ast_fragments.map((ast_fragment) => ["fragment", ...ast_fragment]);
    let sexpr_log_results = fragments.map((ast_node) => ast_to_s_expr(ast_node, 100, false));
    let sexprs = sexpr_log_results.map((x) => x[0]);
    console.log("unifying_ast_fragments fragments:", fragments, " sexprs:", sexprs);
    
    function _common_root_tree(sexprs) {
      let all_names = sexprs.map(x => x[0]);
      for (let name of all_names) {
        if (name !== all_names[0]) {
          return ["ERROR_DIFF_NAME"];
        }
      }

      if (all_names[0] === "str") {
        let common_val = sexprs[0][1];
        for (let sexpr of sexprs) {
          if (sexpr.length !== 2) {
            return ["ERROR_STR_NODE_LENGTH"];
          }
          if (sexpr[1] !== common_val) {
            return wildcard_ph_func("_str_", sexprs);
          }
        }
        return ["str", common_val];
      }
      else if (all_names[0] === "val") {
        let common_val = sexprs[0][1];
        for (let sexpr of sexprs) {
          if (sexpr.length !== 2) {
            return ["ERROR_VAL_NODE_LENGTH"];
          }
          if (String(sexpr[1]) !== String(common_val)) {
            return wildcard_ph_func("_val_", sexprs);
          }
        }
        return ["val", common_val];
      }
      else {
        let is_nt_name = (ntname) => (ntname.startsWith('"') && (ntname.indexOf(".") > 0));
        let is_nt = is_nt_name(all_names[0]);
        let is_fragment = all_names[0] === "fragment";
        let is_nostr = all_names[0] === "nostr";
        if ((!is_nt) && (!is_fragment) && (!is_nostr)) return ["ERROR_NT_OR_FRAGMENT_EXPECTED"];
  
        let common_root = [all_names[0]];
        let i = 1;
        for(;;i++) {
          let ith_elems = sexprs.map(x => x[i]);
          let common_val = ith_elems[0];
          if (common_val === undefined) {
            if(ith_elems.some((x) => x !== undefined)) {
              common_root.push(wildcard_ph_func("*", sexprs));
            }
            break;
          }
  
          let common_type = typeof common_val;
          if (common_type === "string" || common_type === "number") {
            common_root.push("ERROR_UNEXPECTED_STRING_OR_NUMBER");
            return common_root;
          }
          let common_is_arr = Array.isArray(common_val);
          if (!common_is_arr) {
            common_root.push("ERROR_UNEXPECTED_NON_ARRAY_CHILD");
            return common_root;
          }
          let common_is_nt = is_nt_name(common_val[0]);
          let common_name = common_val[0];
          let name_diff_found = false;
          let all_nt = common_is_nt;
          for (let j = 1; j < ith_elems.length; j++) {
            let look_val = ith_elems[j];
            let look_is_arr = Array.isArray(look_val);
            if(!look_is_arr) {
              common_root.push("ERROR_UNEXPECTED_NON_ARRAY_CHILD");
              return common_root;
            }
            if (common_name !== look_val[0]) name_diff_found = true;
            if ((common_is_nt) && !is_nt_name(look_val[0])) all_nt = false;
          }
          if (all_nt) {
            if (name_diff_found) common_root.push(wildcard_ph_func(".", ith_elems));
            else common_root.push(_common_root_tree(ith_elems));
          } else {
            if (name_diff_found) {
              common_root.push(wildcard_ph_func("*", sexprs));
              break;
            } else {
              common_root.push(_common_root_tree(ith_elems));
            }
          }
        }
        return common_root;
      }
    }
    let unified = _common_root_tree(sexprs);
    unified.push(wildcard_ph_func("*", "TAIL"));
    console.log("Unifying result:", unified);
    return unified;
  }

  // ~~~ "Inference" button handler (STEP 3 - main)
  async function ruleInferenceHandler(e) {
    console.log("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
    console.log("starting rule inference");

    let focus_rule = get_single_rule_data_focused();
    let anno_data = get_anno_data(focus_rule, "mark", null);

    if (anno_data !== null) {
      let source_marks = anno_data["source"];
      let target_marks = anno_data["target"];

      let source_query_results = source_marks.map((range) => query_range_func(range, SOURCE_LANGUAGE));
      let target_query_results = target_marks.map((range) => query_range_func(range, TARGET_LANGUAGE));

      console.log("source_query_results:", source_query_results);
      console.log("target_query_results:", target_query_results);

      let src_phs = [];
      let src_tpl_phs = {"_str_": [], "_val_": []};

      // TODO what does this function do?
      let src_wildcard_ph_func = (x, diffing_list) => {
        if (x === "." || x === "*") src_phs.push([x, diffing_list]);
        else if (x in src_tpl_phs) src_tpl_phs[x].push([x, diffing_list]);
        else console.warn("# ruleInferenceHandler src_wildcard_ph_func Unknown ph:", x);
        return '"' + x + '"';
      };

      let tar_phs = [];
      let tar_tpl_phs = {"_str_": [], "_val_": []};

      // TODO what does this function do?
      let tar_wildcard_ph_func = (x, diffing_list) => {
        if (x === "." || x === "*") {
          tar_phs.push([x, diffing_list]);
          return '"' + x + `PH${tar_phs.length}"`;
        }
        else if (x in tar_tpl_phs) {
          tar_tpl_phs[x].push([x, diffing_list]);
          return x === "_str_" ? `"_strPH${tar_tpl_phs[x].length}_"` : `"_valPH${tar_tpl_phs[x].length}_"`;
        }
        else {
          console.warn("# ruleInferenceHandler tar_wildcard_ph_func Unknown ph:", x);
          return '"' + x + '"';
        }
      };

      let src_fragment_infos = source_query_results.map((x) => x[1][x[1].length - 1]);
      let src_fragments = src_fragment_infos.map((x) => x[1]);
      let src_unified_pattern = unifying_ast_fragments(src_fragments, src_wildcard_ph_func);

      let tar_fragment_infos = target_query_results.map((x) => x[1][x[1].length - 1]);
      let tar_gragments = tar_fragment_infos.map((x) => x[1]);
      let tar_unified_pattern = unifying_ast_fragments(tar_gragments, tar_wildcard_ph_func);
      
      console.log("# ruleInferenceHandler src_phs:", src_phs);
      console.log("# ruleInferenceHandler src_tpl_phs:", src_tpl_phs);
      console.log("# ruleInferenceHandler tar_phs:", src_phs);
      console.log("# ruleInferenceHandler tar_tpl_phs:", tar_tpl_phs);

      let phs_compare = await computeTreeDistancesAsync(src_phs, tar_phs, null);
      let str_compare = await computeTreeDistancesAsync(src_tpl_phs["_str_"], tar_tpl_phs["_str_"], "EXACT");
      let val_compare = await computeTreeDistancesAsync(src_tpl_phs["_val_"], tar_tpl_phs["_val_"], "EXACT");

      console.log("# ruleInferenceHandler phs_compare:", phs_compare);
      console.log("# ruleInferenceHandler str_compare:", str_compare);
      console.log("# ruleInferenceHandler val_compare:", val_compare);

      // TODO what does this function do?
      function get_min_idxes(dist_matrix) {
        let result = [];
        for (let i = 0; i < dist_matrix.length; i++) {
          let row = dist_matrix[i];
          let minVal = Infinity;
          let minIdx = -1;
          for (let j = 0; j < row.length; j++) {
            if (row[j] < minVal) {
              minVal = row[j];
              minIdx = j;
            }
          }
          result.push(minIdx);
        }
        return result;
      }

      // TODO: compute ph with minimal distance.
      function set_ph(pattern, search_ph, replace_ph) {
        if(Array.isArray(pattern)) {
          return pattern.map(x => set_ph(x, search_ph, replace_ph));
        }
        if (typeof pattern !== "string") throw Error("set_ph expect nested string or array.");
        if (pattern === search_ph) return replace_ph;
        return pattern;
      }

      let phs_match_idxes = get_min_idxes(phs_compare);
      let str_match_idxes = get_min_idxes(str_compare);
      let val_match_idxes = get_min_idxes(val_compare);

      console.log("phs_match_idxes:", phs_match_idxes);
      console.log("str_match_idxes:", str_match_idxes);
      console.log("val_match_idxes:", val_match_idxes);
      
      for (let i = 0; i < phs_match_idxes.length; i++) {
        tar_unified_pattern = set_ph(tar_unified_pattern, '"*PH' + String(i + 1) + '"', '"*' + String(phs_match_idxes[i] + 1) + '"');
        tar_unified_pattern = set_ph(tar_unified_pattern, '".PH' + String(i + 1) + '"', '".' + String(phs_match_idxes[i] + 1) + '"');
      }

      for (let i = 0; i < str_match_idxes.length; i++) {
        tar_unified_pattern = set_ph(tar_unified_pattern, '"_strPH' + String(i + 1) + '_"', '"_str' + String(str_match_idxes[i] + 1) + '_"');
      }

      for (let i = 0; i < val_match_idxes.length; i++) {
        tar_unified_pattern = set_ph(tar_unified_pattern, '"_valPH' + String(i + 1) + '_"', '"_val' + String(val_match_idxes[i] + 1) + '_"');
      }
      
      focus_rule.match = src_unified_pattern;
      focus_rule.expand = tar_unified_pattern;

      let pretty_code = pretty_rule(focus_rule);
      focus_rule.main_ls = pretty_code.trim().split("\n");

      rule_update_aggregate(focus_rule);
      // after updating focus_rule, repaint
      updateWithNewSingleRulesList([focus_rule]);

    } else {
      alert("Current rule has no marks. Please mark pattern observations in the example code.");
      return;
    }
  }

  function ruleOnSaveEditHandler(e) {
    let edit_key = e.target.__incrementalDOMData.key;
    let saving_rule_id = edit_key.replace("btn_saveedit_", "");
    console.log("ruleOnSaveEditHandler:", saving_rule_id);
    let rule_list = collect_single_rule_list().filter(x => String(x.rule_id) === saving_rule_id);
    if (rule_list.length !== 1) { throw Error("Unexpected Error. Not 1 rule with id " + saving_rule_id); }
    let saving_rule = rule_list[0];
    rule_edit_save_func(saving_rule);
  }

  function markOnDeleteHandler(e) {
    let deleting_key = e.target.__incrementalDOMData.key;
    let [_, mark_key, mark_idx] = deleting_key.split("_");
    console.log("markOnDeleteHandler:", deleting_key);
    let focused_rule = get_single_rule_data_focused();
    if (focused_rule.rule_id === "no_id") {
      alert("Please edit or create a rule first.");
      return;
    }
    delete_mark(focused_rule, mark_key, mark_idx);
    updateWithNewSingleRulesList([focused_rule]);
  }

  function single_rule_modify_ui_reload() {
    let focused_rule = get_single_rule_data_focused();
    let pretty_code = pretty_rule(focused_rule);
    focused_rule.main_ls = pretty_code.trim().split("\n");
    rule_update_aggregate(focused_rule);
    updateWithNewSingleRulesList([focused_rule]);
  }

  // fragments
  function controls() {
    return [
      'div.single-control-bar', { key: "ctrl_bar" },
      ['div.single-control-right-side'],
      ['span.single-control-caption', "Single Rule Edit"],
      ['button.single-control-btn', { key: "btn_new_rule", onclick: newRuleHandler }, "Create New Rule"],
      ['button.single-control-btn', { key: "btn_mark", onclick: onMarkHandler }, "Mark"],
      ['button.single-control-btn', { key: "btn_automark", onclick: onAutoMarkHandler }, "AutoMark"],
      ['button.single-control-btn', { key: "btn_inference", onclick: ruleInferenceHandler }, "Inference"],
      //['button', { key: "btn_edit_source" }, "(dev) Edit Source"]
    ];
  }
  
  function list_item(data) {
    let is_editing_rule = data.rule_id.endsWith("_editing");
    let anno_example_str = get_anno_data(data, "examples", null);
    let anno_mark_data = get_anno_data(data, "mark", null);
    let anno_jsonml = ['div.single-item-anno'];
    let head_info = "Total Length: " + data.total_code.length;
    if (anno_example_str !== null) {
      head_info += "  Example Code Length: " + anno_example_str.length;;
    }
    if (data.rule_id !== "no_id") anno_jsonml.push(['div.anno-row', ["span.anno-row-label", head_info]]);
    if (anno_mark_data !== null && data.rule_id !== "no_id") {
      function anno_mark_range(range, markey, idx) {
        return ['div.mark-range', { key: idx },
          JSON.stringify(range),
          ["button.btn-delete-mark", { key: "btn_" + markey + "_" + idx, onclick: markOnDeleteHandler }, "X"]
        ];
      }
      anno_jsonml.push(['div.anno-row', ["span.anno-row-label", "Source Marks:  "]].concat(anno_mark_data.source.map((range, idx) => anno_mark_range(range, "source", idx))));
      anno_jsonml.push(['div.anno-row', ["span.anno-row-label", "Target Marks:  "]].concat(anno_mark_data.target.map((range, idx) => anno_mark_range(range, "target", idx))));
    }
    return [
      'div.single-list-group-item', { key: "item_" + data.rule_id, __data: data },
      (!is_editing_rule) ? ['div.single-item-right-side',
        ['span.badge', "id: " + data.rule_id]
      ] : ['div.single-item-right-side',
        ['button', { key: "btn_saveedit_" + data.rule_id, onclick: ruleOnSaveEditHandler }, "Save Edit"],
        ['span.badge', "id: " + data.rule_id]
      ],
      anno_jsonml,
      ['div',
        //['span', data.type],
        //['span', " (" + (data.offset + 1)],
        //['span', "," + (data.offset + data.total_lc) + ") "],
        data.rule_id === "no_id" ? ['span', data.note] : jsonml_rulevis(data, true, single_rule_modify_ui_reload),
      ]
    ];
  }

  function list(rules) {
    let offset = 0;
    let result_list = [];
    for (let rule of rules) {
      rule.offset = offset;
      result_list.push(list_item(rule, offset));
      offset = rule.offset + rule.total_lc;
    }
    return result_list;
  }

  function app(s) {
    return ["div",
      controls(),
      ['div#rule-visual-list.list-group', { key: "rule-visual-list" }].concat(list(s))
    ]
  }

  function updateWithNewSingleRulesList(new_single_rules_list) {
    console.log("updateWithNewSingleRulesList:", new_single_rules_list);
    IncrementalDOM.patch(single_rule_visual_wrapper_elem, jsonml2idom, app(new_single_rules_list));
  }
  updateWithNewSingleRulesList_func = updateWithNewSingleRulesList;

  rule_edit_func = (rule) => {
    let rule_copy = JSON.parse(JSON.stringify(rule));
    let str_rule_id = String(rule_copy.rule_id);
    rule_copy.rule_id = str_rule_id.replace("_modified", "") + "_editing";
    updateWithNewSingleRulesList([rule_copy]);
    update_example_str(get_rule_example_code_or_default(rule_copy));
  };

  // render update
  function update() {
    IncrementalDOM.patch(single_rule_visual_wrapper_elem, jsonml2idom, app(initial_state));
    let single_rule_visual_elem = single_rule_visual_wrapper_elem.firstChild.childNodes[1];
    window._single_rule_visual_elem = single_rule_visual_elem;

    let cloning_data_copy = null;
    Sortable.create(single_rule_visual_elem, {
      // handle: '.handle-move',
      group: {
        name: 'shared',
        pull: 'clone',
        put: false
      },
      // swap: true, // Enable swap mode
      // swapClass: "sortable-swap-highlight",
      animation: 150,
      onUpdate: function () {
        let new_rules_list = collect_single_rule_list();
        updateWithNewSingleRulesList(new_rules_list);
      },
      onChange: function (e) {
        console.log("onChange!", e.target.__incrementalDOMData);
      },
      onClone: function (e) {
        let origEl = e.item;
        //let cloneEl = e.clone;
        console.log("onCloneData:", origEl.__data, origEl.__incrementalDOMData);
        cloning_data_copy = JSON.parse(JSON.stringify(origEl.__data));
      },
      onRemove: function (e) {
        console.log("onRemove, re-render with copy:", cloning_data_copy);
        setTimeout(() => updateWithNewSingleRulesList([cloning_data_copy]), 0);
      }
    });
  }
  console.log("update_single_rule_visual updating...");
  update();
  update_example_str(EXAMPLE_EMPTY);
}
