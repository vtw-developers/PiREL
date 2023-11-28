"use strict";

/////////////// utils begin ///////////////
function set_html_text(htmlId, text, color){
  var lab = document.getElementById(htmlId);
  set_html_text_elem(lab, text, color);
}

function set_html_text_elem(elem, text, color){
  if(elem){ elem.innerText = text; }
  if(elem){ elem.style.color = color; }
}
/////////////// utils end ///////////////

let all_iframe_elems = Array.from(document.querySelectorAll(".full-iframe"));
let dashboard_iframe_elem = document.getElementById("iframe-dashboard");
let wssocket_connect_btn = document.getElementById("wssocket-connect-btn");
let wssocket_input_elem = document.getElementById("wssocket-input");
let mainLogger = null;

const RUNNER_STATE_IDLE = "RUNNER_STATE_IDLE";
const RUNNER_STATE_ERROR = "RUNNER_STATE_ERROR";
const RUNNER_STATE_RUNNING = "RUNNER_STATE_RUNNING";
const RUNNER_STATE_DONE = "RUNNER_STATE_DONE";
const RUNNER_STATE_PAUSED = "RUNNER_STATE_PAUSED";
const RUNNER_LABEL_STATE = {
  RUNNER_STATE_IDLE: "Idle",
  RUNNER_STATE_ERROR: "Error",
  RUNNER_STATE_RUNNING: "Running",
  RUNNER_STATE_DONE: "Done",
  RUNNER_STATE_PAUSED: "Paused",
}

let request_runners = [
  {
    "button_elem": document.getElementById("iframe-tab-trans0"),
    "request_id": null,
    "runner_state": RUNNER_STATE_IDLE,
    "logger": null,
    "iframe": document.getElementById("iframe-trans0"),
  },
];

setTimeout((async function main1() {
  mainLogger = dashboard_iframe_elem.contentWindow.createLogger("logMain");
  mainLogger("Initializing...");
  request_runners[0].logger = dashboard_iframe_elem.contentWindow.createLogger("logSub1");
  mainLogger("Initialized.");
  wssocket_connect_btn.disabled = false;
  wssocket_connect_btn.onclick = tryToConnectHandler;
}), 2000);

let is_ws_connected = false;
let current_ws = null;
let ws_callbacks = {}; //dict by id
let msg_idx = 0;
async function sendSockAsync(sendobj) {
  if (current_ws === null) {
    alert("CANNOT to send message because WS does not exist.");
    throw Error("WS_Does_Not_Exist");
  }
  msg_idx += 1;
  let sendid = msg_idx;
  sendobj["id"] = sendid;
  if (sendid === null || sendid === undefined || sendid in ws_callbacks) {
    alert("CANNOT to send invalid message (no id or duplicated id).");
    throw Error("WS_message_obj_invalid");
  }
  setTimeout(() => current_ws.send(JSON.stringify(sendobj)), 0);
  return await new Promise((resolve, reject) => {
    ws_callbacks[sendid] = (dataobj) => {
      if (dataobj["answering_id"] !== sendid) {
        alert("ERROR: sendSockAsync answering_id mismatch!")
        throw Error("sendSockAsync answering_id mismatch!");
      }
      resolve(dataobj);
      ws_callbacks[sendid] = null;
    }
  })
}

async function tryToConnectHandler() {
  if (is_ws_connected) {
    alert("Already connected.");
    return;
  }
  let address = wssocket_input_elem.value;
  set_html_text("ws-stat", "Connecting...", "orange");
  var ws = new WebSocket(address);
  ws.onopen = function(evt) { 
    set_html_text("ws-stat", "ws_output open SUCCEED.", "green");
    is_ws_connected = true; 
    current_ws = ws;
    ws.send('{"type": "init"}')
  };

  ws.onmessage = async function(evt) {
    let data = evt.data;
    let show_data = data.length < 40? data : data.slice(0, 37) + "...";
    let dataobj = JSON.parse(data);
    set_html_text("ws-stat", "ws DATA received: " + show_data, "green");
    console.log("ws_receive:", dataobj);
    if(dataobj["type"] === "run_request") await runRequestAsync(dataobj);
    else if (dataobj["type"] === "result_check") {
      let ansid = dataobj["answering_id"];
      if (ansid in ws_callbacks && ws_callbacks[ansid] !== null) {
        ws_callbacks[ansid](dataobj);
      } else {
        alert("Received data has no corresponding callback. id: " + ansid);
        console.error("Received data has no corresponding callback. id: " + ansid);
      }
    } else {
      alert("Unknown data obj type: " + dataobj["type"]);
      console.error("Unknown data obj type: " + dataobj["type"]);
    }
  };

  ws.onclose = function(evt) {
    set_html_text("ws-stat", "ws CLOSED.", "red");
    is_ws_connected = false; 
    current_ws = null;
  };

  ws.onerror = function(evt) {
    set_html_text("ws-stat", "ws ERROR.", "red");
  }
}

function getIdleRequestRunner() {
  for(let runner of request_runners) {
    if (runner.runner_state == RUNNER_STATE_IDLE) return runner;
  }
  for(let runner of request_runners) {
    if (runner.runner_state == RUNNER_STATE_DONE) {
      runner.runner_state = RUNNER_STATE_IDLE;
      return runner;
    } 
  }
  return null;
}

function setTaskRunnerState(runner, state) {
  runner.runner_state = state;
  runner.button_elem.innerText = RUNNER_LABEL_STATE[state];
}

async function runRequestAsync(request) {
  mainLogger("runRequestAsync start:", request["id"], request["source_path"]);
  let {id, source_language, target_language, source_path, source_str, transprog_path, transprog_str, postprocessing_js} = request;
  let runner = getIdleRequestRunner();
  if (runner === null) {
    alert("ERROR: No idle runner. Cannot run the benchmark.");
    return;
  }
  setTaskRunnerState(runner, RUNNER_STATE_RUNNING);
  let logger = runner.logger;
  
  logger("From", source_language, "to", target_language);

  
  let source_code = source_str;
  if (source_str === undefined || source_str === null) {
    logger("Reading source:", source_path);
    source_code = await anyfileAsync(source_path);
  } 
  let transprog_code = transprog_str;
  if (transprog_str === undefined || transprog_code === null) {
    logger("Reading transprog:", transprog_path);
    transprog_code = await anyfileAsync(transprog_path);
  }

  function _setLanguages(iframe, source_lang, target_lang) {
    let source_select = iframe.contentWindow.document.querySelector("#sourcelang-select");
    let target_select = iframe.contentWindow.document.querySelector("#targetlang-select");
    source_select.value = source_lang;
    target_select.value = target_lang;
  }

  function _setCodes(iframe, code_at_source, lang_at_source, code_at_prog) {
    let monaco_language_name_dict = {
      "js": "javascript",
      "py": "python",
      "java": "java",
      "cs": "csharp",
      "cpp": "cpp",
    };
    let source_lang_editor_obj = iframe.contentWindow.source_lang_editor_obj;
    let target_trans_editor_obj = iframe.contentWindow.target_trans_editor_obj;
    let monaco = iframe.contentWindow.monaco;
    let srcModel = source_lang_editor_obj.getModel(); 
    monaco.editor.setModelLanguage(srcModel, monaco_language_name_dict[lang_at_source]);
    source_lang_editor_obj.setValue(code_at_source);
    target_trans_editor_obj.setValue(code_at_prog);
    iframe.contentWindow.setChoices("STEP", []);
    iframe.contentWindow.setAutoBack(true);
  }

  async function _auto_translate(iframe) {
    let transChoicesHandler = iframe.contentWindow.translateHandlerChAsync;
    let translated_code = "ERROR_OR_EMPTY";
    let src_parse = null;
    while(true) {
      await transChoicesHandler();
      translated_code = iframe.contentWindow.getTranslatedCode();
      src_parse = iframe.contentWindow.getTranslateSrcParse();
      if (translated_code === "ERROR_OR_EMPTY") {
        logger("_auto_translate ERROR_OR_EMPTY. Waiting for user...");
        await iframe.contentWindow.waitForContinueClickAsync();
      } else break;
    }
    logger("get translated_code. length=", translated_code.length);
    return [translated_code, src_parse];
  }

  let iframe_trans = runner.iframe;

  logger("===== Start Trans =====");
  _setLanguages(iframe_trans, source_language, target_language);
  _setCodes(iframe_trans, source_code, source_language, transprog_code);
  let translated_code = null;
  let src_parse = null;
  let answering_id = id;
  while(true) {
    [translated_code, src_parse] = await _auto_translate(iframe_trans);
    let [src_code, parse_result, src_ast_dict] = src_parse;
    let post_code = translated_code;
    let post_error = null;
    if (postprocessing_js) {
      try {
        post_code = eval(postprocessing_js)(translated_code, src_code, parse_result["src_ast"], parse_result["src_ann"], src_ast_dict);
      } catch (e) {
        logger("[WARN] Post processing failed to execute: " + str(e));
        post_error = str(e);
      }
    }
    logger("Submit translated code...");
    let resp = await sendSockAsync({
      type: "request_result",
      answering_id: answering_id, 
      translated_code: post_code,
      post_error: post_error});
    let {is_ok, msg} = resp;
    answering_id = resp["id"];
    if(is_ok) {
      logger("OK confirmed from socket.");
      break;
    } 
    logger("REJECTED. msg:", msg);
    logger("Retry...");
    setTaskRunnerState(runner, RUNNER_STATE_PAUSED);
    iframe_trans.contentWindow.setForHumanAdjustment();
    await iframe_trans.contentWindow.waitForContinueClickAsync();
    setTaskRunnerState(runner, RUNNER_STATE_RUNNING);
  }
  setTaskRunnerState(runner, RUNNER_STATE_DONE);
  mainLogger("runBenchmarkHandler finish:", request["id"]);
}

function iframeTabHandler(tabname) {
  let iframe_id = "iframe-" + tabname;
  for (let elem of all_iframe_elems) {
    elem.style.display = "none";
  }
  for (let elem of all_iframe_elems) {
    if (elem.id === iframe_id) elem.style.display = "block";
  }
}