"use strict";
document.body.style.zoom = "90%";
window.DEBUG_LOGGING = false;

let config_select_elem = document.getElementById("config-select");
let benchfolder_input_elem = document.getElementById("benchfolder-input")
let sourcelang_select_elem = document.getElementById("sourcelang-select");
let targetlang_select_elem = document.getElementById("targetlang-select");
sourcelang_select_elem.disabled = true;
targetlang_select_elem.disabled = true;

let transprog_source_select_elem = document.getElementById("transprog-source-select");
let transprog_transtest_select_elem = document.getElementById("transprog-transtest-select");
let transprog_trans_select_elem = document.getElementById("transprog-trans-select");
let transprog_target_select_elem = document.getElementById("transprog-target-select");
transprog_source_select_elem.disabled = true;
transprog_transtest_select_elem.disabled = true;
transprog_trans_select_elem.disabled = true;
transprog_target_select_elem.disabled = true;

let outpath_input_elem = document.getElementById("outpath-input");
let goldtrans_select_elem = document.getElementById("goldtrans-select");
// let instrugold_check_elem = document.getElementById("instrugold-check");
let split3_check_elem = document.getElementById("split3-check");
let savestage2ret_check_elem = document.getElementById("savestage2ret-check");
let nodech_check_elem = document.getElementById("nodech-check");
outpath_input_elem.disabled = true;
goldtrans_select_elem.disabled = true;
// instrugold_check_elem.disabled = true;
split3_check_elem.disabled = true;
savestage2ret_check_elem.disabled = true;
nodech_check_elem.disabled = true;


let saverun_check_elem = document.getElementById("saverun-check");

let benchmark_list_elem = document.getElementById("benchmark-list");
let all_iframe_elems = Array.from(document.querySelectorAll(".full-iframe"));
let dashboard_iframe_elem = document.getElementById("iframe-dashboard");

let goldtrans_async = null;
let output_fdr = null;
let bench_dirname = null;

let mainLogger = null;
let statusBenchSetter = null;
let statusQueueSetter = null;
let statusServerSetter = null;
let addAllTasksButton = null;
let clearTasksButton = null;

let addall_benchmark_ids = [];
let task_queue = [];

function task_queue_label_update() {
  statusQueueSetter("Task Queue Status\nLength: " + task_queue.length + "\nAddAll: " + addall_benchmark_ids.length);
}
function task_queue_pushtail(benchmark_id) { 
  task_queue.push(benchmark_id); 
  task_queue_label_update(); 
}
function task_queue_pushtail_list(benchmark_id_list) { 
  for (let benchmark_id of benchmark_id_list) {
    task_queue.push(benchmark_id);
  } 
  task_queue_label_update(); 
}
function task_queue_pophead() { 
  if (task_queue.length > 0) {
    let head = task_queue.shift(); 
    task_queue_label_update(); 
    return head;
  } else {
    return null; 
  }
}
function task_queue_clear() { 
  task_queue.length = 0; 
  task_queue_label_update(); 
}

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

let task_runners = [
  {
    "label_elem": document.getElementById("iframe-tab-label0"),
    "benchmark_id": null,
    "runner_state": RUNNER_STATE_IDLE,
    "logger": null,
    "logger_cleaner": null,
    "log_string_list": [],
    "iframe_source": document.getElementById("iframe-source0"),
    "iframe_trans": document.getElementById("iframe-trans0"),
    "iframe_target": document.getElementById("iframe-target0"),
  },
  {
    "label_elem": document.getElementById("iframe-tab-label1"),
    "benchmark_id": null,
    "runner_state": RUNNER_STATE_IDLE,
    "logger": null,
    "logger_cleaner": null,
    "log_string_list": [],
    "iframe_source": document.getElementById("iframe-source1"),
    "iframe_trans": document.getElementById("iframe-trans1"),
    "iframe_target": document.getElementById("iframe-target1"),
  }
];

// ~~~ this is the function that pops an element from the task_queue
setTimeout((async function main1() {
  await echoAsync("index_bench_init_start");

  window._GITSTATUS_LOADING = parse_gitstatus((await getGitStatusAsync())["content"]);
  document.getElementById("echo-test").addEventListener("click", async () => await echoAsync("index_bench_init_start"));

  dashboard_iframe_elem.contentWindow.setOrUpdateLayout(dashboard_layout);

  mainLogger = dashboard_iframe_elem.contentWindow.createLogger("logMain");
  statusBenchSetter = dashboard_iframe_elem.contentWindow.createLabelSetter("statusBench");
  statusQueueSetter = dashboard_iframe_elem.contentWindow.createLabelSetter("statusQueue");
  statusServerSetter = dashboard_iframe_elem.contentWindow.createLabelSetter("statusServer");
  addAllTasksButton = dashboard_iframe_elem.contentWindow.getButton("buttonAddAllTasks");
  clearTasksButton = dashboard_iframe_elem.contentWindow.getButton("buttonClearTasks");

  addAllTasksButton.addEventListener("click", () => task_queue_pushtail_list(addall_benchmark_ids));
  clearTasksButton.addEventListener("click", task_queue_clear);

  mainLogger("Initializing...");
  task_runners[0].logger = composeFuncN(
    dashboard_iframe_elem.contentWindow.createLogger("logSub1"), 
    (msg) => task_runners[0].log_string_list.push(msg)
  );
  task_runners[1].logger = composeFuncN(
    dashboard_iframe_elem.contentWindow.createLogger("logSub2"), 
    (msg) => task_runners[1].log_string_list.push(msg)
  );
  task_runners[0].logger_cleaner = dashboard_iframe_elem.contentWindow.createLoggerCleaner("logSub1");
  task_runners[1].logger_cleaner = dashboard_iframe_elem.contentWindow.createLoggerCleaner("logSub2");

  mainLogger("calling initializeConfigAsync...");
  await initializeConfigAsync();

  mainLogger("calling polyFillRunnerIframes...");
  polyFillRunnerIframes(mainLogger);

  mainLogger("Initialized.");

  mainLogger("starting periodic task dispatcher...");
  let is_dispatcher_running = false;
  task_queue_label_update();
  let dispatch_count = 0;

  setInterval(async () => {
    if(!is_dispatcher_running) {
      is_dispatcher_running = true;
      // ~~~ the popped element (i.e. python program to translate)
      let bench_id_if_any = task_queue_pophead();
      if (bench_id_if_any !== null) {
        if (dispatch_count % 50 === 0) {
          mainLogger("Cleaning Mem Cache (dispatch_count=" + dispatch_count + ")...");
          let clearResult = await clearMemCacheAsync();
          mainLogger("Cleaning Mem Cache Result: " + JSON.stringify(clearResult));
        }
        dispatch_count += 1;
        await runBenchmarkHandler_ErrorAlert(bench_id_if_any);
      }
      is_dispatcher_running = false;
      
    }
  }, 500);

  mainLogger("started periodic task dispatcher.");
  await echoAsync("index_bench_init_end");
}), 3000);

function polyFillRunnerIframes(loggerFunc) {
  for (let runner of task_runners) {
    for (let iframe_key of ["iframe_source", "iframe_trans", "iframe_target"]) {
      let iframe_window = runner[iframe_key].contentWindow;
      iframe_window.alert = messageFunc1Gen([
        ["[UI_INFO]", window.alert],
        ["[UI_HANDLED]", combineVoidFuncN(runner.logger, (msg) => loggerFunc(msg + " (" + runner["benchmark_id"] + " " + iframe_key + ")"))],
        ["[UI_UNEXPECTED_ERROR]", combineVoidFuncN(runner.logger, (msg) => loggerFunc(msg + " (" + runner["benchmark_id"] + " " + iframe_key + ")"), window.alert)],
      ], window.alert);
    }
  }
}

async function initializeConfigAsync() {
  // list of translation rules
  let prog_dict = await getProgfilesAsync();
  
  // sets the values for dropdown UI element
  function set_option_general_elems(select_elem, vals) {
    select_elem.innerHTML = "";
    let option_fragment = document.createDocumentFragment();
    console.log("set_option_general_elems creating DOM elements for progs...");
    for(let val of vals) {
      let option_elem = document.createElement("option");
      option_elem.attributes["value"] = val;
      option_elem.innerText = val;
      option_fragment.appendChild(option_elem);
    }
    select_elem.appendChild(option_fragment);
    select_elem.value = vals[0];
  }

  // `configs` and `goldtrans_options` are defined in `index_bench_config.js`
  set_option_general_elems(config_select_elem, configs.map(x => x["name"]));
  set_option_general_elems(goldtrans_select_elem, Array.from(Object.keys(goldtrans_options)));

  function set_config_data(config_data) {
    goldtrans_async = goldtrans_options[config_data["goldtrans"]];
    for (let k in config_data["value"]) {
      document.getElementById(k).value = config_data["value"][k];
    }
    for (let k in config_data["checked"]) {
      document.getElementById(k).checked = config_data["checked"][k];
    }
  }

  async function _updateConfigAsync() {
    let config_option = config_select_elem.value;
    let sourceLang = sourcelang_select_elem.value;
    let targetLang = targetlang_select_elem.value;
    console.log("_updateConfigAsync: ", sourceLang, targetLang, config_option);

    let srckey = sourceLang + "_" + sourceLang;
    let tarkey = targetLang + "_" + targetLang;
    let pairkey = sourceLang + "_" + targetLang;

    function update_select_elems(select_elem, progkey, default_val) {
      if (progkey in prog_dict["dirs"]) {
        let progs = prog_dict["dirs"][progkey]["files"];
        progs.sort();
        select_elem.innerHTML = "";
        let option_fragment = document.createDocumentFragment();
        console.log("_updateTestcasesSelect creating DOM elements for progs...");
        let default_exists = false;
        for(let prog of progs) {
          if (!prog.endsWith(".snart")) continue;
          let prog_prefix = prog.replace(".snart", "");
          let option_elem = document.createElement("option");
          option_elem.attributes["value"] = prog_prefix;
          if (prog_prefix === default_val) default_exists = true;
          option_elem.innerText = prog_prefix;
          option_fragment.appendChild(option_elem);
        }
        select_elem.appendChild(option_fragment);
        if (default_exists) select_elem.value = default_val;
      } else {
        select_elem.innerHTML = "<option>INVAlID PROGKEY</option>";
      }
    }

    // update the UI elements
    update_select_elems(transprog_source_select_elem, srckey, "instru");
    update_select_elems(transprog_trans_select_elem, pairkey, "gfg");
    update_select_elems(transprog_transtest_select_elem, pairkey, "gfgtest");
    update_select_elems(transprog_target_select_elem, tarkey, "instrudel");
    
    // set config data after loading progs
    let config_data = config_dict[config_option];
    set_config_data(config_data);
    output_fdr = outpath_input_elem.value;
    bench_dirname = benchfolder_input_elem.value;

    // get all the files in the benchmark directory
    let file_dict = await getGeneralBenchFilesAsync(bench_dirname);
    if(window.DEBUG_LOGGING) console.log("# _updateConfigAsync " + bench_dirname + " file_dict:", file_dict);


    let existing_file_list = await listOutputDirFilesAsync(output_fdr + "/" + pairkey);
    let existing_file_list_dict = {};
    if (existing_file_list) for (let file of existing_file_list) existing_file_list_dict[file] = true;
    let existing_logfile_list = await listOutputDirFilesAsync(output_fdr + "/" + pairkey + "_log");
    let existing_logfile_list_dict = {};
    let log_count = 0;
    if (existing_logfile_list) {
      for (let file of existing_logfile_list) {
        if (!(file in existing_file_list_dict)) log_count += 1;
        existing_logfile_list_dict[file] = true;
      }
    }
    if(window.DEBUG_LOGGING) console.log("_updateConfigAsync existing_file_list:", existing_file_list);
    if(window.DEBUG_LOGGING) console.log("_updateConfigAsync existing_logfile_list:", existing_logfile_list);
    
    // TODO: get stafiles according to source language
    let stafiles = sourceLang in file_dict["dirs"] ? file_dict["dirs"][sourceLang]["files"] : [];
    stafiles = stafiles.filter(x => x !== ".gitignore");
    stafiles.sort();
    if(window.DEBUG_LOGGING) console.log("_updateConfigAsync stafiles: ", stafiles);
    let done_ratio = stafiles.length >= 0 && existing_file_list ? Math.round((existing_file_list.length / stafiles.length) * 100) + "%" : "NA";
    statusBenchSetter("Total: " + stafiles.length + "\nDone: " + (existing_file_list? existing_file_list.length : "NA") + " (" + done_ratio + ")"+ "\nLog: " + log_count)
    
    let havent_run_files = [];    
    benchmark_list_elem.innerHTML = "";
    // use fragment to speed up
    let list_fragment = document.createDocumentFragment();
    console.log("_updateConfigAsync creating DOM elements...");
    for(let filename of stafiles) {
      let expected_existing_filename = filename.replace("." + sourceLang, "") + "." + targetLang;
      let is_result_existing = existing_file_list && expected_existing_filename in existing_file_list_dict;
      let expected_existing_logfilename = filename.replace("." + sourceLang, "") + ".log";
      let is_log_existing = existing_logfile_list && expected_existing_logfilename in existing_logfile_list_dict;
      if (!(is_result_existing || is_log_existing)) {
        if(filename.startsWith("GFG")) havent_run_files.push(filename);
        if(filename.startsWith("L")) havent_run_files.push(filename);
        if(filename.startsWith("AL")) havent_run_files.push(filename);
      }
      let additional_class = is_result_existing ? "benchfile-result-exists" : (is_log_existing ? "benchfile-log-exists": "");
      let codepath0 = "duoglot/tests/" + bench_dirname + "/" + sourceLang + "/" + filename;
      let codepath1 = "duoglot/tests/_output_/" + output_fdr + "/" + pairkey + "/" + expected_existing_filename;
      let codepath2 = "duoglot/tests/_output_/" +output_fdr + "/" + pairkey + "_log/" + expected_existing_logfilename;
      let newpageurl = create_url(null, "../_common/index_viewer.html", {
        codepath0: codepath0,
        codepath1: codepath1, 
        codepath2: codepath2, 
        autoload: true});
      let view_code_btn = true ? `<a class="sidelist-item-view-link" href="${newpageurl}" target="_blank">View</a>` : "";
      let item_elem = document.createElement("div");
      item_elem.attributes["key"] = filename;
      item_elem.attributes["x_fail"] = (!is_result_existing) && is_log_existing;
      item_elem.attributes["x_codepath0"] = codepath0;
      item_elem.attributes["x_codepath1"] = codepath1;
      item_elem.attributes["x_codepath2"] = codepath2;
      item_elem.innerHTML = `
        <div class="sidelist-item ${additional_class}">
          <button class="sidelist-item-run-btn" onclick="task_queue_pushtail('${filename}')">Run</button>
          ${view_code_btn}
          <span>${filename}</span>
        </div>
      `;
      item_elem.addEventListener("mouseenter", mouse_enter_bench_item);
      list_fragment.appendChild(item_elem);
    }
    benchmark_list_elem.appendChild(list_fragment);
    
    console.log("_updateConfigAsync havent_run_files:", havent_run_files);
    addall_benchmark_ids = havent_run_files;
    task_queue_label_update();
    console.log("_updateConfigAsync done.");
  }
  await _updateConfigAsync();
  // sourcelang_select_elem.onchange = _updateConfigAsync;
  // targetlang_select_elem.onchange = _updateConfigAsync;
  config_select_elem.onchange = _updateConfigAsync;

}

function getIdleTaskRunner() {
  function _find_idle_runner() {
    for(let runner of task_runners) {
      if (runner.runner_state == RUNNER_STATE_IDLE) {
        runner.logger_cleaner();
        return runner;
      }
    }
    return null;
  }

  let idle_runner = null;

  idle_runner = _find_idle_runner();
  if (idle_runner !== null) return idle_runner;

  //if no, reclaim done runners.
  for(let runner of task_runners) {
    if (runner.runner_state == RUNNER_STATE_DONE) {
      runner.benchmark_id = null;
      runner.runner_state = RUNNER_STATE_IDLE;
      runner.log_string_list.length = 0;
    }
  }
  
  idle_runner = _find_idle_runner();
  if (idle_runner !== null) return idle_runner;

  //if still no, reclaim error runners.
  for(let runner of task_runners) {
    if (runner.runner_state == RUNNER_STATE_ERROR) {
      runner.benchmark_id = null;
      runner.runner_state = RUNNER_STATE_IDLE;
      runner.log_string_list.length = 0;
    }
  }
  
  idle_runner = _find_idle_runner();
  if (idle_runner !== null) return idle_runner;
  
  return null;
}

async function mouse_enter_bench_item(e) {
  let filename = e.target.attributes["key"];
  let is_reason_checked = e.target.attributes["x_reason_checked"];
  let is_fail = e.target.attributes["x_fail"];
  let codepath0 = e.target.attributes["x_codepath0"];
  let codepath1 = e.target.attributes["x_codepath1"];
  let codepath2 = e.target.attributes["x_codepath2"];
  if (!is_reason_checked) {
    console.log("# mouse_enter_bench_item checking:", filename, is_fail);
    e.target.attributes["x_reason_checked"] = true;
    if (is_fail) {
      let src_code = await tryReadFileAsync(codepath0);
      let log_text = await tryReadFileAsync(codepath2);
      let fail_reason = fail_reason_checker(src_code, log_text);
      let fail_reason_p = document.createElement("span");
      fail_reason_p.className = "fail-reason-span";
      fail_reason_p.innerText = fail_reason;
      fail_reason_p.addEventListener("click", () => {
        let copytext = "- `" + filename + "` " + fail_reason;
        navigator.clipboard.writeText(copytext);
        toast_info("Copy to clipboard:\n" + copytext);
      })
      e.target.getElementsByClassName("sidelist-item")[0].appendChild(fail_reason_p);
    }
  }

}

function fail_reason_checker(src, log_text) {
  if (src.indexOf("import deque") >= 0) return "need deque";
  if (src.indexOf("import defaultdict") >= 0) return "need defaultdict";
  if (src.indexOf("Counter(") >= 0) return "need Counter";
  if (src.indexOf("heapq") >= 0) return "need heapq";
  return "UN"; 
}


function setTaskRunnerState(runner, state) {
  runner.runner_state = state;
  runner.label_elem.innerText = RUNNER_LABEL_STATE[state];
}

function setTaskRunnerBenchmarkId(runner, benchmark_id) {
  runner.benchmark_id = benchmark_id;
}

window._rule_parse_cache = {};
async function queryRuleIdxsAsync (rule_text, query) {
  let [rules, dbg_info, error_msg] = [null, null, null];
  if (!(rule_text in _rule_parse_cache)) {
    [rules, dbg_info, error_msg] = await parseRulesAsync(rule_text);
    window._rule_parse_cache[rule_text] = [rules, dbg_info, error_msg];
  } else {
    [rules, dbg_info, error_msg] = window._rule_parse_cache[rule_text];
  }
  return query_rule_idxs_from_rules(rules, query);
}


let MANUAL_FIX_ENABLED = false;

// run runBenchmarkHandler()
// if exception is raised, run errorAnyAlert()
let runBenchmarkHandler_ErrorAlert = (benchmarkname) => errorWrapperFuncArgsAsync(runBenchmarkHandler, [benchmarkname], errorAnyAlert);

// ~~~ this is the function to which a program is passed for translation (e.g. python program to be translated to javascript)
async function runBenchmarkHandler(benchmarkname) {
  let saverun = saverun_check_elem.checked;
  mainLogger("runBenchmarkHandler start:", benchmarkname, " saverun:", saverun);

  let outputpath = output_fdr + "/py_js/" + benchmarkname.replace(".py", ".js");
  let outputlogpath = output_fdr + "/py_js_log/" + benchmarkname.replace(".py", ".log");
  let existingcode = await tryReadOutputFileAsync(outputpath);
  if (existingcode !== null && existingcode !== undefined) {
    mainLogger("[NOTICE] runBenchmarkHandler result exists. ", benchmarkname, existingcode.length);
  }

  // runner is some sort of a dictionary (search for: `let task_runners`)
  let runner = getIdleTaskRunner();
  if (runner === null) {
    alert("ERROR: No idle runner. Cannot run the benchmark.");
    return;
  }
  setTaskRunnerState(runner, RUNNER_STATE_RUNNING);
  setTaskRunnerBenchmarkId(runner, benchmarkname);

  let logger = runner.logger;                                            // some function
  let benchDirname = benchfolder_input_elem.value;                       // 'standalone'
  let sourcelang = sourcelang_select_elem.value;                         // 'py'
  let targetlang = targetlang_select_elem.value;                         // 'js'
  let sourceProgPrefix = transprog_source_select_elem.value;             // 'instru', prefix for translation rules
  let transProgPrefix = transprog_trans_select_elem.value;               // 'gfg'
  let transtestProgPrefix = transprog_transtest_select_elem.value;       // 'gfgtest'
  let targetProgPrefix = transprog_target_select_elem.value;             // 'instrudel'
  let srckey = sourcelang + "_" + sourcelang;                            
  let tarkey = targetlang + "_" + targetlang;                            
  let pairkey = sourcelang + "_" + targetlang;                           
  let staFilepath = "duoglot/tests/" + benchDirname + "/" + sourcelang + "/" + benchmarkname;                                                          // 'duoglot/tests/standalone/py/GFG_ADD_1_TO_A_GIVEN_NUMBER.py'
  let sourceProgPath = sourceProgPrefix === "" ? null : "duoglot/tests/trans_programs/" + srckey + "/" + sourceProgPrefix + ".snart";                  // 'duoglot/tests/trans_programs/py_py/instru.snart'
  let transProgPath = transProgPrefix === "" ? null : "duoglot/tests/trans_programs/" + pairkey + "/" + transProgPrefix + ".snart";                    // 'duoglot/tests/trans_programs/py_js/gfg.snart'
  let transProgConfigPath = transProgPrefix === "" ? null : "duoglot/tests/trans_programs/" + pairkey + "/" + transProgPrefix + ".config.json";        // 'duoglot/tests/trans_programs/py_js/gfg.config.json'
  let transtestProgPath = transtestProgPrefix === "" ? null : "duoglot/tests/trans_programs/" + pairkey + "/" + transtestProgPrefix + ".snart";        // 'duoglot/tests/trans_programs/py_js/gfgtest.snart'
  let targetProgPath = targetProgPrefix === "" ? null : "duoglot/tests/trans_programs/" + tarkey + "/" + targetProgPrefix + ".snart";                  // 'duoglot/tests/trans_programs/js_js/instrudel.snart'
  
  let files_git_status = parse_gitstatus((await getGitStatusAsync())["content"]);

  // TODO why do we need GITSTATUS?
  logger("GITSTATUS_LOADING: ", JSON.stringify(window._GITSTATUS_LOADING));
  logger("GITSTATUS CURRENT: ", JSON.stringify(files_git_status));
  if ((!window._GITSTATUS_LOADING["is_clean"]) || (!files_git_status["is_clean"])) {
    console.warn("Working tree not clean.", window._GITSTATUS_LOADING, files_git_status);
  }
  if ((window._GITSTATUS_LOADING["commit_hash"] !== files_git_status["commit_hash"])) {
    throw Error("NO_WRITE_LOG Error commit_hash mismatch");
  }

  logger("From", sourcelang, "to", targetlang);
  logger("Rules:", sourceProgPrefix, transProgPrefix, targetProgPrefix);

  // 'duoglot/tests/standalone/py/GFG_ADD_1_TO_A_GIVEN_NUMBER.py'
  logger("Reading source:", staFilepath);
  let source_code = await anyfileAsync(staFilepath);

  // 'duoglot/tests/trans_programs/py_py/instru.snart'
  logger("Reading source prog:", sourceProgPath);
  let source_prog_code = sourceProgPath === null ? null : await anyfileAsync(sourceProgPath);

  // 'duoglot/tests/trans_programs/py_js/gfg.snart'
  logger("Reading trans(main) prog:", transProgPath);
  let trans_prog_code = transProgPath === null ? null : await anyfileAsync(transProgPath);

  let trans_prog_config_info = {
    "skip_on_line_error": {}
  };

  // reads some config file for translation rules. TODO what is it for?
  // 'duoglot/tests/trans_programs/py_js/gfg.config.json'
  // default is `{"skip_on_line_error":{}}`
  if (trans_prog_code !== null) {
    logger("Reading trans(main) prog_config:", transProgConfigPath);
    let trans_prog_config = null;
    try {
      let trans_prog_config_code = transProgConfigPath === null ? null : await anyfileAsync(transProgConfigPath);
      trans_prog_config = trans_prog_config_code === null ? null : JSON.parse(trans_prog_config_code);
    } catch (e) {
      logger("[INFO] No experimental config found. Use default.");
    }

    if (trans_prog_config !== null) {
      let groups_info = trans_prog_config["groups"];
      if ("skip_on_line_error" in groups_info) {
        for (let key in groups_info["skip_on_line_error"]) {
          let idxs = await queryRuleIdxsAsync(trans_prog_code, key);
          if (idxs.length !== 1) logger("WARNING: rule query result unexpected: " + key + " result:" + idxs);
          for (let idx of idxs) {
            trans_prog_config_info["skip_on_line_error"][idx] = groups_info["skip_on_line_error"][key];
          }
        }
      }
    }
  }

  console.log("trans_prog_config_info:", trans_prog_config_info);

  // 'duoglot/tests/trans_programs/py_js/gfgtest.snart'
  logger("Reading trans(test) prog:", transtestProgPath);
  let transtest_prog_code = transtestProgPath === null ? null : await anyfileAsync(transtestProgPath);

  // 'duoglot/tests/trans_programs/js_js/instrudel.snart'
  logger("Reading target prog:", targetProgPath);
  let target_prog_code = targetProgPath === null ? null : await anyfileAsync(targetProgPath);

  // set `from` and `to` languages to iframe at http://127.0.0.1:8000/frontend/duoglot/index_t.html
  function _setLanguages(iframe, source_lang, target_lang) {
    let source_select = iframe.contentWindow.document.querySelector("#sourcelang-select");
    let target_select = iframe.contentWindow.document.querySelector("#targetlang-select");
    source_select.value = source_lang;
    target_select.value = target_lang;
  }

  // set codes of <source program> and <translation rules> to iframe
  function _setCodes(iframe, code_at_source, lang_at_source, code_at_prog, note_info) {
    let monaco_language_name_dict = {
      "js": "javascript",
      "py": "python",
      "java": "java",
      "cs": "csharp",
      "cpp": "cpp",
    };

    let source_lang_editor_obj = iframe.contentWindow.source_lang_editor_obj;     // source program editor
    let target_trans_editor_obj = iframe.contentWindow.target_trans_editor_obj;   // rules editor (below source program editor)
    let monaco = iframe.contentWindow.monaco;
    let srcModel = source_lang_editor_obj.getModel(); 

    monaco.editor.setModelLanguage(srcModel, monaco_language_name_dict[lang_at_source]);
    source_lang_editor_obj.setValue(code_at_source);
    target_trans_editor_obj.setValue(code_at_prog);

    if (nodech_check_elem.checked) {
      iframe.contentWindow.setChoices("ASTNODE", []);
    } else {
      iframe.contentWindow.setChoices("STEP", []);
    }

    iframe.contentWindow.setAutoBack(true);
    iframe.contentWindow.setHeadlineNote(note_info);
  }

  // runs translate for a given iframe
  async function _auto_translate(iframe) {
    let transChoicesHandler = iframe.contentWindow.translateHandlerChAsync;
    let translated_code = "ERROR_OR_EMPTY";
    let translate_src_parse = null;
    while(true) {
      await transChoicesHandler();
      translated_code = iframe.contentWindow.getTranslatedCode();         // source code of translated program (target program)
      translate_src_parse = iframe.contentWindow.getTranslateSrcParse();  // [source_code, src_parse_result, source_AST_dict]
      if (translated_code === "ERROR_OR_EMPTY") {
        if (MANUAL_FIX_ENABLED) {
          logger("_auto_translate ERROR_OR_EMPTY. Waiting for user...");
          await iframe.contentWindow.waitForContinueClickAsync();
        } else {
          throw Error("FAILED to do _auto_translate (ERROR_OR_EMPTY) and manual fix is disabled.");
        }
      } else break;
    }
    logger("get translated_code. length=", translated_code.length);
    return [translated_code, translate_src_parse];
  }

  let iframe_source = runner.iframe_source;
  let iframe_trans = runner.iframe_trans;
  let iframe_target = runner.iframe_target;

  // main part
  try {
    logger("===== PreCheck =====");
    let is_long_source = false;
    let source_prog_postprocessing_func = null;
    let transtest_prog_postprocessing_func = null;
    let target_prog_postprocessing_func = null;

    // check for length of source program
    if (source_code.length > 5000) {
      if (source_prog_code && transtest_prog_code && target_prog_code) {
        //throw Error("ERROR SKIPPING: source_code too long. length=" + source_code.length);
        logger("WARNING: very long source_code. length=" + source_code.length);
        is_long_source = true;

        let param_hack_flag = '"disabled" "paramhack"';
        if (source_prog_code.indexOf(param_hack_flag) >= 0) source_prog_code = source_prog_code.replace(param_hack_flag, "");
        else throw Error("Error source_prog_code doesn't support super long files");
        if (transtest_prog_code.indexOf(param_hack_flag) >= 0) transtest_prog_code = transtest_prog_code.replace(param_hack_flag, "");
        else throw Error("Error transtest_prog_code doesn't support super long files");
        if (target_prog_code.indexOf(param_hack_flag) >= 0) target_prog_code = target_prog_code.replace(param_hack_flag, "");
        else throw Error("Error target_prog_code doesn't support super long files");

        source_prog_postprocessing_func = window._postproc_source_copy_func;
        transtest_prog_postprocessing_func = window._postproc_py_array_to_js_array_func;
        target_prog_postprocessing_func = window._postproc_source_copy_func;
      } else {
        logger("WARNING: very long source_code but proceed as normal. length=" + source_code.length);
      }
    }

    let instrumented_code = null;
    let testfunc_code = null;
    let goldfunc_code = null;
    let testcall_code = null;

    // ~~~ STAGE 1
    // source_prog_code => 'duoglot/tests/trans_programs/py_py/instru.snart'
    if (source_prog_code !== null) {
      logger("===== Process stage 1 =====");

      _setLanguages(iframe_source, sourcelang, sourcelang);
      _setCodes(iframe_source, source_code, sourcelang, source_prog_code);

      // `instrumented_code_raw` contains `mylog(MYLOG_COUNTER, param)` every now-and-then (for instrumentation)
      let [instrumented_code_raw, source_code_src_parse] = await _auto_translate(iframe_source);

      if (is_long_source) {
        logger("Stage 1 Postprocessing...");
        let [src_code, parse_result, src_ast_dict] = source_code_src_parse;
        try {
          instrumented_code_raw = source_prog_postprocessing_func(instrumented_code_raw, src_code, parse_result["src_ast"], parse_result["src_ann"], src_ast_dict);
        } catch (e) {
          logger("[WARN] Post processing failed to execute: " + str(e));
          throw Error("Postprocessing failed for instrumented source code");
        }
      }

      let instrumented_seps = instrumented_code_raw.split("MYLOG_COUNTER");
      let interleaved_list = [];
      for (let i = 0; i < instrumented_seps.length; i++) {
        interleaved_list.push(instrumented_seps[i]);
        if (i < instrumented_seps.length - 1) interleaved_list.push(String(i));
      }

      // `raw_instrumented_code` is `instrumented_code_raw` with each MYLOG_COUNTER substituted with ints in range(0,)
      let raw_instrumented_code = interleaved_list.join("");

      let instru_code_split = raw_instrumented_code.split('"-----------------"');
      if (instru_code_split.length !== 3) {
        throw Error("ERROR: Instrumented Code should be 3 parts. Terminate.");
      }

      let [raw_testfunc_code, raw_goldfunc_code, raw_testcall_code] = instru_code_split;
      testcall_code = raw_testcall_code;  // test()

      // do they rely on the structure of test function?
      testfunc_code = raw_testfunc_code.replace("mylog(2", "myexactlog(2");
      testfunc_code = testfunc_code.replace("mylog(1", "myexactlog(1");
      testfunc_code = testfunc_code.replace("mylog(3", "myexactlog(3");
      
      //FUTURE TODO: remove mylog instrumentation in goldfunc_code
      goldfunc_code = raw_goldfunc_code.split("\n").filter(x => !(x.trim().startsWith("mylog"))).join("\n");
      logger("INFO: removed 'mylog' instrumentation in goldfunc (if any).");
      //goldfunc_code = raw_goldfunc_code;

      instrumented_code = [testfunc_code, goldfunc_code, testcall_code].join('"-----------------"');
    } else {
      logger("===== Process stage 1 skipped =====");
      _setLanguages(iframe_source, sourcelang, sourcelang);
      _setCodes(iframe_source, "STAGE1_SKIPPED", sourcelang, "; STAGE1_SKIPPED");
      instrumented_code = source_code;

      if (split3_check_elem.checked) {
        let instru_code_split = source_code.split('"-----------------"');
        if (instru_code_split.length !== 3) {
          throw Error("ERROR: Instrumented Code should be 3 parts. Terminate.");
        } else {
          testfunc_code = instru_code_split[0];
          goldfunc_code = instru_code_split[1];
          testcall_code = instru_code_split[2];
        }
      }
      else {
        testfunc_code = null;
        goldfunc_code = source_code;
        testcall_code = null;
      }
    }
    
    // ~~~ STAGE 2
    logger("===== Process stage 2 =====");
    _setLanguages(iframe_trans, sourcelang, targetlang);

    let [testfunc_trans_code, testfunc_src_parse] = [null, null];
    // `split3_check_elem` is a checkbox in UI `Split3`
    if (split3_check_elem.checked) {
      logger("Translating test func...");

      // `transtest_prog_code` is 'duoglot/tests/trans_programs/py_js/gfgtest.snart'
      // `testfunc_code` is instrumented test function code
      _setCodes(iframe_trans, testfunc_code, sourcelang, transtest_prog_code);

      // translate instrumented test function code from source to target language (i.e. py -> js)
      [testfunc_trans_code, testfunc_src_parse] = await _auto_translate(iframe_trans);

      if (is_long_source) {
        logger("Stage 2 (test func) Postprocessing...");
        let [src_code, parse_result, src_ast_dict] = testfunc_src_parse;
        try {
          testfunc_trans_code = transtest_prog_postprocessing_func(testfunc_trans_code, src_code, parse_result["src_ast"], parse_result["src_ann"], src_ast_dict);
        } catch (e) {
          logger("[WARN] Post processing failed to execute: " + str(e));
          throw Error("Postprocessing failed for translated test func");
        }
      }
      if (window._DEBUG_STOP_AFTER_TRANS_TEST) {
        throw Error("inspect translation of test.");
      }
    }
    
    logger("Translating f_gold func...");
    function testcode_wrapper(goldfunc_trans_code) {
      if (split3_check_elem.checked) {
        let combined_testcode = testfunc_trans_code + '\n"-----------------"\n' + goldfunc_trans_code + '\n"-----------------"\n' + testcall_code;
        return combined_testcode;
      } else {
        return goldfunc_trans_code;
      }
    }

    async function test_runner(translated_code, is_dryrun = false) {
      let test_runner_before_t = performance.now();
      logger("Run standalone code pair...");
      let {target_code, target_log, target_error, error_msg, timespan_s, timespan_t} = await standalonePairFileRunAsync(instrumented_code, translated_code, sourcelang, targetlang, is_dryrun);
      if(window.DEBUG_LOGGING) console.log("STAGE2", target_log, target_error);
      if (error_msg !== undefined && error_msg !== null) {
        throw Error("Backend failed to execute test command: " + error_msg)
      } else {
        if(target_error === null) {
          if (target_log !== null && target_log !== undefined) {
            let target_log_str = JSON.stringify(target_log);
            logger("Target Log:", target_log_str)
            logger("SUCCESS (Check passed).");
          } else {
            logger("POSSIBLY DRY_RUN (no log)");
          }

          let test_runner_after_t = performance.now();
          logger("TIME (test_runner): " + String((test_runner_after_t - test_runner_before_t) / 1000));
          return [true, target_code, target_log, target_error, timespan_s, timespan_t];
        } 
        logger("FAILED. target_error:", JSON.stringify(target_error));

        let test_runner_after_t = performance.now();
        logger("TIME (test_runner): " + String((test_runner_after_t - test_runner_before_t) / 1000));
        return [false, target_code, target_log, target_error, timespan_s, timespan_t];
      }
    }

    let transgold_before_t = performance.now();
    let translated_code = await goldtrans_async(logger, testcode_wrapper, test_runner, benchmarkname, goldfunc_code, sourcelang, targetlang, trans_prog_code, trans_prog_config_info, iframe_trans, _setCodes);
    let transgold_after_t = performance.now();
    logger("TIME (goldtrans_async): " + String((transgold_after_t - transgold_before_t) / 1000));

    if (!(savestage2ret_check_elem.checked)) {
      let deinstrumented_code = null;
      if (target_prog_code !== null) {
        logger("===== Process stage 3 =====");
        _setLanguages(iframe_target, targetlang, targetlang);
        _setCodes(iframe_target, translated_code, targetlang, target_prog_code);
        let translated_src_parse;
        [deinstrumented_code, translated_src_parse] = await _auto_translate(iframe_target);
        if (is_long_source) {
          logger("Stage 3 Postprocessing...");
          let [src_code, parse_result, src_ast_dict] = translated_src_parse;
          try {
            deinstrumented_code = target_prog_postprocessing_func(deinstrumented_code, src_code, parse_result["src_ast"], parse_result["src_ann"], src_ast_dict);
          } catch (e) {
            logger("[WARN] Post processing failed to execute: " + str(e));
            throw Error("Postprocessing failed for deinstrumented code");
          }
        }
      } else {
        logger("===== Process stage 3 skipped =====");
        deinstrumented_code = translated_code;
      }
      
      if (saverun) {
        logger("Write to file: " + outputpath, JSON.stringify(await writeOutputFileAsync(outputpath, deinstrumented_code)));
      } else {
        logger("Skipping Write to file (saverun = " + saverun + ")");
      }
    } else {
      logger("===== Stage 2 SaveRet =====");
      if (saverun) {
        logger("SaveRet Write to file: " + outputpath, JSON.stringify(await writeOutputFileAsync(outputpath, translated_code)));
      } else {
        logger("SaveRet Skipping Write to file (saverun = " + saverun + ")");
      }
    }
    logger("===== Done =====");

    setTaskRunnerState(runner, RUNNER_STATE_DONE);
    if (saverun) {
      let write_resp = JSON.stringify(await writeOutputFileAsync(outputlogpath, runner.log_string_list.join("\n")));
      mainLogger("runBenchmarkHandler write log (done): " + outputlogpath + " " + write_resp);
    } else {
      mainLogger("runBenchmarkHandler skipping logging (done, saverun = " + saverun + ").");
    }
    mainLogger("runBenchmarkHandler DONE:", benchmarkname);
  }
  catch (err) {
    logger("!FAILED! ********************");
    logger("!FAILED! error: " + err);
    logger("!FAILED! ERROR_STACK: " + err.stack);
    logger("===== FAILED =====");
    setTaskRunnerState(runner, RUNNER_STATE_ERROR);
    if (saverun) {
      if (!String(err).startsWith("NO_WRITE_LOG")) {
        let write_resp = JSON.stringify(await writeOutputFileAsync(outputlogpath, runner.log_string_list.join("\n")));
        mainLogger("runBenchmarkHandler write log (error): " + outputlogpath + " " + write_resp);
      } else {
        mainLogger("runBenchmarkHandler skipping logging (NO_WRITE_LOG).");
      }
    } else {
      mainLogger("runBenchmarkHandler skipping logging (error).");
    }
    mainLogger("runBenchmarkHandler ERROR:", benchmarkname);
  }
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

function toast_info(infostr) {
  Toastify({
    text: infostr,
    gravity: "bottom",
    position: "center",
    className: "toast-info",
    duration: 3000
  }).showToast();
}