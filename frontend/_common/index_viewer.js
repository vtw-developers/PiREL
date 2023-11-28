"use strict";

require.config({ paths: { vs: './monaco/node_modules/monaco-editor/min/vs' } });

let monaco_language_name_dict = {
  "js": "javascript",
  "py": "python",
  "java": "java",
  "cs": "csharp",
  "cpp": "cpp",
  "log": "log",
};

let load_btn = document.getElementById("load-btn");
let copyurl_btn = document.getElementById("copyurl-btn");

let monaco_editor_elems = [
  document.getElementById("code-viewer0"),
  document.getElementById("code-viewer1"),
  document.getElementById("code-viewer2")
];

let monaco_editor_objs = [];

let codepath_input_elems = [
  document.getElementById("codepath-input0"),
  document.getElementById("codepath-input1"),
  document.getElementById("codepath-input2")
];

require(['vs/editor/editor.main'], function () {
  createMonacoEditors();
  makeInputAutoComplete("codepath-input0");
  makeInputAutoComplete("codepath-input1");
  makeInputAutoComplete("codepath-input2");
  load_btn.addEventListener("click", loadHandlerAsync);
  copyurl_btn.addEventListener("click", copyUrlHandler);
  setTimeout(readUrlHandler, 1000);
});

function readUrlHandler() {
  const urlParams = new URLSearchParams(window.location.search);
  console.log("readUrlHandler:", window.location.search);
  let setted_vals = [];
  if (urlParams.has("codepath0")) {setted_vals.push("codepath0"); codepath_input_elems[0].value = urlParams.get("codepath0");}
  if (urlParams.has("codepath1")) {setted_vals.push("codepath1"); codepath_input_elems[1].value = urlParams.get("codepath1");}
  if (urlParams.has("codepath2")) {setted_vals.push("codepath2"); codepath_input_elems[2].value = urlParams.get("codepath2");}
  if (urlParams.has("autoload")) {setted_vals.push("autoload"); if (urlParams.get("autoload") === "true") setTimeout(() => load_btn.click(), 500);}
  console.log("readUrlHandler setting:", setted_vals);
}


function copyUrlHandler() {
  let codepath0 = codepath_input_elems[0].value;
  let codepath1 = codepath_input_elems[1].value;
  let codepath2 = codepath_input_elems[2].value;
  let urlparams = {
    "codepath0": codepath0,
    "codepath1": codepath1,
    "codepath2": codepath2,
    "autoload": true,
  };
  let url = new URL(document.URL);
  url.search = new URLSearchParams(urlparams); 
  window.history.pushState(null, "history_url", url);
  navigator.clipboard.writeText(url.toString());
  console.log("copyUrlHandler:", url.toString());
}


function createMonacoEditors() {
  for (let monaco_editor_elem of monaco_editor_elems) {
    monaco_editor_objs.push(
      monaco.editor.create(monaco_editor_elem, {
        value: [''].join('\n'),
        language: 'javascript',
        wordWrap: "on",
        automaticLayout: true
      })
    );
  }
}

function makeInputAutoComplete(elem_id) {
  let codepath_input_elem = document.getElementById(elem_id);
  let _autocomplete_list_cache = {};
  async function _query_autocomplete_list(query) {
    let q = codepath_input_elem.value;
    let normalized_q = q.indexOf("/") >= 0 ? q.split("/").slice(0,-1).join("/") : "";
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
    let selected_value =  event.detail.selection.value;
    console.log("codepath_input_elem selection Event:", selected_value);
    codepath_input_elem.value = selected_value;
    filepath_autocomplete_obj.start(selected_value);
  });
}


async function loadHandlerAsync() {
  //TODO: read sourcelang, targetlang, testcase
  let comment_prefix_dict = {
    "js": "//",
    "py": "#"
  }
  async function _loadHandleIdxAsync(idx) {
    let codepath_elem = codepath_input_elems[idx];
    let editor_obj = monaco_editor_objs[idx];
    let anyfile_path = codepath_elem.value.trim();
    if (anyfile_path === "") {
      console.log("_loadHandleIdxAsync empty path:", idx);  
      return;
    }
    let path_split_on_dot = anyfile_path.split(".");
    let lang = path_split_on_dot[path_split_on_dot.length - 1];
    let comment_prefix = lang in comment_prefix_dict ? comment_prefix_dict[lang] : "";
    console.log("Load code file " + anyfile_path + "...");
    let codestr = null;
    try {
      codestr = await anyfileAsync(anyfile_path);
    } catch (e) {
      codestr = comment_prefix + "FAILED_TO_LOAD\n" + comment_prefix + e;
    }
    let codeModel = editor_obj.getModel(); 
    if (lang in monaco_language_name_dict) {
      console.log("set editor to language:", monaco_language_name_dict[lang]);
      monaco.editor.setModelLanguage(codeModel, monaco_language_name_dict[lang]);
    } else {
      console.log("set editor as plain text:", idx);
      monaco.editor.setModelLanguage(codeModel, "txt");
    }
    editor_obj.setValue(codestr);
  }

  _loadHandleIdxAsync(0);
  _loadHandleIdxAsync(1);
  _loadHandleIdxAsync(2);
}