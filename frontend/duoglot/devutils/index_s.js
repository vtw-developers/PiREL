"use strict";

require.config({ paths: { vs: '../../_common/monaco/node_modules/monaco-editor/min/vs' } });


let monaco_language_name_dict = {
  "js": "javascript",
  "py": "python",
  "java": "java",
  "cs": "csharp",
  "cpp": "cpp",
}

/* Specialized UI elements */
let sourcelang_select_elem = document.getElementById("sourcelang-select");
let targetlang_select_elem = document.getElementById("targetlang-select");
let testcase_select_elem = document.getElementById("testcase-select");
let load_btn = document.getElementById("load-btn");
let parse_btn = document.getElementById("parse-btn");
let match_btn = document.getElementById("match-btn"); //dynamic handler
let match_algo_select_elem = document.getElementById("match-algo-select");
let ast_container_elem = document.getElementById("ast-visualization-container");
let ast_source_info_elem = document.getElementById("astvis-source-info-bar");
let ast_common_info_elem = document.getElementById("astvis-common-info-bar");
let ast_target_info_elem = document.getElementById("astvis-target-info-bar");
let ast_get_sexpr_btn = document.getElementById("astvis-get-sexpr-btn");
let source_lang_editor_elem = document.getElementById('source-lang-editor');
let target_lang_editor_elem = document.getElementById('target-lang-editor');
let target_trans_editor_elem = document.getElementById('target-trans-editor');
let panel_transform_source_elem = document.getElementById('panel-transform-source-viewer');
let panel_transform_target_elem = document.getElementById('panel-transform-target-viewer');
let panel_mapping_elem = document.getElementById('panel-mapping-viewer');
let panel_mapping_main_table_elem = document.getElementById("panel-mapping-main-table");
let panel_mapping_main_table_obj = null;
let source_lang_editor_obj = null;
let target_lang_editor_obj = null;
let target_trans_editor_obj = null;

let file_dict = null;
let source_AST = null;
let source_AST_dict = null; //int id
let source_ann = null;
let target_AST = null;
let target_AST_dict = null; //int id
let target_ann = null;

//map of comboId. updated by match api call. read only
let combo_match_info = { 
  "by_source": {}, 
  "by_target": {},
  reset: () => {
    combo_match_info.by_source = {},
    combo_match_info.by_target = {}
  }
};
//UI states for ast visualizer
let astvis_edit_state = {
  "node": {
    "hover": { "source": [], "target": [] },
  },
  "combo": {
    "nomatch": { "source": [], "target": [] },
    "selected": { "source": [], "target": [] },
    "hover": { "source": [], "target": [] },
    "grouphover": {"_id": null, "stateNames": ["scpink1", "scpink2"], "st_nullable_pairs": []},
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
  set_combo_grouphover: (_id, pairs) => {
    astvis_edit_state.combo.grouphover._id = _id;
    astvis_edit_state.combo.grouphover.st_nullable_pairs = pairs;
  },
  clear_combo_grouphover: () => {
    astvis_edit_state.combo.grouphover._id = null;
    astvis_edit_state.combo.grouphover.st_nullable_pairs = [];
  },
  reset: () => {
    astvis_edit_state["node"] = {
      "hover": { "source": [], "target": [] },
    };
    astvis_edit_state["combo"] = {
      "nomatch": { "source": [], "target": [] },
      "selected": { "source": [], "target": [] },
      "hover": { "source": [], "target": [] },
      "grouphover": {"_id": null, "stateNames": ["scpink1", "scpink2"], "st_nullable_pairs": []},
    };
  },
};
let astvis_ratio = 3;
let astvis_width = null;
let astvis_height = null;
//UI states for monaco editor
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


load_btn.addEventListener("click", loadHandlerAsync);
parse_btn.addEventListener("click", parseSourceHandlerAsync);
ast_get_sexpr_btn.addEventListener("click", astGetSexprHandler);

(async function main1() {
  getFileDictHandlerAsync();

  //about updating options:
  //https://stackoverflow.com/questions/64466716/conditonally-wrap-line-in-monaco-editor

  //the demo code is not a real file
  require(['vs/editor/editor.main'], function () {
    source_lang_editor_obj = monaco.editor.create(source_lang_editor_elem, {
      // value: ['def x():', '\tprint("Hello world!")', ''].join('\n'),
      language: 'python',
      wordWrap: "on",
      automaticLayout: true
    });
    target_lang_editor_obj = monaco.editor.create(target_lang_editor_elem, {
      // value: ['function x() {', '\tconsole.log("Hello world!");', '}'].join('\n'),
      language: 'javascript',
      wordWrap: "on",
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

//https://g6.antv.vision/en/docs/manual/middle/layout/custom-layout/
(async function main2() {
  G6.registerLayout('PairAST', {
    getDefaultCfg() {
      //The default configurations will be mixed by configurations from user
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
      //update cfg
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


async function getFileDictHandlerAsync() {
  let file_dict = await getTestfilesAsync();
  console.log("# got file_dict:", file_dict);
  function _updateTestcasesSelect() {
    let sourceLang = sourcelang_select_elem.value;
    let targetLang = targetlang_select_elem.value;
    console.log("_updateTestcasesSelect: ", sourceLang, targetLang);

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
  _updateTestcasesSelect();
  sourcelang_select_elem.onchange = _updateTestcasesSelect;
  targetlang_select_elem.onchange = _updateTestcasesSelect;
}

async function loadHandlerAsync() {
  //TODO: read sourcelang, targetlang, testcase
  let srcLang = sourcelang_select_elem.value;
  let tarLang = targetlang_select_elem.value;
  let option2SourcePath = (x) => "duoglot/tests/basic/" + srcLang + "/" + x + "." + srcLang;
  let option2TargetPath = (x) => "duoglot/tests/basic/" + tarLang + "/" + x + "." + tarLang;
  let tranlatorPath = (translator_name) => "duoglot/tests/trans_programs/" + srcLang + "_" + tarLang + "/" + translator_name + ".snart";
  let defaultTranslatorPath = tranlatorPath("default");

  let selectedValue = testcase_select_elem.value;
  if (selectedValue === null || selectedValue === undefined || selectedValue === "") {
    alert("No testcase is selected.");
    return;
  }
  let sourcePath = option2SourcePath(selectedValue);
  let targetPath = option2TargetPath(selectedValue);

  console.log("Load testcase " + selectedValue + "...");
  let sourceCodeStr = await anyfileAsync(sourcePath);
  let targetCodeStr = await anyfileAsync(targetPath);

  let srcModel = source_lang_editor_obj.getModel(); 
  monaco.editor.setModelLanguage(srcModel, monaco_language_name_dict[srcLang]);
  source_lang_editor_obj.setValue(sourceCodeStr);

  let tarModel = target_lang_editor_obj.getModel();
  monaco.editor.setModelLanguage(tarModel, monaco_language_name_dict[tarLang]);
  target_lang_editor_obj.setValue(targetCodeStr);

  console.log("Load translator program (if any)...");
  try {
    let progCodeStr = await anyfileAsync(defaultTranslatorPath);
    target_trans_editor_obj.setValue(progCodeStr);
  } catch (error) {
    console.warn("Translator program not loaded. Default might not exist.", error);
    target_trans_editor_obj.setValue("; empty ...");
  }
}

async function parseSourceHandlerAsync() {
  let source_code = source_lang_editor_obj.getValue();
  let target_code = target_lang_editor_obj.getValue();
  
  console.log("# parsing:", sourcelang_select_elem.value, targetlang_select_elem.value);
  let source_result = await parseAsync(source_code, sourcelang_select_elem.value);
  let target_result = await parseAsync(target_code, targetlang_select_elem.value);
  source_AST = source_result[0];
  source_ann = source_result[1];
  target_AST = target_result[0];
  target_ann = target_result[1];
  source_AST_dict = {};
  target_AST_dict = {};
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
  astToDictRec(target_AST, target_AST_dict);
  console.log("source_code:", source_AST, "source_ann:", source_ann);
  console.log("target_code:", target_AST, "target_ann:", target_ann);
  visualizeAST(true);
}

function get_s_expr(ast_node, depth_val, is_ignore_str) {
  if (ast_node === null) return ["null", ["input is null."]];
  let logs = [];
  function _log() {logs.push(Array.from(arguments).join(" "));}
  _log("depth_val:", depth_val, " is_ignore_str:", is_ignore_str);
  function _s_expr_rec(ast_node, parname, depth) {
    if (depth >= depth_val) {
      _log("ignoring node at", depth)
      return "...";
    }
    if (Array.isArray(ast_node)) {
      if (ast_node[0] === "anno") {
        let ret_arr = ['(anno '];
        for(let i = 1; i < ast_node.length; i++) {
          ret_arr.push(" ");
          ret_arr.push("(");
          ret_arr.push(ast_node[i][0]);
          ret_arr.push(" ");
          ret_arr.push(ast_node[i][1]);
          ret_arr.push(")");
        }
        ret_arr.push(")");
        return ret_arr.join("");
      } else {
        let ret_arr = ['("' + ast_node[0] + '"'];
        for(let i = 2; i < ast_node.length; i++) {
          ret_arr.push(" ");
          ret_arr.push(_s_expr_rec(ast_node[i], ast_node[0], depth + 1));
        }
        ret_arr.push(")");
        return ret_arr.join("");
      }
    }
    else if (typeof(ast_node) == "number") {
      _log("WARN Unexpected ast_node:", ast_node);
    }
    else {
      if (parname.indexOf("identifier") > 0) {
        return '(val ' + ast_node + ')';
      } else if (parname.indexOf("number") > 0 || parname.indexOf("integer") > 0) {
        return '(val ' + ast_node.slice(1, -1) + ')';
      } else {
        if(is_ignore_str) {
          _log("str node (ignored):", ast_node);
          return "";
        }
        return '(str ' + ast_node + ')';
      }
    }
  }
  return [_s_expr_rec(ast_node, ast_node[0], 0), logs];
}

/* General UI elements */
let pop_window_wrapper = document.getElementById("pop-window-wrapper");
let pop_window1_text_viewer_elem = document.getElementById("pop-window1-text-viewer");
let pop_window1_log_viewer_elem = document.getElementById("pop-window1-log-viewer");
let pop_window1_range1_elem = document.getElementById("pop-window1-range1");
let pop_window1_checkbox1_elem = document.getElementById("pop-window1-checkbox1");
function set_pop_window_visibility(visibility) {
  if(visibility) {
    pop_window_wrapper.classList.remove("display-none");
  } else {
    pop_window_wrapper.classList.add("display-none");
  }
}

function astGetSexprHandler() {
  let depth_val = pop_window1_range1_elem.value;
  let is_ignore_str = pop_window1_checkbox1_elem.checked;
  let src_hover_ids = astvis_edit_state["combo"]["hover"]["source"];
  let tar_hover_ids = astvis_edit_state["combo"]["hover"]["target"];
  let src_hover_id = null;
  let tar_hover_id = null;
  if (src_hover_ids.length > 0) src_hover_id = src_hover_ids[0];
  if (tar_hover_ids.length > 0) tar_hover_id = tar_hover_ids[0];
  if (src_hover_id === null && tar_hover_id === null) {
    alert("Please choose at least 1 source node or 1 target node (in hover state).");
    return;
  }
  if (src_hover_ids.length !== 1 && tar_hover_ids.length !== 1) {
    alert("Unexpected. astGetSexprHandler expect at most 1 source node and 1 target node are in hover state.");
    return;
  }
  
  let src_node = src_hover_id ? source_AST_dict[src_hover_id.replace("c_source", "")] : null;
  let tar_node = tar_hover_id ? target_AST_dict[tar_hover_id.replace("c_target", "")] : null;
  console.log("astGetSexprHandler.", src_node, tar_node);
  let [src_str, src_log] = get_s_expr(src_node, depth_val, is_ignore_str);
  let [tar_str, tar_log] = get_s_expr(tar_node, depth_val, is_ignore_str);
  pop_window1_text_viewer_elem.value = src_str + "\n\n--------------\n\n" + tar_str;
  let log_str = "----src get_s_expr log----\n" + src_log.join("\n") + "\n\n----tar get_s_expr log----\n" + tar_log.join("\n");
  pop_window1_log_viewer_elem.innerText = log_str;
  set_pop_window_visibility(true);
}

// ==========================================================
// ==========================================================
// ======================== MONACO ========================
function prepareDecoration() {
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
  console.log("prepareDecoration done.", source_decoration_dict, target_decoration_dict);
}

function update_monaco_decoration_dicts_by_astvis_edit_state() {
  //set all to false
  for(let nodeId in source_decoration_dict) source_decoration_dict[nodeId].isOn = false;
  for(let nodeId in target_decoration_dict) target_decoration_dict[nodeId].isOn = false;
  //set on
  function _setNodeIdsClassName(nodeIds, decoDict, classname) {
    nodeIds.forEach((nodeId) => {
      decoDict[nodeId].isOn = true; 
      decoDict[nodeId].deco.options.inlineClassName = classname
    });
  }
  _setNodeIdsClassName(astvis_edit_state.node.hover.target, target_decoration_dict, "mymonaco-hover");
  _setNodeIdsClassName(astvis_edit_state.node.hover.source, source_decoration_dict, "mymonaco-hover");
  
  function _setNodesOfComboIdsClassName(comboIds, decoDict, classname) {
    for (let comId of comboIds) {
      let [_, nodeIds] = getDirectNodeIdsByComboId(comId);
      _setNodeIdsClassName(nodeIds, decoDict, classname);
    }
  }
  _setNodesOfComboIdsClassName(astvis_edit_state.combo.hover.target, target_decoration_dict, "mymonaco-hover");
  _setNodesOfComboIdsClassName(astvis_edit_state.combo.hover.source, source_decoration_dict, "mymonaco-hover");
  _setNodesOfComboIdsClassName(astvis_edit_state.combo.selected.target, target_decoration_dict, "mymonaco-selected");
  _setNodesOfComboIdsClassName(astvis_edit_state.combo.selected.source, source_decoration_dict, "mymonaco-selected");

  let currentStateNameIdx = 0;
  let candidateStateNames = astvis_edit_state.combo.grouphover.stateNames;
  for(let pair of astvis_edit_state.combo.grouphover.st_nullable_pairs) {
    let [srcComId, tarComId] = pair;
    let stateName = candidateStateNames[currentStateNameIdx];
    if(srcComId !== null && srcComId !== undefined) _setNodesOfComboIdsClassName([srcComId], source_decoration_dict, "mymonaco-" + stateName);
    if(tarComId !== null && tarComId !== undefined) _setNodesOfComboIdsClassName([tarComId], target_decoration_dict, "mymonaco-" + stateName);
    currentStateNameIdx = (currentStateNameIdx + 1) % candidateStateNames.length;
  }
}


let _source_decoration_old_decids = [];
let _target_decoration_old_decids = [];
function update_monaco_marks_by_decoration_dicts() {
  //see the doc about adding decorations in monaco editor
  //https://microsoft.github.io/monaco-editor/playground.html#interacting-with-the-editor-line-and-inline-decorations
  let sourceDecoList = Object.keys(source_decoration_dict).map((nodeId) => source_decoration_dict[nodeId]["isOn"] ? source_decoration_dict[nodeId]["deco"] : null).filter(x => x !== null);
  let targetDecoList = Object.keys(target_decoration_dict).map((nodeId) => target_decoration_dict[nodeId]["isOn"] ? target_decoration_dict[nodeId]["deco"] : null).filter(x => x !== null);
  _source_decoration_old_decids = source_lang_editor_obj.deltaDecorations(
    _source_decoration_old_decids, sourceDecoList);
  _target_decoration_old_decids = target_lang_editor_obj.deltaDecorations(
    _target_decoration_old_decids, targetDecoList);
  // console.log("src_deco_list:", sourceDecoList, "tar_deco_list:", targetDecoList);
  // console.log("src_decids:", _source_decoration_old_decids, "tar_decids:", _target_decoration_old_decids);
}


// ==========================================================
// ==========================================================
// ======================== INFO BAR ========================
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


// ==========================================================
// ==========================================================
// ======================== G6 GRAPH ========================
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

function getComboInfoTreePair(graph) {
  console.log("getComboInfoTreePair called:", graph.cfg.comboTrees);
  function _getComboInfoTreeRec(combo) {
    if (combo["itemType"] !== "combo") throw "item_not_combo";
    let comboInfoTree = { "comboId": combo["id"], "mainId": null, "children": [] };
    if (combo["children"]) {
      for (let child of combo["children"]) {
        if (child["itemType"] === "node") {
          if (comboInfoTree["mainId"] === null) comboInfoTree["mainId"] = child["id"];
          else throw "Multiple_main_node_inside_combo";
        }
        if (child["itemType"] !== "combo") continue;
        comboInfoTree["children"].push(_getComboInfoTreeRec(child));
      }
    }
    return comboInfoTree;
  }
  let comboTrees = graph.cfg.comboTrees;
  if (comboTrees.length !== 2) {
    alert("Expecting exactly two combo trees.");
    throw "comboTrees_not_two";
  }
  let sourceComboTree = null;
  let targetComboTree = null;
  if (comboTrees[0]["id"] === "c_source0") {
    sourceComboTree = comboTrees[0];
    if (comboTrees[1]["id"] !== "c_target0") {
      alert("Target combo tree has unexpected id:", comboTrees[1]["id"]); throw "comboTree_target_id_unexpected";
    }
    targetComboTree = comboTrees[1];
  } else if (comboTrees[0]["id"] === "c_target0") {
    targetComboTree = comboTrees[0];
    if (comboTrees[1]["id"] !== "c_source0") {
      alert("Source combo tree has unexpected id:", comboTrees[1]["id"]); throw "comboTree_source_id_unexpected";
    }
    sourceComboTree = comboTrees[1];
  } else {
    alert("Combo tree has unexpected id:", comboTrees[1]["id"]); throw "comboTree_id_unexpected";
  }
  let resultSourceTree = _getComboInfoTreeRec(sourceComboTree);
  let resultTargetTree = _getComboInfoTreeRec(targetComboTree);
  console.log("getComboInfoTreePair(result):", resultSourceTree, resultTargetTree);
  return [resultSourceTree, resultTargetTree];
}

function visualizeAST(useCostomLayout) {
  console.log("============================= visualizeAST begin =============================");
  //last time cleaning
  if(panel_mapping_main_table_obj !== null && panel_mapping_main_table_obj !== undefined) panel_mapping_main_table_obj.destroy();
  ast_source_info_elem.innerText = "Source";
  ast_target_info_elem.innerText = "Target";
  ast_common_info_elem.innerText = "------";
  astvis_edit_state.reset();
  combo_match_info.reset();
  resetDecorationDicts();
  prepareDecoration();

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
        // {
        //   type: 'drag-combo',
        //   activeState: 'inactive',
        // },
        // {
        //   type: 'drag-node',
        //   comboActiveState: 'active',
        // },
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
      scpink1: {
        fill: "greenyellow"
      },
      scpink2: {
        fill: "lightgreen"
      }
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
  function _update_graph_item_states_by_astvis_edit_state() {
    // console.log("updateGraphItemStates");
    //clear all node's states
    for (let node of graph.cfg.nodes) {
      graph.clearItemStates(node);
    }
    for (let targetId of astvis_edit_state.node.hover.target) {
      graph.setItemState(_getNodeItemById(targetId), 'hover', true);
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
    _setComboIdListState(astvis_edit_state.combo.hover.target, "hover", true);
    _setComboIdListState(astvis_edit_state.combo.hover.source, "hover", true);
    _setComboIdListState(astvis_edit_state.combo.nomatch.target, "nomatch", true);
    _setComboIdListState(astvis_edit_state.combo.nomatch.source, "nomatch", true);
    _setComboIdListState(astvis_edit_state.combo.selected.target, "selected", true);
    _setComboIdListState(astvis_edit_state.combo.selected.source, "selected", true);
    
    let currentStateNameIdx = 0;
    let candidateStateNames = astvis_edit_state.combo.grouphover.stateNames;
    for(let pair of astvis_edit_state.combo.grouphover.st_nullable_pairs) {
      let [srcComId, tarComId] = pair;
      let stateName = candidateStateNames[currentStateNameIdx];
      if(srcComId !== null && srcComId !== undefined) graph.setItemState(_getComboItemById(srcComId), stateName, true);
      if(tarComId !== null && tarComId !== undefined) graph.setItemState(_getComboItemById(tarComId), stateName, true);
      currentStateNameIdx = (currentStateNameIdx + 1) % candidateStateNames.length;
    }
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
    _update_graph_item_states_by_astvis_edit_state();
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

      _update_graph_item_states_by_astvis_edit_state();
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
      let [side, _] = decodeComboId(comId);
      let comboMatchById = side === 'source' ? combo_match_info["by_source"] : combo_match_info["by_target"];
      let otherComId = comboMatchById[comId];
      // let [_, _] = otherComId === null || otherComId === undefined ? [null, null] : decodeComboId(otherComId);

      // const comboItem = e.item; // Get the target item
      // const otherComboItem = otherComId !== null && otherComId !== undefined ? getComboItemById(otherComId) : null;
      if (eventName === 'mouseenter') {
        astvis_edit_state.set_single_combo_auto(comId, "hover");
        astvis_edit_state.set_single_combo_auto(otherComId, "hover");
        updateCompoPairInfo(comId, otherComId);
      } else if (eventName === 'mouseleave') {
        astvis_edit_state.combo.hover.source = [];
        astvis_edit_state.combo.hover.target = [];
        updateCompoPairInfo(null, null);
      } else {
        throw "Unknown_combo_event_" + eventName;
      }

      _update_graph_item_states_by_astvis_edit_state();
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

  //update match handler
  match_btn.onclick = async function () {
    console.log("++++++++++++++ match_btn event handler ++++++++++++++", data);
    let [sourceComboTree, targetComboTree] = getComboInfoTreePair(graph);
    let algo_name = match_algo_select_elem.value;
    let [match_result, typematch] = await matchAsync(sourceComboTree, targetComboTree, algo_name);
    //table hover handler generator, using typematch
    function _getTableRowEventHandler(eventName) {
      function _tabRowEventHandler(e, row) {
        let rowId = row.getCells()[0].getValue();
        let ugItem = typematch[parseInt(rowId) - 1];
        if (parseInt(ugItem["id"]) !== parseInt(rowId)) throw "table_row_id_mismatch";
        // console.log("row " + eventName  + ":", rowId, ugItem);
        if(eventName === "mouseenter") {
          let observedPairs = ugItem["observedComboIdPairs"];
          astvis_edit_state.set_combo_grouphover(rowId, observedPairs);
        } else if(eventName === "mouseleave") { 
          astvis_edit_state.clear_combo_grouphover();
        } else if(eventName === "click") {  
          console.warn("table row click not implemented.");
        } else {
          throw "Unknown_table_row_event_" + eventName;
        }
        _update_graph_item_states_by_astvis_edit_state();
        update_monaco_decoration_dicts_by_astvis_edit_state();
        update_monaco_marks_by_decoration_dicts();
      }
      return _tabRowEventHandler;
    }

    //update combo_match_info
    combo_match_info["by_source"] = {};
    combo_match_info["by_target"] = {};
    //clear astvis_edit_state
    astvis_edit_state.combo.nomatch.source.length = 0;
    astvis_edit_state.combo.nomatch.target.length = 0;

    let sourceMis = 0;
    let targetMis = 0;
    for (let match of match_result) {
      let [sourceId, targetId] = match;
      if (sourceId === null && targetId === null) throw "match_both_source_target_null";
      if (sourceId !== null) combo_match_info["by_source"][sourceId] = targetId;
      else { targetMis += 1; astvis_edit_state.combo.nomatch.target.push(targetId); }
      if (targetId !== null) combo_match_info["by_target"][targetId] = sourceId;
      else { sourceMis += 1; astvis_edit_state.combo.nomatch.target.push(sourceId); }
    }
    _update_graph_item_states_by_astvis_edit_state();
    ast_common_info_elem.innerText = "[" + algo_name + ", mis:" + sourceMis + "," + targetMis + "]";
    

    panel_mapping_main_table_obj = new Tabulator("#panel-mapping-main-table", {
      data: [], //set initial table data
      height:"calc(100% - 4px)",
      columns: [
        { title: "Id", field: "id" },
        { title: "Source (NT)", field: "sourceComboNT" },
        { title: "Target (NT)", field: "targetComboNT" },
        { title: "#", field: "count" },
        { title: "Conflict Matches", field: "conflicts" },
      ],
      rowFormatter: function(row){
        let rowData = row.getData();
        if (rowData.sourceComboNT === null || rowData.targetComboNT === null){
          const children = row.getElement().childNodes;
          children.forEach((child) => {
            child.style.cssText +=
            "background: rgb(255 255 84 / 50%);";
          });
        }
        else if(rowData.conflicts.length > 0) {
          const children = row.getElement().childNodes;
          children.forEach((child) => {
            child.style.cssText +=
            "background: #faebd78c;";
          });
        }
      }
    });
    console.log("panel_mapping_main_table_obj row event handler update.");
    panel_mapping_main_table_obj.on("rowClick", _getTableRowEventHandler("click"));
    panel_mapping_main_table_obj.on("rowMouseEnter", _getTableRowEventHandler("mouseenter"));
    panel_mapping_main_table_obj.on("rowMouseLeave", _getTableRowEventHandler("mouseleave"));
    setTimeout(() => panel_mapping_main_table_obj.clearData(), 0);
    setTimeout(() => panel_mapping_main_table_obj.setData(typematch), 0);
    console.log("+++++++++++++ match-btn match_result:", match_result, "ug_proposal:", typematch);
  };
  console.log("visualizeAST done.");
}

