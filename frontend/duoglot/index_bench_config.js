////////////////////////////// benchmark setting config //////////////////////////////

let configs = [
  // {
  //   "name": "leetcode-dg-sch",
  //   "value": {
  //     "benchfolder-input": "staleetcode",
  //     "transprog-source-select": "",
  //     "transprog-transtest-select": "leettest",
  //     "transprog-trans-select": "leet",
  //     "transprog-target-select": "",
  //     "outpath-input": "staleetcode"
  //   },
  //   "checked": {
  //     "split3-check": true,
  //     "savestage2ret-check": false,
  //     "nodech-check": false,
  //   },
  //   "goldtrans": "rules_default"
  // },
  {
    "name": "ctci-dg-nch",
    "value": {
      "benchfolder-input": "stactci",
      "transprog-source-select": "",
      "transprog-transtest-select": "",
      "transprog-trans-select": "ctci",
      "transprog-target-select": "",
      "outpath-input": "stactci"
    },
    "checked": {
      "split3-check": false,
      "savestage2ret-check": false,
      "nodech-check": true,
    },
    "goldtrans": "rules_default"
  },
  {
    "name": "ctci-exportscript",
    "value": {
      "benchfolder-input": "stactci",
      "transprog-source-select": "",
      "transprog-transtest-select": "",
      "transprog-trans-select": "",
      "transprog-target-select": "",
      "outpath-input": "stactci-exportscript"
    },
    "checked": {
      "split3-check": false,
      "savestage2ret-check": true,
      "nodech-check": false,
    },
    "goldtrans": "exportscript-ph"
  },
  {
    "name": "leetcode-dg-nch",
    "value": {
      "benchfolder-input": "staleetcode",
      "transprog-source-select": "",
      "transprog-transtest-select": "leettest",
      "transprog-trans-select": "leet",
      "transprog-target-select": "",
      "outpath-input": "staleetcode"
    },
    "checked": {
      "split3-check": true,
      "savestage2ret-check": false,
      "nodech-check": true,
    },
    "goldtrans": "rules_default"
  },
  {
    "name": "leetcode-exportscript",
    "value": {
      "benchfolder-input": "staleetcode",
      "transprog-source-select": "",
      "transprog-transtest-select": "leettest",
      "transprog-trans-select": "",
      "transprog-target-select": "",
      "outpath-input": "staleetcode-exportscript"
    },
    "checked": {
      "split3-check": true,
      "savestage2ret-check": true,
      "nodech-check": true,
    },
    "goldtrans": "exportscript-ph"
  },
  // {
  //   "name": "gfg-dg-errtab",
  //   "value": {
  //     "benchfolder-input": "standalone",
  //     "transprog-source-select": "instru",
  //     "transprog-transtest-select": "gfgtest",
  //     "transprog-trans-select": "gfg",
  //     "transprog-target-select": "instrudel",
  //     "outpath-input": "standalone-errtab"
  //   },
  //   "checked": {
  //     "split3-check": true,
  //     "savestage2ret-check": false,
  //     "nodech-check": true,
  //   },
  //   "goldtrans": "rules_errtab"
  // },
  {
    "name": "gfg-dg-basic",
    "value": {
      "benchfolder-input": "standalone",
      "transprog-source-select": "instru",
      "transprog-transtest-select": "gfgtest",
      "transprog-trans-select": "gfg",
      "transprog-target-select": "instrudel",
      "outpath-input": "standalone-basic"
    },
    "checked": {
      "split3-check": true,
      "savestage2ret-check": false,
      "nodech-check": true,
    },
    "goldtrans": "rules_default"
  },
  {
    "name": "gfg-exportscript",
    "value": {
      "benchfolder-input": "standalone",
      "transprog-source-select": "instru",
      "transprog-transtest-select": "gfgtest",
      "transprog-trans-select": "",
      "transprog-target-select": "instrudel",
      "outpath-input": "standalone-exportscript"
    },
    "checked": {
      "split3-check": true,
      "savestage2ret-check": true,
      "nodech-check": false,
    },
    "goldtrans": "exportscript-ph"
  },
  // {
  //   "name": "gfg-exportextscript",
  //   "value": {
  //     "benchfolder-input": "standalone_ext",
  //     "transprog-source-select": "instru",
  //     "transprog-transtest-select": "gfgtest",
  //     "transprog-trans-select": "",
  //     "transprog-target-select": "instrudel",
  //     "outpath-input": "standalone_ext-exportextscript"
  //   },
  //   "checked": {
  //     "split3-check": true,
  //     "savestage2ret-check": true,
  //     "nodech-check": false,
  //   },
  //   "goldtrans": "exportscript-ph"
  // }
]

let config_dict = {}
for (let config of configs) config_dict[config["name"]] = config;

let goldtrans_options = {
  "rules_errtab": gen_goldtrans_rules_noinstru_async(true),
  "rules_default": gen_goldtrans_rules_noinstru_async(false),
  // "codex-naive": null,
  // "codex-loop": null,
  // "trcoder-java": null,
  // "trpiler-py2js": trpiler_py2js_async,
  "exportscript-ph": exportscript_async,
}

async function exportscript_async(logger, testcode_wrapper, test_runner, benchmarkname, goldfunc_code, sourcelang, targetlang, trans_prog_code, trans_prog_config_info, iframe_trans, _setCodes) {
  let placeholder = "\n//TRANSlATED_PLACEHOLDER_NO_OUTPUT_EXPECTED\n";
  let translated_code = testcode_wrapper(placeholder);
  let [is_success, target_runcode, target_log, target_error] = await test_runner(translated_code, true);
  return target_runcode;
}

// async function trpiler_py2js_async(logger, testcode_wrapper, test_runner, benchmarkname, goldfunc_code, sourcelang, targetlang, trans_prog_code, trans_prog_config_info, iframe_trans, _setCodes) {
//   if (goldfunc_code.indexOf("mylog(") >= 0) throw Error("UNEXPECTED goldfunc_code should not have mylog calls.");
//   let filename = "./comparisons/try_py2js/trans/" + benchmarkname.slice(4,-3) + ".js";
//   let py2js_result = await anyfileAsync(filename);
//   let libcode = await anyfileAsync("./comparisons/py2js/py-builtins.js");
//   let gold_translated_code = "/////libcode-start/////\n" + libcode +  "/////libcode-end/////\n" + py2js_result;
//   let translated_code = testcode_wrapper(gold_translated_code);
//   let [is_success, target_runcode, target_log, target_error] = await test_runner(translated_code, false);
//   if (is_success) return py2js_result;

//   throw Error("Translation is not correct.");
// }

function gen_goldtrans_rules_noinstru_async(use_error_table) {
  return async function goldtrans_rules_noinstru_async(logger, testcode_wrapper, test_runner, benchmarkname, goldfunc_code, sourcelang, targetlang, trans_prog_code, trans_prog_config_info, iframe_trans, _setCodes) {
    _setCodes(iframe_trans, goldfunc_code, sourcelang, trans_prog_code, "Benchmark: " + benchmarkname);
    let goldfunc_trans_code = null;
    let goldfunc_src_parse = null;
    let translated_code = null;
    let auto_tried_choices = [];
  
    async function _auto_translate_forgoldfunc(iframe) {
      let transChoicesHandler = iframe.contentWindow.translateHandlerChAsync;
      let gold_translated_code = "ERROR_OR_EMPTY";
      let translate_src_parse = null;
      while(true) {
        let trans_choices_time1 = performance.now();
        await transChoicesHandler();
        let trans_choices_time2 = performance.now();
        logger("TIME (translateHandlerChAsync): " + String((trans_choices_time2 - trans_choices_time1) / 1000));

        gold_translated_code = iframe.contentWindow.getTranslatedCode();
        translate_src_parse = iframe.contentWindow.getTranslateSrcParse();
        if (gold_translated_code === "ERROR_OR_EMPTY") {
          if (MANUAL_FIX_ENABLED) {
            logger("_auto_translate ERROR_OR_EMPTY. Waiting for user...");
            await iframe.contentWindow.waitForContinueClickAsync();
          } else {
            throw Error("FAILED to do _auto_translate (ERROR_OR_EMPTY) and manual fix is disabled.");
          }
        } else break;
      }
      logger("get gold_translated_code. length=", gold_translated_code.length);
      return [gold_translated_code, translate_src_parse];
    }
  
    let current_choices = null;
    let translate_dbg_history = null;
    let translated_code_map = null;
    let target_error = null;
    while(true) {
      let auto_trans_time1 = performance.now();
      let is_getting_translation = true;
      try {
        [goldfunc_trans_code, goldfunc_src_parse] = await _auto_translate_forgoldfunc(iframe_trans);
      } catch (err) {
        logger("NOT getting valid translation: " + err);
        if (String(err).indexOf("FAILED to do _auto_translate (ERROR_OR_EMPTY)") >= 0) {
          //[goldfunc_trans_code, goldfunc_src_parse] should stay as old
          //indicate it is error.
          is_getting_translation = false;
        } else {
          throw err;
        }
      }
      let auto_trans_time2 = performance.now();
      logger("TIME (_auto_translate_forgoldfunc): " + String((auto_trans_time2 - auto_trans_time1) / 1000));

      if (is_getting_translation) {
        current_choices = iframe_trans.contentWindow.getChoices();
        translate_dbg_history = iframe_trans.contentWindow.getTranslateDbgHistory();
        translated_code_map = iframe_trans.contentWindow.getTranslatedCodeMap();
      } else {
        //keep the last round info.
      }

      let translate_timespan = iframe_trans.contentWindow.getTranslateTimespan();
      let translate_timespan_pretty = iframe_trans.contentWindow.getTranslateTimespanPretty();
      logger("TIME (Translator Report): " + translate_timespan);
      logger("TIME (Translator Pretty Report): " + translate_timespan_pretty);

      if (is_getting_translation) {
        translated_code = testcode_wrapper(goldfunc_trans_code);
        let [is_success, target_runcode, target_log, _tmp_target_error, timespan_s, timespan_t] = await test_runner(translated_code, false);
        target_error = _tmp_target_error;
        logger("TIME (Tester Report run source): " + timespan_s);
        logger("TIME (Tester Report run target): " + timespan_t);
  
        let all_rule_ids = translate_dbg_history.map(x => x.dbg_info.notes["rule_id"]);
        logger("APPLIED_RULE_IDS (" + (is_success ? "SUCCESS" : "FAILED") + "): " + JSON.stringify(all_rule_ids));
        if (is_success) break;  
      }
      
      if (current_choices === null) {
        throw Error("FAILED to produce any valid translation.");
      }

      console.log("Trying automatic fix. current_choices:", current_choices, " translate_dbg_history:", translate_dbg_history, " translated_code_map:", translated_code_map, " error_info:", target_error);
      let proposed_choices = null;
      if (use_error_table === false) {
        logger("Trying automatic fix (error_table OFF)...");
        proposed_choices = proposeAutoFixNoinstru(translated_code, goldfunc_trans_code, current_choices, auto_tried_choices, translate_dbg_history, translated_code_map, target_error, null);
      } else {
        logger("Trying automatic fix (error_table ON)...");
        proposed_choices = proposeAutoFixNoinstru(translated_code, goldfunc_trans_code, current_choices, auto_tried_choices, translate_dbg_history, translated_code_map, target_error, trans_prog_config_info);
      }
      
      if (proposed_choices === null || proposed_choices === undefined) {
        if (MANUAL_FIX_ENABLED) {
          logger("Failed to find an automatic fix. Waiting for user retry...");
          setTaskRunnerState(runner, RUNNER_STATE_PAUSED);
          iframe_trans.contentWindow.setForHumanAdjustment();
          await iframe_trans.contentWindow.waitForContinueClickAsync();
          setTaskRunnerState(runner, RUNNER_STATE_RUNNING);
        } else {
          throw Error("Failed to find an automatic fix and manual fix is disabled.");
        }
      }
      else {
        logger("Setting automatic fix (choices)...");
        auto_tried_choices.push(proposed_choices);
        iframe_trans.contentWindow.setChoices(proposed_choices["type"], proposed_choices["choices_list"]);
      }
    }
    return translated_code;
  }
}



////////////////////////////// dashboard config //////////////////////////////


let dashboard_layout = {
  "bodyZoom": "100%",
  "layout": {
    "id": null,
    "type": "HORIZONTAL",
    "width": "100%",
    "height": "100%",
    "children": [
      {
        "id": null,
        "type": "EMPTY",
        "width": "60px",
        "height": "100%"
      },
      {
        "id": null,
        "type": "VERTICAL",
        "width": "100%",
        "height": "100%",
        "children": [
          {
            "id": null,
            "type": "EMPTY",
            "width": "auto",
            "height": "60px"
          },
          {
            "id": null,
            "type": "HORIZONTAL",
            "width": "100%",
            "height": "100%",
            "children": [
              {
                "id": null,
                "type": "VERTICAL",
                "width": "40%",
                "height": "100%",
                "children": [
                  {
                    "id": null,
                    "type": "HORIZONTAL",
                    "width": "auto",
                    "height": "100px",
                    "children": [
                      {
                        "id": "statusBench",
                        "type": "LABELBLOCK",
                        "width": "33%",
                        "height": "auto"
                      },
                      {
                        "id": null,
                        "type": "VERTICAL",
                        "width": "33%",
                        "height": "auto",
                        "children": [
                          {
                            "id": "statusQueue",
                            "type": "LABELBLOCK",
                            "width": "auto",
                            "height": "100%",
                          },
                          {
                            "id": null,
                            "type": "HORIZONTAL",
                            "width": "auto",
                            "height": "40px",
                            "children": [
                              {
                                "id": "buttonAddAllTasks",
                                "innerText": "AddAll",
                                "type": "BUTTONBLOCK",
                                "width": "auto",
                                "height": "auto",
                              },
                              {
                                "id": "buttonClearTasks",
                                "innerText": "Clear",
                                "type": "BUTTONBLOCK",
                                "width": "auto",
                                "height": "auto",
                              },
                            ]
                          }
                        ]
                      },
                      {
                        "id": "statusServer",
                        "type": "LABELBLOCK",
                        "width": "33%",
                        "height": "auto"
                      },
                    ]
                  },
                  {
                    "id": "logMain",
                    "type": "LOGBLOCK",
                    "width": "auto",
                    "height": "100%"
                  }
                ]
              },
              {
                "id": null,
                "type": "VERTICAL",
                "width": "60%",
                "height": "100%",
                "children": [
                  {
                    "id": "logSub1",
                    "type": "LOGBLOCK",
                    "width": "auto",
                    "height": "100%"
                  },
                  {
                    "id": "logSub2",
                    "type": "LOGBLOCK",
                    "width": "auto",
                    "height": "100%"
                  }
                ]
              }
            ]
          },
          {
            "id": null,
            "type": "EMPTY",
            "width": "auto",
            "height": "60px"
          }
        ]
      },
      {
        "id": null,
        "type": "EMPTY",
        "width": "60px",
        "height": "100%"
      }
    ]
  }
};
