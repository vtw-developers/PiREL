"use strict";

document.body.style.zoom = "90%";
window.DEBUG_LOGGING = false;
require.config({ paths: { vs: '../../_common/monaco/node_modules/monaco-editor/min/vs' } });

let monaco_language_name_dict = {
  "js": "javascript",
  "py": "python",
  // "java": "java",
  // "cs": "csharp",
  // "cpp": "cpp",
}

let sourcelang_select_elem = document.getElementById("sourcelang-select");
let targetlang_select_elem = document.getElementById("targetlang-select");

let loadtype_select_elem = document.getElementById("loadtype-select");
let testcase_select_elem = document.getElementById("testcase-select");
let transprog_select_elem = document.getElementById("transprog-select");
let srcfilepath_input_elem = document.getElementById("srcfilepath-input");
let load_btn = document.getElementById("load-btn");
let translate_btn = document.getElementById("translate-btn");
let translate_choices_btn = document.getElementById("translate-choices-btn");
let continue_choices_btn = document.getElementById("continue-choices-btn");
let choices_input_elem = document.getElementById("choices-input");
let translate_autobackward_elem = document.getElementById("translate-autobackward");
let translate_pirel_checkbox = document.getElementById("translate-pirel");
let copyurl_btn = document.getElementById("copyurl-btn");
let headline_note_elem = document.getElementById("headline-note");

let ast_container_elem = document.getElementById("ast-visualization-container");
let ast_source_info_elem = document.getElementById("astvis-source-info-bar");
let ast_common_info_elem = document.getElementById("astvis-common-info-bar");
let ast_target_info_elem = document.getElementById("astvis-target-info-bar");
let delayed_graph_visualize_btn = document.getElementById("delayed-graph-visualize-btn");
let source_lang_editor_elem = document.getElementById('source-lang-editor');
let target_lang_editor_elem = document.getElementById('target-lang-editor');
let target_trans_editor_elem = document.getElementById('target-trans-editor');
let panel_transform_source_elem = document.getElementById('panel-transform-source-viewer');
let panel_transform_target_elem = document.getElementById('panel-transform-target-viewer');
let panel_mapping_elem = document.getElementById('panel-mapping-viewer');
let panel_dbg_history_table_elem = document.getElementById("panel-dbg-history-table");


window.panel_dbg_history_table_obj = null;
window.source_lang_editor_obj = null;
window.target_lang_editor_obj = null;
window.target_trans_editor_obj = null;


window.getTranslatedCode = function () {
  let original_model = window.target_lang_editor_obj.getModel().original;
  if (!original_model) throw Error("getTranslatedCode failed. original_model not found.");
  return original_model.getValue();
}

window._translate_dbg_history = null;
window.getTranslateDbgHistory = function () {
  return window._translate_dbg_history;
}

window._translate_src_parse = null;
window.getTranslateSrcParse = function () {
  return window._translate_src_parse;
}

window._translated_code_map = null;
window.getTranslatedCodeMap = function () {
  return window._translated_code_map;
}

window._translate_timespan = null;
window.getTranslateTimespan = function () {
  return window._translate_timespan;
}

window._translate_timespan_pretty = null;
window.getTranslateTimespanPretty = function () {
  return window._translate_timespan_pretty;
}

window.waitForContinueClickAsync = async function () {
  const myPromise = new Promise((resolve, reject) => {
    continue_choices_btn.onclick = () => resolve("CONTINUE");
  });
  await myPromise;
}

window.setForHumanAdjustment = function () {
  function _setContinueButton(text, is_disabled) {
    continue_choices_btn.innerText = text;
    continue_choices_btn.disabled = is_disabled;
  }
  _setContinueButton("Continue(ch)", false);
  alert("[UI_INFO] Please adjust choices and click continue.");
}

window.getChoices = function () {
  return JSON.parse(choices_input_elem.value);
}

window.setChoices = function (choice_type, choices_list) {
  if ((choice_type !== "STEP" && choice_type !== "ASTNODE")) {
    throw Error("choice_type is unexpected: " + choice_type);
  }
  if (!Array.isArray(choices_list)) {
    throw Error("choices_list not valid array.");
  }
  choices_input_elem.value = JSON.stringify({
    "type": choice_type,
    "choices_list": choices_list
  });
}

window.getAutoBack = function () {
  return translate_autobackward_elem.checked;
}

window.setAutoBack = function (autoback) {
  translate_autobackward_elem.checked = String(autoback) === "true";
}

window.setHeadlineNote = function (note) {
  headline_note_elem.innerText = note;
}


// UI states for ast visualizer
let astvis_edit_state = {
  "node": {
    "hover": { "source": [] },
  },
  "combo": {
    "nomatch": { "source": [] },
    "selected": { "source": [] },
    "hover": { "source": [] },
    "expanmatch": {"source": []},
    "expanslotmatch1": {"source": []},
    "expanslotmatch2": {"source": []},
  },
  set_single_node_auto: (nodeId, stateName) => {
    if (nodeId !== null && nodeId !== undefined) {
      if(nodeId.startsWith("source")) astvis_edit_state.node[stateName].source = [nodeId];
      else if(nodeId.startsWith("target")) astvis_edit_state.node[stateName].target = [nodeId];
      else throw "set_node_hover_auto_node_id_unexpected_prefix_" + nodeId;
    }
  },
  set_single_combo_auto: (comboId, stateName) => {
    if (comboId !== null && comboId !== undefined) {
      if(comboId.startsWith("c_source")) astvis_edit_state.combo[stateName].source = [comboId];
      else if(comboId.startsWith("c_target")) astvis_edit_state.combo[stateName].target = [comboId];
      else throw "set_combo_hover_auto_combo_id_unexpected_prefix_" + comboId;
    }
  },
  add_multiple_combo_source: (comboIds, stateName) => {
    astvis_edit_state.combo[stateName].source.push(...comboIds);
  },
  clear_multiple_combo_source: (stateName) => {
    astvis_edit_state.combo[stateName].source = [];
  },
  reset: () => {
    astvis_edit_state["node"] = {
      "hover": { "source": [] },
    };
    astvis_edit_state["combo"] = {
      "nomatch": { "source": [] },
      "selected": { "source": [] },
      "hover": { "source": [] },
      "expanmatch": {"source": []},
      "expanslotmatch1": {"source": []},
      "expanslotmatch2": {"source": []},
    };
  },
};

let astvis_ratio = 3;
let astvis_width = null;
let astvis_height = null;


// UI states for monaco editor
let source_decoration_dict = {
  "_example_node_id": {isOn: false, deco: {range: null, options: { inlineClassName: null}}},
};
let target_decoration_dict = {
  "_example_node_id": {isOn: false, deco: {range: null, options: { inlineClassName: null}}},
};
function resetDecorationDicts() {
  source_decoration_dict = {};
  target_decoration_dict = {};
}


pastedUrlHandler();
setTimeout(pastedUrlHandler, 1500);
setTimeout(pastedUrlHandler, 3000);
load_btn.addEventListener("click", loadHandlerAsync);

window.translateHandlerDefaultAsync = translateHandlerGen(false);
window.translateHandlerChAsync = translateHandlerGen(true);
translate_btn.addEventListener("click", window.translateHandlerDefaultAsync);
translate_choices_btn.addEventListener("click", window.translateHandlerChAsync);
copyurl_btn.addEventListener("click", copyUrlHandler);


(async function main1() {
  getFileDictHandlerAsync();

  // about updating options:
  // https://stackoverflow.com/questions/64466716/conditonally-wrap-line-in-monaco-editor

  // the demo code is not a real file
  require(['vs/editor/editor.main'], function () {
    source_lang_editor_obj = monaco.editor.create(source_lang_editor_elem, {
      // value: ['def x():', '\tprint("Hello world!")', ''].join('\n'),
      language: 'python',
      wordWrap: "off",
      automaticLayout: true
    });
    target_lang_editor_obj = monaco.editor.createDiffEditor(target_lang_editor_elem, {
      // value: ['function x() {', '\tconsole.log("Hello world!");', '}'].join('\n'),
      wordWrap: "off",
      enableSplitViewResizing: true,
      automaticLayout: true
    });
    target_trans_editor_obj = monaco.editor.create(target_trans_editor_elem, {
      value: ['; target translation program'].join('\n'),
      language: 'scheme',
      wordWrap: "on",
      automaticLayout: true
    });
  });
})();


// https://g6.antv.vision/en/docs/manual/middle/layout/custom-layout/
(async function main2() {
  G6.registerLayout('PairAST', {
    getDefaultCfg() {
      // The default configurations will be mixed by configurations from user
      return {};
    },
    init(data) {
      const self = this;
      self.nodes = data.nodes;
      self.edges = data.edges;
    },
    execute() {
      console.log("PairAST execute() called.");
      let minX = null;
      let maxX = null;
      let minY = null;
      let maxY = null;
      for (let node of this.nodes) {
        node.x = node.orix;
        node.y = node.oriy;
        if (minX === null || node.x < minX) minX = node.x;
        if (maxX === null || node.x > maxX) maxX = node.x;
        if (minY === null || node.y < minY) minY = node.y;
        if (maxY === null || node.y > maxY) maxY = node.y;
      }
      if (minX !== null && maxX !== null && minY !== null && maxY !== null && maxX !== minX) {
        astvis_ratio = (maxY - minY) / (maxX - minX);
        console.log("update astvis_ratio:", astvis_ratio);
      }
    },
    layout(data) {
      const self = this;
      self.init(data);
      self.execute();
    },
    updateCfg(cfg) {
      const self = this;
      // update cfg
    },
    destroy() {
      const self = this;
      self.positions = null;
      self.nodes = null;
      self.edges = null;
      self.destroyed = true;
    },
  });
})();


// ==========================================================
// ==========================================================
// ============== Functions =================================
window._MI = false;
function setMI(mi) {
  if (mi === "true") {
    window._MI = true;
    translate_btn.style.display = "none";
    translate_choices_btn.style.display = "none";
    continue_choices_btn.style.display = "";
    copyurl_btn.style.display = "none";
    let link = document.getElementsByClassName("the-other-link")[0];
    link.href = "javascript:;";
    link.innerText = "---";
    sourcelang_select_elem.disabled = true;
    targetlang_select_elem.disabled = true;
  }
}

function copyUrlHandler() {
  let srclang = sourcelang_select_elem.value;
  let tarlang = targetlang_select_elem.value;
  let transprog = transprog_select_elem.value;
  let loadtype = loadtype_select_elem.value;
  let srcfilepath = srcfilepath_input_elem.value;
  let testcase = testcase_select_elem.value;
  let choices = choices_input_elem.value;
  let autoback = translate_autobackward_elem.checked;
  let mi = window._MI;
  let urlparams = {
    "srclang": srclang,
    "tarlang": tarlang,
    "transprog": transprog,
    "loadtype": loadtype,
    "srcfilepath": srcfilepath,
    "testcase": testcase,
    "choices": choices,
    "autoback": autoback,
    "mi": mi,
  };
  if (document.getElementById("load-control-group").style.display == "none") {
    urlparams["hideload"] = "none";
  }
  let url = new URL(document.URL);
  url.search = new URLSearchParams(urlparams);
  window.history.pushState(null, "Trans (URL Copied)", url);
  navigator.clipboard.writeText(url.toString());
  console.log("copyUrlHandler:", url.toString());
}

function pastedUrlHandler() {
  const urlParams = new URLSearchParams(window.location.search);
  console.log("pastedUrlHandler:", window.location.search);
  let setted_vals = [];
  if (urlParams.has("hideload")) {setted_vals.push("hideload"); document.getElementById("load-control-group").style.display = urlParams.get("hideload");}
  if (urlParams.has("srclang")) {setted_vals.push("srclang"); sourcelang_select_elem.value = urlParams.get("srclang");}
  if (urlParams.has("tarlang")) {setted_vals.push("tarlang"); targetlang_select_elem.value = urlParams.get("tarlang");}
  if (urlParams.has("transprog")) {setted_vals.push("transprog"); transprog_select_elem.value = urlParams.get("transprog");}
  if (urlParams.has("loadtype")) {setted_vals.push("loadtype"); loadtype_select_elem.value = urlParams.get("loadtype");}
  if (urlParams.has("srcfilepath")) {setted_vals.push("srcfilepath"); srcfilepath_input_elem.value = urlParams.get("srcfilepath");}
  if (urlParams.has("testcase")) {setted_vals.push("testcase"); testcase_select_elem.value = urlParams.get("testcase");}
  if (urlParams.has("choices")) {setted_vals.push("choices"); choices_input_elem.value = urlParams.get("choices");}
  if (urlParams.has("autoback")) {window.setAutoBack(urlParams.get("autoback"));}
  if (urlParams.has("mi")) {setted_vals.push("mi"); setMI(urlParams.get("mi")); }
  console.log("pastedUrlHandler setting:", setted_vals);
}

async function getFileDictHandlerAsync() {
  let file_dict = await getTestfilesAsync();
  let prog_dict = await getProgfilesAsync();
  console.log("# getFileDictHandlerAsync file_dict:", file_dict, " prog_dict:", prog_dict);
  function _updateLoadTypeSelect() {
    let loadType = loadtype_select_elem.value;
    console.log("_updateLoadTypeSelect LoadType:", loadType);
    if (loadType === "testcase") {
      srcfilepath_input_elem.style.display = "none";
      testcase_select_elem.style.display = "inline";
    } else if (loadType === "singlefile") {
      srcfilepath_input_elem.style.display = "inline";
      testcase_select_elem.style.display = "none";
    } else {
      alert("[UI_UNEXPECTED_ERROR] Unknwon loadType: " + loadType);
    }
  }
  function _updateTestcasesSelect() {
    let sourceLang = sourcelang_select_elem.value;
    let targetLang = targetlang_select_elem.value;
    console.log("_updateTestcasesSelect: ", sourceLang, targetLang);

    // ~~~ default ruleset
    // let defaultValueForSelect = "base_upd";
    // let defaultValueForSelect = "base_fn_header_only_ext";
    let defaultValueForSelect = "current_learned_rules";

    let pairkey = sourceLang + "_" + targetLang;
    if (pairkey in prog_dict["dirs"]) {
      let progs = prog_dict["dirs"][pairkey]["files"];
      progs.sort();
      transprog_select_elem.innerHTML = "";
      let option_fragment = document.createDocumentFragment();
      console.log("_updateTestcasesSelect creating DOM elements for progs...");
      for(let prog of progs) {
        let prog_prefix = prog.replace(".snart", "");
        let option_elem = document.createElement("option");
        option_elem.attributes["value"] = prog_prefix;

        if (prog_prefix === defaultValueForSelect) {
          option_elem.setAttribute("selected", "selected");
        }

        option_elem.innerText = prog_prefix;
        option_fragment.appendChild(option_elem);
      }
      transprog_select_elem.appendChild(option_fragment);
    } else {
      transprog_select_elem.innerHTML = "";
    }

    let common_filenames = [];
    if(sourceLang !== targetLang) {
      let source_files = file_dict["dirs"][sourceLang]["files"];
      let target_files = file_dict["dirs"][targetLang]["files"];
      console.log("_updateTestcasesSelect finding matches...");
      let prefix_dict = {};
      for(let srcfile of source_files) {
        let src_prefix = srcfile.split(".").slice(0,-1).join("");
        if (!(src_prefix in prefix_dict)) prefix_dict[src_prefix] = true;
      }
      for (let tarfile of target_files) {
        let tar_prefix = tarfile.split(".").slice(0,-1).join("");
        if (tar_prefix in prefix_dict) {
          common_filenames.push(tar_prefix);
        }
      }
      common_filenames.sort();
      console.log("_updateTestcasesSelect common: ", common_filenames);
      testcase_select_elem.innerHTML = "";
      //use fragment to speed up
      let option_fragment = document.createDocumentFragment();
      console.log("_updateTestcasesSelect creating DOM elements...");
      for(let fileprefix of common_filenames) {
        let option_elem = document.createElement("option");
        option_elem.attributes["value"] = fileprefix;
        option_elem.innerText = fileprefix;
        option_fragment.appendChild(option_elem);
      }
      testcase_select_elem.appendChild(option_fragment);
    } else {
      testcase_select_elem.innerHTML = "";
    }
    console.log("_updateTestcasesSelect done.");
  }
  _updateLoadTypeSelect();
  _updateTestcasesSelect();
  sourcelang_select_elem.onchange = _updateTestcasesSelect;
  targetlang_select_elem.onchange = _updateTestcasesSelect;
  loadtype_select_elem.onchange = _updateLoadTypeSelect;
  //add auto completers
  let _autocomplete_list_cache = {};
  async function _query_autocomplete_list() {
    let srclang = sourcelang_select_elem.value;
    if (!(srclang in _autocomplete_list_cache)) _autocomplete_list_cache[srclang] = {};
    let q = srcfilepath_input_elem.value;
    let normalized_q = q.indexOf("/") >= 0 ? q.split("/").slice(0,-1).join("/") : "";
    if (normalized_q in _autocomplete_list_cache[srclang]) return _autocomplete_list_cache[srclang][normalized_q];
    let resp_dict = await listDirAsync(srclang, normalized_q);
    let ac_list = [];
    if ("filepaths" in resp_dict) ac_list = ac_list.concat(resp_dict["filepaths"]);
    if ("dirpaths" in resp_dict) ac_list = ac_list.concat(resp_dict["dirpaths"]);
    if ("error_msg" in resp_dict) ac_list = ["NOT_VALID_FILE_PATH"];
    console.log("# _query_autocomplete_list new query:", normalized_q, resp_dict, ac_list)
    _autocomplete_list_cache[srclang][normalized_q] = ac_list;
    return _autocomplete_list_cache[srclang][normalized_q];
  }
  let srcfilepath_autocomplete_obj = new autoComplete({
    selector: "#srcfilepath-input",
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
    "create srcfilepath_autocomplete_obj:",
    srcfilepath_autocomplete_obj);
  srcfilepath_input_elem.addEventListener("selection", function (event) {
    // "event.detail" carries the autoComplete.js "feedback" object
    let selected_value =  event.detail.selection.value;
    console.log("srcfilepath_input_elem selection Event:", selected_value);
    srcfilepath_input_elem.value = selected_value;
    srcfilepath_autocomplete_obj.start(selected_value);
  });
}

async function loadHandlerAsync() {
  // TODO: read sourcelang, targetlang, testcase
  let srcLang = sourcelang_select_elem.value;
  let tarLang = targetlang_select_elem.value;
  let transprogprefix = transprog_select_elem.value;
  let option2SourcePath = (x) => "/duoglot/tests/basic/" + srcLang + "/" + x + "." + srcLang;
  let option2TargetPath = (x) => "/duoglot/tests/basic/" + tarLang + "/" + x + "." + tarLang;
  let tranlatorPath = (translator_name) => "/duoglot/tests/trans_programs/" + srcLang + "_" + tarLang + "/" + translator_name + ".snart";
  let defaultTranslatorPath = tranlatorPath(transprogprefix);

  let loadTypeValue = loadtype_select_elem.value;
  let selectedValue = testcase_select_elem.value;
  let srcfilepathValue = srcfilepath_input_elem.value;
  let is_testfile_load_success = false;
  let new_source_code_str = null;
  let new_target_code_str = null;
  if (loadTypeValue === "testcase") {
    if (selectedValue === null || selectedValue === undefined || selectedValue === "") {
      alert("[UI_HANDLED] No testcase is selected.");
    } else {
      let sourcePath = option2SourcePath(selectedValue);
      let targetPath = option2TargetPath(selectedValue);
      console.log("Load testcase " + selectedValue + "...");
      new_source_code_str = await errorWrapperPromiseAsync(anyfileAsync(sourcePath), error404Nullify);
      new_target_code_str = await errorWrapperPromiseAsync(anyfileAsync(targetPath), error404Nullify);
      is_testfile_load_success = new_source_code_str !== "" && new_target_code_str !== "";
    }
  } else if (loadTypeValue === "singlefile") {
    new_source_code_str = await errorWrapperPromiseAsync(anyfileAsync(srcfilepathValue), error404Nullify);
    new_target_code_str = null;
    is_testfile_load_success = new_source_code_str !== null;
  } else {
    alert("[UI_UNEXPECTED_ERROR] Unknown loadType: " + loadTypeValue);
    return;
  }

  if (true) {
    new_source_code_str = new_source_code_str === null ? "" : new_source_code_str;
    new_target_code_str = new_target_code_str  === null ? "" : new_target_code_str;
    let srcModel = source_lang_editor_obj.getModel();
    monaco.editor.setModelLanguage(srcModel, monaco_language_name_dict[srcLang]);
    source_lang_editor_obj.setValue(new_source_code_str);

    var tarCurrentlModel = monaco.editor.createModel('', monaco_language_name_dict[tarLang]);
    var tarTargetModel = monaco.editor.createModel(new_target_code_str, monaco_language_name_dict[tarLang]);
    target_lang_editor_obj.setModel({
      original: tarCurrentlModel,
      modified: tarTargetModel
    });
  }

  console.log("Load translator program (if any)...");
  try {
    let progCodeStr = await anyfileAsync(defaultTranslatorPath);
    target_trans_editor_obj.setValue(progCodeStr);
  } catch (error) {
    console.warn("Translator program not loaded. Default might not exist.", error);
    target_trans_editor_obj.setValue("; empty ...");
  }
}


// ~~~ Trans button handler on http://127.0.0.1:8000/frontend/duoglot/pirel/ui_translate_single.html
function translateHandlerGen(is_reading_choices) {

  function _setContinueButton(text, is_disabled) {
    continue_choices_btn.innerText = text;
    continue_choices_btn.disabled = is_disabled;
  }

  /**
   * ~~~~~ loop for learning rules
   * transRules: all rules in a single string
  */
  async function pirelLoop(srcCode, srcLang, tarLang, transRules, transType, transChoices, autobackEnabled) {
    let programTranslationState = {};
    let attemptCount = 0;

    pirelLoop:
    while (attemptCount < consts_ns.MAX_NUM_LOOPS_PIREL) {
      let translationResult = await translateAsync(srcCode, srcLang, tarLang, transRules, transType, transChoices, autobackEnabled);
      let [_1, _2, errorInfo, _4, _5, _6, _7] = translationResult;

      if (!errorInfo) {
        return translationResult;
      }

      if ("templates_dict" in errorInfo) {
        let templatesDict = JSON.parse(errorInfo["templates_dict"]);
        let translationRules = await getTranslationRules(templatesDict, programTranslationState, srcLang, tarLang);
        // remove duplicate translation rules
        translationRules = [...new Set(translationRules)];
        for (let translationRule of translationRules) {
          transRules = `;;;; NEW FROM PIREL:\n${translationRule}\n\n\n` + transRules;
        }
        await utils_ns.writeWithTimestamp(transRules, 'updated-ruleset.snart', consts_ns.DEBUG_OUTPUT_TRANSLATE_SINGLE_DIR);

      } else {
        console.log("SEVERE: error on backend", errorInfo);
        alert("error on backend: check console logs");
      }

      attemptCount += 1;
    }

    // should not reach this
    alert('should not reach this, debugging needed');
  }

  /**
   * part of pirel
   * templatesDict - as is from the backend
  */
  async function getTranslationRules(templatesDict, programTranslationState, srcLang, tarLang) {
    let problematicNodeType = templatesDict["problematic_node_type"];
    await utils_ns.writeJsonWithTimestamp(templatesDict, `gen-templates-${problematicNodeType}`, consts_ns.DEBUG_OUTPUT_TRANSLATE_SINGLE_DIR);

    // initiate the state for the current problematic node
    let nodeTranslationState = null;
    let isPreviouslySeenNode = false;
    let problematicNodeId = templatesDict["problematic_node_id"];
    if (problematicNodeId in programTranslationState) {
      nodeTranslationState = programTranslationState[problematicNodeId];
      isPreviouslySeenNode = true;
    } else {
      nodeTranslationState = programTranslationState[problematicNodeId] = {};
    }

    // generate program pairs
    // this is a hack to make query_llm.js work for ui_translate_single.js
    learnRules_ns.log = function() { console.log(...arguments); };
    let programMetadata = {file_name: "", source_code: "", id: "", log_dir: consts_ns.DEBUG_OUTPUT_TRANSLATE_SINGLE_DIR, path: (x => x)};

    // iterate over templates
    for (let templateId = 0; templateId < templatesDict["num_templates"]; templateId++) {
      let templateDict = templatesDict[templateId];

      // skip an invalid template
      if (!templateDict["is_valid_template"]) {
        continue;
      }

      let translationPairsDict = await queryAPI_ns.genTransPair(srcLang, tarLang, templateDict, programMetadata);
      // let translationPairsDict = {
      //   "translation_pairs": [
      //     [
      //       {
      //         "source": "for i, v in enumerate(lst):\n    secret_fun_4071()",
      //         "target": "for(let i = 0; i < lst.length; i++) {\n    let v = lst[i];\n    secret_fun_4071();\n}"
      //       },
      //       {
      //         "source": "for _ in enumerate(my_tuple):\n    secret_fun_4071()",
      //         "target": "for(let i = 0; i < my_tuple.length; i++) {\n    let v = my_tuple[i];\n    secret_fun_4071();\n}"
      //       }
      //     ],
      //     [
      //       {
      //         "source": "for i, v in enumerate(lst):\n    secret_fun_4071()",
      //         "target": "lst.forEach((v, i) => {\n    secret_fun_4071();\n});"
      //       },
      //       {
      //         "source": "for _ in enumerate(my_tuple):\n    secret_fun_4071()",
      //         "target": "my_tuple.forEach((v, i) => {\n    secret_fun_4071();\n});"
      //       }
      //     ]
      //   ],
      //   "templatized_nodes_replace_dws_values": [
      //     true,
      //     false,
      //     false
      //   ]
      // }

      // skip if no translation pairs were generated
      if (translationPairsDict["translation_pairs"].length === 0) {
        continue;
      }

      await utils_ns.writeJsonWithTimestamp(translationPairsDict, `translation-pairs-for-template-id-${templateId}`, programMetadata.log_dir);

      let translationRules = await inferTranslationRules(
        srcLang,
        tarLang,
        translationPairsDict,
        templateDict,
      );

      await utils_ns.writeJsonWithTimestamp(translationRules, `translation-rules-for-template-id-${templateId}`, programMetadata.log_dir);

      return translationRules;
    }
  }

  /**
   * RETURN
   * List of translation rules
  */
  async function inferTranslationRules(srcLang, tarLang, translationPairsDict, templateDict) {
    let translationRules = [];
    let chooseLargestContainingNode = true;
    let prettyPrintTreeLike = false;

    let translationPairs = translationPairsDict["translation_pairs"];
    let templatizedNodesReplaceDWS = translationPairsDict["templatized_nodes_replace_dws_values"];

    for (let translationPair of translationPairs) {
      // TODO optimize earlier: already know which contexts are contained in translationPair
      for (let context of templateDict["contexts"]) {
        try {
          let newTranslationRule = await ruleInfAPI_ns.inferTranslationRule(
            srcLang,
            tarLang,
            translationPair,
            context,
            templateDict["templatized_node_ids"],
            templatizedNodesReplaceDWS,
            templateDict["is_insert_secret_fn"],
            prettyPrintTreeLike
          );
          translationRules.push(newTranslationRule);
        } catch (e) {
          if (e instanceof ruleInfAPI_ns.ContextNotFoundError) {
            continue;
          }
          alert(`error during rule inference: ${e}\n${e.stack}`);
          continue;
        }
      }
    }
    return translationRules;
  }

  async function _translateHandlerAsync() {
    console.log("++++++++++++++ translate_btn event handler ++++++++++++++");
    //------- set parse globals
    _setContinueButton("Waiting...", true);
    function _get_src_AST_dict(source_AST, source_ann) {
      let source_AST_dict = {};
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
      astToDictRec(source_AST, source_AST_dict);
      if (false) console.log("_get_src_AST_dict.  source_code:", source_AST, "source_ann:", source_ann);
      return source_AST_dict;
    }
    let sourceLang = sourcelang_select_elem.value;
    let targetLang = targetlang_select_elem.value;
    let source_code = source_lang_editor_obj.getValue();
    let transprog = target_trans_editor_obj.getValue();
    let choices_info = {"type": "STEP", "choices_list": []};
    if (is_reading_choices) {
      choices_info = JSON.parse(choices_input_elem.value);
    }
    let {type, choices_list} = choices_info;

    // ~~~ invoke translation
    let pirelEnabled = translate_pirel_checkbox.checked;
    let translationResult = null;
    if (pirelEnabled) {
      translationResult = await pirelLoop(source_code, sourceLang, targetLang, transprog, type, choices_list, translate_autobackward_elem.checked);
    } else {
      translationResult = await translateAsync(source_code, sourceLang, targetLang, transprog, type, choices_list, translate_autobackward_elem.checked);
    }
    let [src_parse_result, translate_result, error_info, dbg_history, translator_dbg_info, timespan, timespan_p] = translationResult;

    window._translate_dbg_history = dbg_history;
    window._translate_timespan = timespan;
    window._translate_timespan_pretty = timespan_p;
    window._translate_src_parse = null;
    if (window.DEBUG_LOGGING) {
      console.log("++++++++++++++ translate-btn src_parse:", src_parse_result);
      console.log("++++++++++++++ translate-btn translate_result:", translate_result);
      console.log("++++++++++++++ translate-btn error_info:", error_info);
      console.log("++++++++++++++ translate-btn translate dbg_history:", dbg_history);
      console.log("++++++++++++++ translate-btn translator_dbg_info:", translator_dbg_info);
      console.log("++++++++++++++ translate-btn timespan:", timespan);
    }
    //------- update translated code
    function _updateTranslatedCodeMonaco(partial_code) {
      if (partial_code == null) {
        //console.warn("# _updateTranslatedCodeMonaco code is null.");
        partial_code = "ERROR_OR_EMPTY";
      }

      try {
        var oldModel = target_lang_editor_obj.getModel().original;
        if (oldModel) oldModel.dispose();
      } catch (e) {console.warn("Cannot clean the old model.");}

      var tarCurrentlModel = monaco.editor.createModel(partial_code, monaco_language_name_dict[targetLang]);
      var tarTargetModel = target_lang_editor_obj.getModel().modified;
      if (tarTargetModel === null) tarTargetModel = monaco.editor.createModel("", monaco_language_name_dict[targetLang]);
      target_lang_editor_obj.setModel({
        original: tarCurrentlModel,
        modified: tarTargetModel
      });
    }

    if (translate_result) {
      window._translated_code_map = translate_result["map_to_exid"];
      _updateTranslatedCodeMonaco(translate_result["code"]);
      _setContinueButton("Done", true);
    } else {
      window._translated_code_map = null;
      _updateTranslatedCodeMonaco(null);
      _setContinueButton("Continue(ch)", false);
      if (error_info["type"] === "API_PARAM_ERROR") {
        alert("[UI_HANDLED]API Param Error. Translation Abort. " + error_info["msg"]);
        return;
      } else {
        alert("[UI_HANDLED]" + error_info["msg"]);
      }
    }
    console.log("+++++++++++++ translate-btn done.");


    let source_AST = src_parse_result["src_ast"];
    let source_ann = src_parse_result["src_ann"];
    let source_AST_dict = _get_src_AST_dict(source_AST, source_ann);
    window._translate_src_parse = [source_code, src_parse_result, source_AST_dict];
    visualizeAST(true,
      sourceLang, targetLang,
      source_AST_dict, null,
      source_AST, null,
      source_ann, null,
      dbg_history, translator_dbg_info,
      translate_result, _updateTranslatedCodeMonaco);
  }
  return _translateHandlerAsync;
}


// ==========================================================
// ==========================================================
// ============== Other UI changing funcs ===================
function updateChoices(step, astrange, idx) {
  console.log("# updateChoices step: ", step, " astrange:", astrange, " idx: ", idx);
  let current_choices = JSON.parse(choices_input_elem.value);
  let {type, choices_list} = current_choices;

  let new_choices = null;
  let new_choices_list = [];
  let is_set = false;
  if (type === "STEP") {
    if (!(typeof step === "number")) throw Error("Current choices are of type STEP. step number must be provided.");
    for (let choice of choices_list) {
      if (choice[0] === step) {
        is_set = true;
        if(idx !== 0) new_choices_list.push([step, idx]);
      } else {
        new_choices_list.push(choice);
      }
    }
    if (!is_set) new_choices_list.push([step, idx]);

  } else if (type === "ASTNODE") {
    if (!Array.isArray(astrange) && astrange.length !== 3) throw Error("ASTNODE choice need to have shape [[id, s, e], ch]");
    for (let choice of choices_list) {
      if (choice.length !== 2 && (!Array.isArray(choice[0])) && choice[0].length !== 3) throw Error("ASTNODE choice need to have shape [[id, s, e], ch]. Existing choice wrong format.");
      if (choice[0][0] === astrange[0] && choice[0][1] === astrange[1] && choice[0][2] === astrange[2]) {
        is_set = true;
        if (idx !== 0) new_choices_list.push([astrange, idx]);
      } else {
        new_choices_list.push(choice);
      }
    }
    if (!is_set) new_choices_list.push([astrange, idx]);

  } else {
    throw Error("updateChoices Unknown type: " + type);
  }

  new_choices = {
    "type": type,
    "choices_list": new_choices_list
  };
  let new_str = JSON.stringify(new_choices);
  choices_input_elem.value = new_str;
}


// ==========================================================
// ==========================================================
// ==================== Const funcs =========================
function decodeNodeId(nodeId) {
  if (nodeId.startsWith("source")) return ["source", nodeId.replace("source", "")];
  else if (nodeId.startsWith("target")) return ["target", nodeId.replace("target", "")];
  throw "nodeId_invalid";
}

function decodeComboId(comboId) {
  if (comboId.startsWith("c_source")) return ["source", comboId.replace("c_source", "")];
  else if (comboId.startsWith("c_target")) return ["target", comboId.replace("c_target", "")];
  throw "comboId_invalid";
}

function getDirectNodeIdsByComboId(comboId) {
  let [side, id] = decodeComboId(comboId);
  return [side, [side + id]];
}


// ==========================================================
// ==========================================================
// ======================== MONACO ========================
function prepareDecoration(source_ann, target_ann) {
  for (let id in source_ann) {
    let start = source_ann[id][2];
    let end = source_ann[id][3];
    let decoDict = {
      range: new monaco.Range(start[0] + 1, start[1] + 1, end[0] + 1, end[1] + 1),
      options: { inlineClassName: 'myMonacoInlineDecoration' }
    };
    let myDecoDict = { "isOn": false, "deco": decoDict };
    source_decoration_dict["source" + id] = myDecoDict;
  }
  for (let id in target_ann) {
    let start = target_ann[id][2];
    let end = target_ann[id][3];
    let decoDict = {
      range: new monaco.Range(start[0] + 1, start[1] + 1, end[0] + 1, end[1] + 1),
      options: { inlineClassName: 'myMonacoInlineDecoration' }
    };
    let myDecoDict = { "isOn": false, "deco": decoDict };
    target_decoration_dict["target" + id] = myDecoDict;
  }
  //console.log("prepareDecoration done.", source_decoration_dict, target_decoration_dict);
}

function update_monaco_decoration_dicts_by_astvis_edit_state() {
  //set all to false
  for(let nodeId in source_decoration_dict) source_decoration_dict[nodeId].isOn = false;
  //set on
  function _setNodeIdsClassName(nodeIds, decoDict, classname) {
    nodeIds.forEach((nodeId) => {
      decoDict[nodeId].isOn = true;
      decoDict[nodeId].deco.options.inlineClassName = classname
    });
  }
  _setNodeIdsClassName(astvis_edit_state.node.hover.source, source_decoration_dict, "mymonaco-hover");

  function _setNodesOfComboIdsClassName(comboIds, decoDict, classname) {
    for (let comId of comboIds) {
      let [_, nodeIds] = getDirectNodeIdsByComboId(comId);
      _setNodeIdsClassName(nodeIds, decoDict, classname);
    }
  }
  _setNodesOfComboIdsClassName(astvis_edit_state.combo.hover.source, source_decoration_dict, "mymonaco-hover");
  _setNodesOfComboIdsClassName(astvis_edit_state.combo.selected.source, source_decoration_dict, "mymonaco-selected");
  _setNodesOfComboIdsClassName(astvis_edit_state.combo.expanmatch.source, source_decoration_dict, "mymonaco-expanmatch");
  _setNodesOfComboIdsClassName(astvis_edit_state.combo.expanslotmatch1.source, source_decoration_dict, "mymonaco-expanslotmatch1");
  _setNodesOfComboIdsClassName(astvis_edit_state.combo.expanslotmatch2.source, source_decoration_dict, "mymonaco-expanslotmatch2");
}


let _source_decoration_old_decids = [];
let _target_decoration_old_decids = [];
function update_monaco_marks_by_decoration_dicts() {
  //see the doc about adding decorations in monaco editor
  //https://microsoft.github.io/monaco-editor/playground.html#interacting-with-the-editor-line-and-inline-decorations
  let sourceDecoList = Object.keys(source_decoration_dict).map((nodeId) => source_decoration_dict[nodeId]["isOn"] ? source_decoration_dict[nodeId]["deco"] : null).filter(x => x !== null);
  //let targetDecoList = Object.keys(target_decoration_dict).map((nodeId) => target_decoration_dict[nodeId]["isOn"] ? target_decoration_dict[nodeId]["deco"] : null).filter(x => x !== null);
  _source_decoration_old_decids = source_lang_editor_obj.deltaDecorations(
    _source_decoration_old_decids, sourceDecoList);
  // _target_decoration_old_decids = target_lang_editor_obj.deltaDecorations(
  //   _target_decoration_old_decids, targetDecoList);
}

let _transprog_decoration_old_decids = [];
function update_monaco_highlight_locate_for_trans(start, end) {
  //console.log("# update_monaco_highlight_locate_for_trans:", start, end);
  if(start === undefined || start === null || end === undefined || end === null) {
    console.error("invaid start and end!");
    throw "FAILED_update_monaco_highlight_locate_for_trans";
  }
  function _decoration(start, end, className) {
    const sp = target_trans_editor_obj.getModel().getPositionAt(start);
    const ep = target_trans_editor_obj.getModel().getPositionAt(end);
    let range = new monaco.Range(sp.lineNumber, sp.column, ep.lineNumber, ep.column);
    //console.log(sp, ep, range);
    //hacky. reveal the line.
    target_trans_editor_obj.revealLine(sp.lineNumber);
    target_trans_editor_obj.revealLine(ep.lineNumber);
    return {
      range: range, options: { inlineClassName: className}
    };
  }
  let new_decos = [];
  if (start !== -1 && end !== -1) {
    new_decos.push(_decoration(start, end, 'mymonaco-locate'));
  }
  _transprog_decoration_old_decids = target_trans_editor_obj.deltaDecorations(
    _transprog_decoration_old_decids, new_decos);
}


// ==========================================================
// ==========================================================
// ================ G6 GRAPH and tabulator ==================

//graph viz is deferred in this function
let graph_visualize_pack_func = null;
delayed_graph_visualize_btn.addEventListener("click", () => {
  if (graph_visualize_pack_func !== null) {
    graph_visualize_pack_func();
    graph_visualize_pack_func = null;
  } else {
    alert("[INFO] No visualization available.");
  }
})

function visualizeAST(useCostomLayout, sourceLang, targetLang, source_AST_dict, target_AST_dict, source_AST, target_AST, source_ann, target_ann, dbg_history, translator_dbg_info, translate_result, translated_code_updater_func) {
  console.log("============================= visualizeAST begin =============================");
  //last time cleaning
  if(panel_dbg_history_table_obj !== null && panel_dbg_history_table_obj !== undefined) panel_dbg_history_table_obj.destroy();
  ast_source_info_elem.innerText = "Source";
  ast_target_info_elem.innerText = "Target";
  ast_common_info_elem.innerText = "------";
  graph_visualize_pack_func = null;
  astvis_edit_state.reset();
  resetDecorationDicts();
  prepareDecoration(source_ann, target_ann);
  //---------------------------------------------------------- INFO BAR
  function updateNodeInfo(side, nodeId) {
    function _astNodeToLabel(astNode) {
      if (astNode !== null && astNode !== undefined) {
        let nt = astNode[0];
        return nt + "-" + astNode[1];
      }
      return "<ERROR>";
    }
    if (nodeId === null || nodeId === undefined) {
      ast_source_info_elem.innerText = "";
      ast_target_info_elem.innerText = "";
    } else {
      if (side === "source") {
        ast_source_info_elem.innerText = _astNodeToLabel(source_AST_dict[nodeId]);
      } else if (side === "target") {
        ast_target_info_elem.innerText = _astNodeToLabel(target_AST_dict[nodeId]);
      } else {
        throw "updateNodeInfo_unknown_side";
      }
      return true;
    }
  }
  function updateCompoInfo(comId, expectedSide) {
    function _comboIdToLabel(comId, side, mainId) {
      if (mainId !== null && mainId !== undefined) {
        let astNode = null;
        let astDict = null;
        if (side === "source") { astDict = source_AST_dict; astNode = source_AST_dict[mainId]; }
        else if (side === "target") { astDict = target_AST_dict; astNode = target_AST_dict[mainId]; }
        let nt = astNode[0];
        return nt + "|" + mainId;
      }
      return "<" + comId + ">";
    }
    if (comId === null || comId === undefined) {
      if (expectedSide === "source") ast_source_info_elem.innerText = "";
      else if (expectedSide === "target") ast_target_info_elem.innerText = "";
      else return false;
    } else {
      let [side, id] = decodeComboId(comId);
      if (expectedSide !== null && expectedSide !== undefined && side !== expectedSide) return false;
      if (side === "source") {
        ast_source_info_elem.innerText = _comboIdToLabel(comId, side, id);
      } else if (side === "target") {
        ast_target_info_elem.innerText = _comboIdToLabel(comId, side, id);
      } else {
        throw "updateCompoInfo_unknown_side";
      }
      return true;
    }
  }
  function updateCompoPairInfo(comId1, comId2) {
    if (comId1 === null && comId2 === null) {
      updateCompoInfo(null, "source");
      updateCompoInfo(null, "target");
    } else {
      updateCompoInfo(null, "source");
      updateCompoInfo(null, "target");
      let b1 = updateCompoInfo(comId1, null);
      let b2 = updateCompoInfo(comId2, null);
      if (!(b1 || b2)) throw "updateCompoPairInfo_failed";
    }
  }

  let _update_graph_item_states_by_astvis_edit_state_func = null;
  graph_visualize_pack_func = () => {
    let nodes = [];
    let edges = [];
    let combos = [];
    let addNode = (id, comboId, subGraphId, x, y) => nodes.push({ id: id, comboId: comboId, subGraphId: subGraphId, orix: x, oriy: y });
    let addEdge = (id1, id2) => edges.push({ source: id1, target: id2 });
    let addCombo = (id, parentid) => combos.push(parentid ? { id: id, parentId: parentid, padding: 3 } : { id: id, padding: 4 });
    function _add_nodes_edges(ast, node_prefix, subGraphId, combo_prefix, get_offset_x, get_offset_y) {
      let order = 1;
      let fill_level = 0;
      function _add_nodes_edges_rec(parentid, current, level) {
        if (Array.isArray(current)) {
          if (current[0] === "anno") return;
          let currentid = node_prefix + current[1];
          if (level <= fill_level) {
            order += 1;
          }
          fill_level = level;
          let comboId = combo_prefix + currentid;
          let comboParentId = null;
          if (parentid !== null) comboParentId = combo_prefix + parentid;
          addCombo(comboId, comboParentId);
          addNode(currentid, comboId, subGraphId, get_offset_x(level), get_offset_y(level, order));
          if (parentid !== null) addEdge(currentid, parentid);
          for (let i = 2; i < current.length; i++) {
            _add_nodes_edges_rec(currentid, current[i], level + 1);
          }
        }
      }
      _add_nodes_edges_rec(null, ast, fill_level + 1);
    };
    _add_nodes_edges(source_AST, "source", 1, "c_", (x) => - 30 * x, (x, y) => 28 * y + 0 * x);
    _add_nodes_edges(target_AST, "target", 2, "c_", (x) => + 30 * x, (x, y) => 28 * y + 0 * x);
    let data = {
      nodes: nodes,
      edges: edges,
      combos: combos,
    };
    console.log("# visualization data:", data);
    let graph_init = {
      fitView: true,
      fitViewPadding: 20,
      minZoom: 0.00000001,
      container: 'ast-visualization-container', // String | HTMLElement
      modes: {
        default: [
          // checkout document about default behavior
          //https://g6.antv.vision/en/docs/manual/middle/states/defaultBehavior
          // 'drag-canvas', 'zoom-canvas', 'click-select', 'tooltip'
          // 'create-edge', 'shortcuts-call', 'activate-relations'
          {
            type: 'collapse-expand-combo',
            relayout: true,
          },
        ]
      },
      defaultNode: {
        size: 9,
        type: 'circle',
        style: {
          lineWidth: 1,
          stroke: '#5B8FF9',
          fill: '#C6E5FF',
        },
      },
      defaultCombo: {
        type: 'rect',
      },
      nodeStateStyles: {
        hover: {
          fill: 'purple',
        },
      },
      comboStateStyles: {
        hover: {
          fill: 'lightblue',
        },
        nomatch: {
          lineWidth: 1,
          stroke: '#CC1111',
          fill: '#FFCCCC'
        },
        expanmatch: {
          fill: '#FFF582',
        },
        expanslotmatch1: {
          fill: 'greenyellow',
        },
        expanslotmatch2: {
          fill: 'lightgreen',
        },
      },
      animate: false,
    }
    if (useCostomLayout) {
      graph_init["layout"] = {
        type: 'PairAST',
      };
    } else {
      graph_init["layout"] = {
        pipes: [
          {
            type: 'dagre',
            nodesFilter: (node) => node.subGraphId === '1',
            direction: 'LR',
          },
          {
            type: 'dagre',
            nodesFilter: (node) => node.subGraphId === '2',
            direction: 'RL',
          }
        ]
      };
    }
    ast_container_elem.innerHTML = '';
    const graph = new G6.Graph(graph_init);
    _update_graph_item_states_by_astvis_edit_state_func = function () {
      // console.log("updateGraphItemStates");
      //clear all node's states
      for (let node of graph.cfg.nodes) {
        graph.clearItemStates(node);
      }
      for (let sourceId of astvis_edit_state.node.hover.source) {
        graph.setItemState(_getNodeItemById(sourceId), 'hover', true);
      }
      //clear all combo's states
      //https://g6.antv.vision/en/docs/api/graphFunc/state#graphclearitemstatesitem-states
      for (let combo of graph.cfg.combos) {
        graph.clearItemStates(combo);
      }
      function _setComboIdListState(comIdList, state, val) {
        for (let targetId of comIdList) {
          graph.setItemState(_getComboItemById(targetId), state, val);
        }
      }
      _setComboIdListState(astvis_edit_state.combo.hover.source, "hover", true);
      _setComboIdListState(astvis_edit_state.combo.nomatch.source, "nomatch", true);
      _setComboIdListState(astvis_edit_state.combo.selected.source, "selected", true);
      _setComboIdListState(astvis_edit_state.combo.expanmatch.source, "expanmatch", true);
      _setComboIdListState(astvis_edit_state.combo.expanslotmatch1.source, "expanslotmatch1", true);
      _setComboIdListState(astvis_edit_state.combo.expanslotmatch2.source, "expanslotmatch2", true);
    }
    function _updateGraphSize() {
      astvis_width = ast_container_elem.clientWidth - 5;
      astvis_height = astvis_width * astvis_ratio;
      graph.changeSize(astvis_width, astvis_height);
      console.log("graph size updated:", astvis_width, astvis_height);
    }
    graph.data(data);
    graph.layout(data);

    console.log("# initial astvis draw setTimeout.");
    function _initialDraw() {
      console.log("# initial astvis draw begin...");
      _updateGraphSize();
      graph.render();
      console.log("# initial astvis draw done.");
    }
    setTimeout(_initialDraw, 100);
    setTimeout(_initialDraw, 150);

    window.onresize = function () {
      _updateGraphSize();
      graph.render();
      _update_graph_item_states_by_astvis_edit_state_func();
    };

    graph.on('dragend', function (e) {
      console.log("graph dragend.");
    });

    function _getNodeItemById(nodeId) {
      for (let node of graph.cfg.nodes) {
        if (node["_cfg"]["id"] === nodeId) return node;
      }
      throw "node_not_found_" + nodeId;
    };
    function _getComboItemById(comboId) {
      for (let combo of graph.cfg.combos) {
        if (combo["_cfg"]["id"] === comboId) return combo;
      }
      throw "combo_not_found_" + comboId;
    };

    let isFreezing = false;
    function _getNodeEventHandler(eventName) {
      return function (e) {
        if(isFreezing) return;
        let nodeInternal = e["item"]["_cfg"];
        let nodeModel = nodeInternal["model"];
        let nodeId = nodeModel["id"];
        let [side, id] = decodeNodeId(nodeId);

        // const nodeItem = e.item;
        if (eventName === 'mouseenter') {
          astvis_edit_state.set_single_node_auto(nodeId, "hover");
          updateNodeInfo(side, id);
        } else if (eventName === 'mouseleave') {
          astvis_edit_state.node.hover.source = [];
          astvis_edit_state.node.hover.target = [];
          updateNodeInfo(side, null);
        } else {
          throw "Unknown_node_event_" + eventName;
        }

        _update_graph_item_states_by_astvis_edit_state_func();
        update_monaco_decoration_dicts_by_astvis_edit_state();
        update_monaco_marks_by_decoration_dicts();
      }
    }
    function _getComboEventHandler(eventName) {
      return function (e) {
        if(isFreezing) return;
        let comboInternal = e["item"]["_cfg"];
        let comboModel = comboInternal["model"];
        let comId = comboModel["id"];

        if (eventName === 'mouseenter') {
          astvis_edit_state.set_single_combo_auto(comId, "hover");
          updateCompoPairInfo(comId, null);
        } else if (eventName === 'mouseleave') {
          astvis_edit_state.combo.hover.source = [];
          astvis_edit_state.combo.hover.target = [];
          updateCompoPairInfo(null, null);
        } else {
          throw "Unknown_combo_event_" + eventName;
        }

        _update_graph_item_states_by_astvis_edit_state_func();
        update_monaco_decoration_dicts_by_astvis_edit_state();
        update_monaco_marks_by_decoration_dicts();
        // console.log(eventName + "update state:", source_decoration_common_states, target_decoration_common_states);
      }
    }
    graph.on('node:mouseenter', _getNodeEventHandler("mouseenter"));
    graph.on('node:mouseleave', _getNodeEventHandler("mouseleave"));
    graph.on('combo:mouseenter', _getComboEventHandler("mouseenter"));
    graph.on('combo:mouseleave', _getComboEventHandler("mouseleave"));
    graph.on('node:click', () => {isFreezing = !isFreezing;});
    graph.on('combo:click', () => {isFreezing = !isFreezing;});
  };

  //history table
  function choicesClickHandler(e) {
    let update_choices_param = e.target._update_choices_param;
    let {step, target_choose_idx, range_info} = update_choices_param;
    updateChoices(step, range_info, target_choose_idx);
  }
  let changeOp = function(cell, formatterParams, onRendered){
    let row_data = cell.getRow().getData();
    let step = row_data["step"];
    let nch_count_str = row_data["ch_com"].split("/")[1].replace("+", "");
    let nch_count = nch_count_str === "??" ? 1 : parseInt(nch_count_str) + 1;
    let nch_done = (!row_data["ch_com"].endsWith("+")) || row_data["ch_com"].endsWith("??");
    let choose_idx = row_data["choose_idx"];
    console.log("# create changeOp button:", step, nch_count_str, nch_count, nch_done, choose_idx);
    let divElem = document.createElement("div");
    if (nch_count == 1 && nch_done) return divElem;
    if (choose_idx > 0) {
      //should have left btn
      let leftBtn = document.createElement("button");
      leftBtn.className = "tiny-btn";
      leftBtn.innerText = "<";
      leftBtn._update_choices_param = {
        "step": step,
        "target_choose_idx": choose_idx - 1,
        "range_info": row_data["range_info"]
      };
      leftBtn.addEventListener("click", choicesClickHandler);
      divElem.appendChild(leftBtn);
    }
    if (choose_idx < nch_count - 1 || (!nch_done)) {
      //should have right btn
      let rightBtn = document.createElement("button");
      rightBtn.className = "tiny-btn";
      rightBtn.innerText = ">";
      rightBtn._update_choices_param = {
        "step": step,
        "target_choose_idx": choose_idx + 1,
        "range_info": row_data["range_info"]
      };
      rightBtn.addEventListener("click", choicesClickHandler);
      divElem.appendChild(rightBtn);
    }
    return divElem;
  };
  //display history
  panel_dbg_history_table_obj = new Tabulator("#panel-dbg-history-table", {
    data: [], //set initial table data
    height:"calc(100% - 4px)",
    columns: [
      { title: "step", field: "step" },
      { title: "ch", field: "ch_com" },
      { title: "", formatter: changeOp, hozAlign:"center" },
      { title: "rule", field: "rule_id" },
      { title: "slot", field: "slot" },
      { title: "loop", field: "loop_count" },
      { title: "out", field: "outcome" },
      { title: "new_slots", field: "new_slots" },
      { title: "rule_summary", field: "rule_summary" },
    ],
    rowFormatter: function(row){
      let rowData = row.getData();
      let stepOut = rowData["outcome"];
      if (stepOut === "ER" || stepOut == "RE"){
        const children = row.getElement().childNodes;
        children.forEach((child) => {
          child.style.cssText +=
          "background: rgb(255 85 84 / 50%);";
        });
      }
    },
    tooltipGenerationMode: "hover",
  });
  function _get_table_data(dbg_history, translator_dbg_info) {
    let result = [];
    let summary_dict = translator_dbg_info["program"]["expansion_programs"]["summary_dict"];
    if(false) console.log("# _get_table_data. rule summary_dict:", summary_dict);
    let prev_row_data = null;
    for (let i = 0; i < dbg_history.length; i++) {
      let dbg_entry = dbg_history[i];
      if (i + 1 !== dbg_entry["alt_step"]) {
        alert("[UI_UNEXPECTED_ERROR] history index mismatch with alt_step.");
        throw "alt_step_mismatch_error";
      }
      let choose_idx = dbg_entry["dbg_info"]["notes"]["choose_idx"];
      let range_info = dbg_entry["range_info"];
      let nch_count = dbg_entry["next_choices_status"]["count"];
      let nch_done = dbg_entry["next_choices_status"]["done"];

      let row_data = {
        "step": dbg_entry["alt_step"], //TODO: hacky
        "choose_idx": choose_idx,
        "nch_count": nch_count,
        "nch_done": nch_done,
        "range_info": range_info,
        "ch_com": prev_row_data ? choose_idx.toString() + prev_row_data["_next_nch_com"] :  choose_idx.toString() + "/??",
        "_next_nch_com": "/" + (nch_count - 1).toString() + (nch_done ? "" : "+"),
        "rule_id": dbg_entry["dbg_info"]["notes"]["rule_id"],
        "slot": dbg_entry["dbg_info"]["corres_slot_id"],
        "outcome": dbg_entry["dbg_info"]["outcome"],
        "step_type": "Unknown",
        "loop_count": dbg_entry["dbg_info"]["loop_count"],
        "new_slots": dbg_entry["dbg_info"]["slot_ids"].join(", ") + " (" + dbg_entry["dbg_info"]["slot_names"].join(", ") + ")",
        "rule_summary": summary_dict[dbg_entry["dbg_info"]["notes"]["rule_id"]]
      };
      result.push(row_data);
      prev_row_data = row_data;
    }
    return result;
  }
  //table data
  let tabData = _get_table_data(dbg_history, translator_dbg_info);
  //table event handler
  let _entering_row_id = null;
  function _getTableRowEventHandler(eventName) {
    function _tabRowEventHandler(e, row) {
      let rowId = row.getCells()[0].getValue() - 1; //hacky
      let dbg_data = dbg_history[parseInt(rowId)];
      if(eventName === "mouseenter") {
        console.log("row " + eventName  + ":", rowId, dbg_data);
        _entering_row_id = rowId;
        let rule_id = dbg_data["dbg_info"]["notes"]["rule_id"];
        let loc_dict = translator_dbg_info["program"]["expansion_programs"]["rule_loc_dict"];
        console.log("# _getTableRowEventHandler mouseenter", rowId, " rule_id:", rule_id);

        //translator program highlight update
        setTimeout(async () => {
          let opt_info_id = dbg_data["dbg_info"]["elem_list_info_id"];
          let code = await cachedGetPartialCodeOptAsync(targetLang, opt_info_id);
          if (_entering_row_id === rowId) translated_code_updater_func(code);
        }, 0);
        update_monaco_highlight_locate_for_trans(loc_dict[rule_id][0], loc_dict[rule_id][1]);

        //clear and add graph visstate
        let matching_node_ids = dbg_data["dbg_info"]["src_matching_node_ids"].map((x) => "c_source" + x);
        let slot_matching_node_ids = dbg_data["dbg_info"]["slot_src_matching_node_ids"].map(ids => ids.map(x => "c_source" + x));
        astvis_edit_state.clear_multiple_combo_source("expanmatch");
        astvis_edit_state.add_multiple_combo_source(matching_node_ids, "expanmatch");
        let slot_graph_state_names = ["expanslotmatch1", "expanslotmatch2"];
        for(let cname of slot_graph_state_names) astvis_edit_state.clear_multiple_combo_source(cname);
        let classname_idx = 0;
        for(let node_ids of slot_matching_node_ids) {
          if(node_ids === null) continue;
          astvis_edit_state.add_multiple_combo_source(node_ids, slot_graph_state_names[classname_idx]);
          classname_idx = (classname_idx + 1) % 2;
        }
        //source graph and monaco highlight update
        if (_update_graph_item_states_by_astvis_edit_state_func !== null) _update_graph_item_states_by_astvis_edit_state_func();
        update_monaco_decoration_dicts_by_astvis_edit_state();
        update_monaco_marks_by_decoration_dicts();
      } else if(eventName === "click") {
        //console.warn("table row click not implemented.");
      } else {
        throw "Unknown_table_row_event_" + eventName;
      }
    }
    return _tabRowEventHandler;
  }
  panel_dbg_history_table_obj.on("rowClick", _getTableRowEventHandler("click"));
  panel_dbg_history_table_obj.on("rowMouseEnter", _getTableRowEventHandler("mouseenter"));
  panel_dbg_history_table_obj.on("headerMouseEnter", () => {
    translated_code_updater_func(translate_result ? translate_result["code"] : null);
    update_monaco_highlight_locate_for_trans(-1, -1);
    console.log("# headerMouseEnter: reset to translate_result code.");
    astvis_edit_state.clear_multiple_combo_source("expanmatch");
    astvis_edit_state.clear_multiple_combo_source("expanslotmatch1");
    astvis_edit_state.clear_multiple_combo_source("expanslotmatch2");
    if (_update_graph_item_states_by_astvis_edit_state_func !== null) _update_graph_item_states_by_astvis_edit_state_func();
    update_monaco_decoration_dicts_by_astvis_edit_state();
    update_monaco_marks_by_decoration_dicts();
    console.log("# headerMouseEnter: graph/monaco vis reset.");
  });
  setTimeout(() => panel_dbg_history_table_obj.clearData(), 0);
  setTimeout(() => panel_dbg_history_table_obj.setData(tabData), 0);
  console.log("================= visualizeAST done. ================= ");
}
