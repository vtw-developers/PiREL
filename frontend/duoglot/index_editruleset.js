
document.body.style.zoom = "90%";

let load_btn = document.getElementById("load-btn");
let save_btn = document.getElementById("save-btn");
let copyurl_btn = document.getElementById("copyurl-btn");

let codepath_input0_elem = document.getElementById("codepath-input0");

let ruleset_copy_list_wrapper_elems = [
  document.getElementById("ruleset-copy-list-wrapper0"),
  document.getElementById("ruleset-copy-list-wrapper1"),
  document.getElementById("ruleset-copy-list-wrapper2")
];

let ruleset_visual_list_wrapper_elems = [
  document.getElementById("ruleset-visual-list-wrapper0"),
  document.getElementById("ruleset-visual-list-wrapper1"),
  document.getElementById("ruleset-visual-list-wrapper2")
];

let edit_right_side_elems = [
  document.getElementById("edit-right-side0"),
  document.getElementById("edit-right-side1"),
  document.getElementById("edit-right-side2")
];

let sortified_combo_keys = {};

let short_loaded_libpath = null;
let loaded_libpath = null;
let loaded_subpaths = [];
let loaded_ruleset_keys = {};
let combo_keys_per_subpath = {};
let _ruleset_dict = {};
let _combo_dict = {};
function get_unique_combo_key() { let i = 0; while(true) {if (!("Combo"+ i in _combo_dict)) {return "Combo" + i;} i++;}}
function delete_combo(combo_key) {delete _combo_dict[combo_key];}

//////// api ////////
window.getComboCode = function (combo_key) {
  collectUpdateConfigData();
  rulesetVisualListViewUpdate();
  if (!(combo_key in _combo_dict)) return null;
  let combo_data = _combo_dict[combo_key];
  let ruleset_key_list = combo_data["ruleset_key_list"];
  let code_list = ruleset_key_list.map(
    (ruleset_key) => _ruleset_dict[ruleset_key]["code"]
  );
  return code_list.join("\n\n; ================================\n\n");
}

window.externalListeners = {
  onRulesetDblClickAsync: null,
  onReloadAsync: null,
  onSaveComboConfigAsync: null
}

window.externalFunctions = {};

window.API = {
  reloadPathAsync: _reloadPathAsync,
  loadPathAsync: _loadPathAsync
}

window.setExternalListener = function (eventname, handler) {
  if (!(eventname in window.externalListeners)) throw Error("setExternalListener Unknown event: " + eventname);
  window.externalListeners[eventname] = handler;
}

window.setExternalFunction = function (functionName, func) {
  window.externalFunctions[functionName] = func;
}


/////////////// utils //////////////
window._getExternalFunction = function (functionName) {
  if (!(functionName in window.externalFunctions)) throw Error("_getExternalFunction not found: " + functionName);
  return window.externalFunctions[functionName];
}

async function _reloadPathAsync() {
  await loadHandlerAsync();
}

async function _loadPathAsync(path) {
  codepath_input0_elem.value = path;
  await loadHandlerAsync();
}

//////// internal ui ////////
function jsonml_right_side(idx) {
  return ['div', 
    ['span', loaded_subpaths[idx]],
    ['div.right-side-deleter', 
      ['div.right-side-deleter-bg', jsonml_svg_icon_trash(".full-svg-icon")],
      ['div.right-side-deleter-list']
    ]
  ];
}

async function ruleset_item_dblclick_handler(e) {
  let ruleset_key = e.currentTarget.__incrementalDOMData.key;
  console.log("ruleset_item_dblclick_handler:", ruleset_key);
  if (window.externalListeners.onRulesetDblClickAsync) {
    await window.externalListeners.onRulesetDblClickAsync(ruleset_key);
  }
}
function jsonml_ruleset_item(ruleset_key) {
  return ['div.ruleset-item', {key:ruleset_key, ondblclick:ruleset_item_dblclick_handler}, ruleset_key, " (" + _ruleset_dict[ruleset_key]["stated_rules"].length + " rules)"];
}
function jsonml_copy_list(data) {
  let retml = ['div.ruleset-copy-list', {key: "copy_list"}, 
    ...data.map((x) => jsonml_ruleset_item(x))
  ];
  console.log("jsonml_copy_list:", retml);
  return retml;
}

function jsonml_combo(combo_key, ruleset_key_list) {
  return ['div.combo-ruleset-list', {key:combo_key},
    ...ruleset_key_list.map((x) => {
      return jsonml_ruleset_item(x);
    })
  ];
}


function my_show_dialog_sync_noblock(text) {
  var modal = new tingle.modal({
    footer: true,
    stickyFooter: false,
    closeMethods: ['overlay', 'button', 'escape'],
    closeLabel: "Close",
    cssClass: ['my-modal-dialog'],
  });
  let textarea = document.createElement("textarea");
  textarea.value = text;
  textarea.classList.add("my-modal-textarea");
  modal.setContent(textarea);
  modal.open();
}

function show_combo_code_handler(e) {
  let comboKey = e.currentTarget.parentNode.__incrementalDOMData.key;
  console.log("show_combo_code_handler combo_key:", );
  e.stopPropagation();
  setTimeout(() => {  
    let code = window.getComboCode(comboKey);
    my_show_dialog_sync_noblock(code);
  }, 0);
}

function jsonml_visual_list(combo_keys) {
  let retml = ['div.ruleset-visual-list', {key: "visual_list"}, 
    ...combo_keys.map((ckey) => {
      let x = _combo_dict[ckey];
      return ['div.visual-list-item', {key:x["combo_key"]}, ['span.visual-list-item-label', {ondblclick: show_combo_code_handler}, x["combo_name"]], jsonml_combo(x["combo_key"], x["ruleset_key_list"])];
    }),
  ];
  console.log("jsonml_visual_list:", retml);
  return retml;
}

window._IS_AUTOLOAD = false;
(async function main() {
  readUrlHandler();
  makeInputAutoComplete("codepath-input0");
  load_btn.addEventListener("click", loadHandlerAsync);
  save_btn.addEventListener("click", saveHandlerAsync);
  copyurl_btn.addEventListener("click", copyUrlHandler);
  if (window._IS_AUTOLOAD) await loadHandlerAsync();
})();

function rulesetCopyListViewUpdate() {
  for(let i = 0; i < 3; i++) {
    render_copy_list(i,  loaded_ruleset_keys[loaded_subpaths[i]]);
  }
}

function rulesetVisualListViewUpdate() {
  for(let i = 0; i < 3; i++) {
    render_visual_list(i,  combo_keys_per_subpath[loaded_subpaths[i]]);
    incrementally_make_sublist_sortable_visual_list(i);
  }
}

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



async function loadHandlerAsync() {
  if(false) {
    await _loadHandlerAsyncInner();
  }
  else {
    let is_success = false;
    try {
      await _loadHandlerAsyncInner();
      is_success = true;
    } catch (e) {
      alert("Load failed: " + e);
      throw e;
    }
    if (window.externalListeners.onReload) {
      await window.externalListeners.onReload();
    }
  }
}
async function _loadHandlerAsyncInner() {
  let config_path = codepath_input0_elem.value;
  let config_json = await anyfileAsync(config_path);
  let config_data = JSON.parse(config_json);
  short_loaded_libpath = config_data["libpath"];
  loaded_libpath = get_dirpath_of_filepath(config_path) + config_data["libpath"];
  loaded_subpaths = config_data["subpaths"];
  combo_keys_per_subpath = config_data["combo_keys_per_subpath"];
  let is_empty_combo_dict = config_data["combo_dict"] === undefined || config_data["combo_dict"] === null; 
  _combo_dict = is_empty_combo_dict ? {} : config_data["combo_dict"];
  if(loaded_subpaths.length !== 3) {
    alert("Only support exactly 3 subpaths.");
    throw Error("Expecting_Exact_3_subpaths");
  }

  //initialize & clear
  sortified_combo_keys = {};
  for(let i = 0; i < loaded_subpaths.length; i++) {
    loaded_ruleset_keys[loaded_subpaths[i]] = [];

    render_copy_list(i, loaded_ruleset_keys[loaded_subpaths[i]]);
    make_sortable_copy_list(i);
    render_right_side(i);
    make_sortable_right_side_deleter_list(i);
    render_visual_list(i, []);
  }
  
  async function _loadHandleIdxAsync(idx) {
    console.log("_loadHandleIdxAsync", idx);
    let listingpath = loaded_libpath + loaded_subpaths[idx];
    let dirfiles = await listDirAsync(null, listingpath);
    if ("error_msg" in dirfiles) {
      alert("Failed to load: " + dirfiles["error_msg"]);
      return;
    }
    console.log("_loadHandleIdxAsync:", dirfiles["filepaths"]);

    await Promise.all(dirfiles["filepaths"].map((filepath) => 
      (async () => {
        console.log("Load code file " + filepath + "...");
        let ruleset = {};
        ruleset["filepath"] = filepath;
        ruleset["key"] =  loaded_subpaths[idx] + "/" + filepath.split("/").reverse()[0].replace(".snart", "");
        let codestr = null;
        try {
          codestr = await anyfileAsync(filepath);
          ruleset["code"] = codestr;
          let parse_result =  await statRulesAsync(codestr);
          ruleset["stated_rules"] = parse_result[0];
          ruleset["error_msg"] = parse_result[1];
        } catch (e) {
          alert("FAILED_TO_LOAD\n" + e);
          throw Error("Failed to load file: " + filepath);
        }
        _ruleset_dict[ruleset["key"]] = ruleset;
        loaded_ruleset_keys[[loaded_subpaths[idx]]].push(ruleset["key"]);
        if (is_empty_combo_dict) {
          let new_combo_key = get_unique_combo_key();
          let rulecombo = {
            "combo_key": new_combo_key,
            "combo_name": new_combo_key,
            "ruleset_key_list": [ruleset["key"]]
          };
          _combo_dict[new_combo_key] = rulecombo;
          combo_keys_per_subpath[loaded_subpaths[idx]].push(new_combo_key);
        }
      })()
    ));
  }
  let promises = [];
  for (let i = 0; i < loaded_subpaths.length; i++) {
    promises.push((async () => {
      await _loadHandleIdxAsync(i);
      rulesetCopyListViewUpdate();
    })());
  }
  await Promise.all(promises);
  rulesetVisualListViewUpdate();
}

function collectUpdateConfigData() {
  combo_keys_per_subpath = {};
  _combo_dict = {};
  for (let i = 0; i < ruleset_visual_list_wrapper_elems.length; i++) {
    let subpath = loaded_subpaths[i];
    combo_keys_per_subpath[subpath] = [];
    let ruleset_visual_list_wrapper_elem = ruleset_visual_list_wrapper_elems[i];
    for (let combo_group of Array.from(ruleset_visual_list_wrapper_elem.firstChild.children)) {
      let comboKey = combo_group.children[1].__incrementalDOMData.key;
      combo_keys_per_subpath[subpath].push(comboKey);
      _combo_dict[comboKey] = {
        "combo_key": comboKey,
        "combo_name": combo_group.children[0].innerText,
        "ruleset_key_list": [],
      };
      for (let ruleset_key_item of Array.from(combo_group.children[1].children)) {
        _combo_dict[comboKey]["ruleset_key_list"].push(ruleset_key_item.__incrementalDOMData.key);
      }
    }
  }
}

async function saveHandlerAsync() {
  collectUpdateConfigData();
  let data = {
    "libpath": short_loaded_libpath,
    "subpaths": loaded_subpaths,
    "combo_keys_per_subpath": combo_keys_per_subpath,
    "combo_dict": _combo_dict
  }
  console.log("saveHandlerAsync:", data);
  rulesetVisualListViewUpdate();
  let json_str = JSON.stringify(data, null, 2);
  console.log(json_str);

  let write_path = codepath_input0_elem.value;
  Toastify({
    text: "Saving current rules to " + write_path + " ...",
    gravity: "bottom",
    position: "center",
    className: "toast-info",
    duration: 3000
  }).showToast();
  let result = await saveAnyTextfileAsync(write_path, json_str);
  Toastify({
    text: "Saving response: " + result,
    gravity: "bottom",
    position: "center",
    className: "toast-info",
    duration: 3000
  }).showToast();
  if (window.externalListeners.onSaveComboConfigAsync) {
    await window.externalListeners.onSaveComboConfigAsync();
  }
}

function render_right_side(idx) {
  let right_side_elem = edit_right_side_elems[idx];
  IncrementalDOM.patch(right_side_elem, jsonml2idom, jsonml_right_side(idx));
}

function render_copy_list(idx, datalist) {
  let copy_list_wrapper = ruleset_copy_list_wrapper_elems[idx];
  IncrementalDOM.patch(copy_list_wrapper, jsonml2idom, jsonml_copy_list(datalist));
}

function render_visual_list(idx, datalist) {
  let visual_list_wrapper = ruleset_visual_list_wrapper_elems[idx];
  IncrementalDOM.patch(visual_list_wrapper, jsonml2idom, jsonml_visual_list(datalist));
}

function make_sortable_copy_list(idx) {
  Sortable.create(ruleset_copy_list_wrapper_elems[idx].firstChild, {
    // handle: '.handle-move',
    group: {
      name: 'shared' + idx,
      put: false,
      pull:'clone'
    },
    sort: false,
    animation: 150,
    onRemove: function (e) {
      console.log("onRemove, re-render copy-list.");
      setTimeout(() => rulesetCopyListViewUpdate(), 0);
    }
  });
}

function make_sortable_right_side_deleter_list(idx) {
  Sortable.create(edit_right_side_elems[idx].firstChild.children[1].children[1], {
    // handle: '.handle-move',
    group: {
      name: 'shared' + idx,
    },
    sort: false,
    animation: 150,
    onAdd: function (e) {
      console.log("onAdd, remove from delete-list.", e.to);
      e.to.innerHTML = "";
    }
  });
}

function incrementally_make_sublist_sortable_visual_list(idx) {
  for (let combo_group of Array.from(ruleset_visual_list_wrapper_elems[idx].firstChild.children)) {
    let key = combo_group.children[1].__incrementalDOMData.key;
    if (key !== undefined && (! (key in sortified_combo_keys))) {
      console.log("incrementally_make_sublist_sortable_visual_list create combo sortable:", key);
      Sortable.create(combo_group.children[1], {
        // handle: '.handle-move',
        group: {
          name: 'shared' + idx,
        },
        animation: 150
      });
      sortified_combo_keys[key] = true;
    } 
    
  }
}


///////////////////////////////////////// other utils /////////////////////////////////////////
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