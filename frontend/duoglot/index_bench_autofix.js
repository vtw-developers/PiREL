function get_charpos_to_linepos_maplists(lines) {
  let linemap = [];
  let columnmap = [];
  for (let i = 0; i < lines.length; i++) {
    let line = lines[i];
    for (let j = 0; j < line.length; j++) {
      linemap.push(i);
      columnmap.push(j);
    }
    // the newline char
    linemap.push(i);
    columnmap.push(-1);
  }
  return {linemap, columnmap};
}

function proposeAutoFixNoinstru(
  wrapper_code,
  focus_code,
  current_choices,
  tried_choices_history,
  translate_dbg_history,
  translated_code_map,
  error_info,
  trans_prog_config_info
) {

  let focus_splitted = wrapper_code.split(focus_code);
  if (focus_splitted.length !== 2) {
    throw Error("focus_code should appear once in wrapper");
  }

  let [before_focus, after_focus] = focus_splitted;
  let before_focus_lines = before_focus.split("\n");
  let focus_lines = focus_code.split("\n");
  let before_line_count = before_focus_lines.length;

  let {error_msg, error_type, line_content, lineno} = error_info;
  let line_idx = null;

  if (error_type === "SyntaxError:" || error_type === "ReferenceError:" || error_type === "TypeError:") {
    line_idx = lineno[1] - before_line_count;
    let expected_line = focus_lines[line_idx];

    if (expected_line === undefined) {
      throw Error("Expected line doesn't exist for line_idx " + line_idx);
    }
    if (expected_line.indexOf(line_content) < 0) {
      throw Error("Expected line doesn't contains error line content.");
    }

    console.log(error_type + " at line ", line_idx + 1, "(idx=" + line_idx + ")", line_content);
  } else {
    throw Error("proposeAutoFix Unknown Error Type:" + error_type + " msg:" + error_msg);
  }

  let {linemap, columnmap} = get_charpos_to_linepos_maplists(focus_lines);
  let exids_by_line_idx = {};
  for (let exid in translated_code_map) {
    let ranges_of_exid = translated_code_map[exid];
    for (let rg of ranges_of_exid) {
      let {range, str} = rg;
      let [chpos1, chpos2] = range;

      if (focus_code.slice(chpos1, chpos2) !== str) {
        console.error("code_map is wrong!", focus_code.slice(chpos1, chpos2), str);
        throw Error("ErrorCodeMap");
      }

      let linepos1 = linemap[chpos1];
      let linepos2 = linemap[chpos2];
      if (linepos1 === linepos2) {
        if(focus_lines[linepos1].indexOf(str) < 0) {
          console.error("code_map processing code is wrong!", focus_lines[linepos1], str);
          throw Error("ErrorProcessingCodeMap");
        }
        if (!(linepos1 in exids_by_line_idx)) {
          exids_by_line_idx[linepos1] = {};
        }
        exids_by_line_idx[linepos1][exid] = true;
      } else {
        alert("Unhandled case: a str across multiple lines.");
        throw Error("Unhandled case: a str across multiple lines.");
      }
    }
  }

  let alt_step_to_choices_exid = [];
  let exid_to_alt_step_choices = {};
  for (let elem of translate_dbg_history) {
    console.assert(elem["alt_step"] - 1 === alt_step_to_choices_exid.length);
    let push_obj = {
      "alt_step": elem["alt_step"],
      "next_choices_count": elem["next_choices_status"]["count"],
      "next_choices_all_known": elem["next_choices_status"]["done"],
      "ex_id": elem["dbg_info"]["ex_id"],
      "current_choose_idx": elem["dbg_info"]["notes"]["choose_idx"],
      "current_rule_id": elem["dbg_info"]["notes"]["rule_id"],
      "current_range_key": elem["range_info"]
    }
    alt_step_to_choices_exid.push(push_obj);
    exid_to_alt_step_choices[push_obj["ex_id"]] = push_obj;
  }
  console.log("proposeAutoFix exids_by_line_idx:", exids_by_line_idx);
  console.log("proposeAutoFix exid_to_alt_step_choices:", exid_to_alt_step_choices);
  // console.log("proposeAutoFix alt_step_to_choices_exid:", alt_step_to_choices_exid);

  let canskip_dict = {};
  let error_table_available = trans_prog_config_info !== null && "skip_on_line_error" in trans_prog_config_info;
  if (error_table_available) {
    for (let rule_id in trans_prog_config_info["skip_on_line_error"]) {
      let error_matcher = trans_prog_config_info["skip_on_line_error"][rule_id];
      if ("error_type" in error_matcher) {
        let re = new RegExp(error_matcher["error_type"]);
        if (!re.test(error_type)) continue;
      }
      if ("error_msg" in error_matcher) {
        let re = new RegExp(error_matcher["error_msg"]);
        if (!re.test(error_msg)) continue;
      }
      canskip_dict[rule_id] = true;
    }
  }

  // get relevant choices_and_exid
  let exids = exids_by_line_idx[line_idx];
  console.log("proposeAutoFix line_idx:", line_idx, " exids:", exids);
  let related_alt_step_infos = {};
  let RELATED_WINDOW_SIZE = 1;

  for (let exid in exids) {
    let alt_step_info = exid_to_alt_step_choices[exid];
    let alt_step = alt_step_info["alt_step"];

    for (let i = alt_step - 1 - RELATED_WINDOW_SIZE; i <= alt_step - 1; i++) {
      if (i <= 0 || i >= alt_step_to_choices_exid.length) {
        continue;
      }
      if (alt_step_to_choices_exid[i-1]["next_choices_count"] > 1) {
        let related_alt_step_id = alt_step_to_choices_exid[i]["alt_step"];
        let rule_id = alt_step_to_choices_exid[i]["current_rule_id"];
        let is_skip_allowed = rule_id in canskip_dict;
        related_alt_step_infos[related_alt_step_id] = [
          alt_step_to_choices_exid[i-1]["next_choices_count"],
          alt_step_to_choices_exid[i]["current_choose_idx"],
          alt_step_to_choices_exid[i]["ex_id"],
          rule_id,
          is_skip_allowed,
          alt_step_to_choices_exid[i]["current_range_key"],];
      }
    }
  }

  if (error_table_available) {
    let filtered_related_alt_step_infos = {};

    for (k in related_alt_step_infos) {
      let info = related_alt_step_infos[k];
      if (info[4] === true) {
        filtered_related_alt_step_infos[k] = info;
      }
    }

    console.log("proposeAutoFix related_alt_steps:", related_alt_step_infos, " filtered (err_table):", filtered_related_alt_step_infos);
    let new_choices = find_next_unique_choices(filtered_related_alt_step_infos, current_choices, tried_choices_history);
    console.log("proposeAutoFix get_new_choices:", current_choices, "->", new_choices);
    return new_choices;

  } else {
    console.log("proposeAutoFix related_alt_steps:", related_alt_step_infos, "(no filter)");
    let new_choices = find_next_unique_choices(related_alt_step_infos, current_choices, tried_choices_history);
    console.log("proposeAutoFix get_new_choices:", current_choices, "->", new_choices);
    return new_choices;
  }
}

function find_next_unique_choices(related_alt_step_infos, current_choices, tried_choices_history) {
  let {type, choices_list} = current_choices;
  if (type === "STEP") {
    for (alt_step in related_alt_step_infos) {
      let [chcount, current_ch] = related_alt_step_infos[alt_step];
      for (let i = 0; i < chcount; i++) {
        if (i === current_ch) {
          continue;
        }
        let updated_choices_list = _step_choices_list_update(choices_list, parseInt(alt_step), i);
        console.log("find_next_unique_choices updated_choices_list:", updated_choices_list);
        let new_choices = {
          "type": "STEP",
          "choices_list": updated_choices_list
        };
        if(!_choices_any_duplicate(new_choices, tried_choices_history)) {
          return new_choices;
        }
      }
    }
  } else if (type === "ASTNODE") {
    // TODO...
    for (alt_step in related_alt_step_infos) {
      let [chcount, current_ch] = related_alt_step_infos[alt_step];
      let current_range_key = related_alt_step_infos[alt_step][5];
      for (let i = 0; i < chcount; i++) {
        if (i === current_ch) {
          continue;
        }
        let updated_choices_list = _astnode_choices_list_update(choices_list, current_range_key, i);
        console.log("find_next_unique_choices updated_choices_list:", updated_choices_list);
        let new_choices = {
          "type": "ASTNODE",
          "choices_list": updated_choices_list
        };
        if(!_choices_any_duplicate(new_choices, tried_choices_history)) {
          return new_choices;
        }
      }
    }
  } else {
    throw Error("find_next_unique_choices not implemented for type: " + type);
  }
  return null;
}

function _step_choices_list_update(current_choices_list, step, update_ch) {
  let new_choices = [];
  let is_set = false;
  for (let choice of current_choices_list) {
    if (choice[0] === step) {
      is_set = true;
      if(update_ch !== 0) new_choices.push([step, update_ch]);
    } else {
      if (choice[0] > step) continue;
      else new_choices.push(choice);
    }
  }
  if (!is_set && update_ch !== 0) new_choices.push([step, update_ch]);
  return new_choices;
}

function _astnode_choices_list_update(current_choices_list, current_range_key, update_ch) {
  let new_choices = [];
  let is_set = false;
  let [c_astid, c_start, c_end] = current_range_key;
  for (let choice of current_choices_list) {
    let [astid, start, end] = choice[0];
    if (c_astid === astid && c_start === start && c_end === end) {
      is_set = true;
      if(update_ch !== 0) new_choices.push([current_range_key, update_ch]);
    } else {
      new_choices.push(choice);
    }
  }
  if (!is_set && update_ch !== 0) new_choices.push([current_range_key, update_ch]);
  return new_choices;
}

function _step_choices_list_compare(choices_list1, choices_list2) {
  let choices1_dict = {};
  for (let [step, ch] of choices_list1) {
    if (step in choices1_dict) {
      throw Error("_step_choices_list_compare invalid choices_list1: duplicated step: " + JSON.stringify(choices1_dict));
    }
    if (ch !== 0) {
      choices1_dict[step] = ch;
    }
  }
  for (let [step, ch] of choices_list2) {
    if (step in choices1_dict) {
      if (choices1_dict[step] === ch) {
        choices1_dict[step] = -1;
        continue;
      } else {
        return false;
      }
    } else {
      if (ch === 0) {
        continue;
      } else {
        return false;
      }
    }
  }
  for (let step in choices1_dict) {
    if (choices1_dict[step] !== -1) {
      return false;
    }
  }
  return true;
}

function _astnode_choices_list_compare(choices_list1, choices_list2) {
  let choices1_dict = {};
  for (let [range_key, ch] of choices_list1) {
    let [astid, start, end] = range_key;
    let range_key_str = astid + "-" + start + "-" + end;
    if (range_key_str in choices1_dict) {
      throw Error("_astnode_choices_list_compare invalid choices_list1: duplicated range_key: " + JSON.stringify(choices1_dict));
    }
    if (ch !== 0) {
      choices1_dict[range_key_str] = ch;
    }
  }
  for (let [range_key, ch] of choices_list2) {
    let [astid, start, end] = range_key;
    let range_key_str = astid + "-" + start + "-" + end;
    if (range_key_str in choices1_dict) {
      if (choices1_dict[range_key_str] === ch) {
        choices1_dict[range_key_str] = -1;
        continue;
      } else {
        return false;
      }
    } else {
      if (ch === 0) {
        continue;
      } else {
        return false;
      }
    }
  }
  for (let range_key_str in choices1_dict) {
    if (choices1_dict[range_key_str] !== -1) {
      return false;
    }
  }
  return true;
}

function _choices_any_duplicate(choices, tried_choices_history) {
  let {type, choices_list} = choices;
  for (let cmpchoices of tried_choices_history) {
    let cmp_type = cmpchoices["type"];
    if (cmp_type !== type) {
      throw Error("_choices_any_duplicate boolean check FAILED. Choices are of different type.");
    }
    let cmp_choices_list = cmpchoices["choices_list"];
    if (type === "STEP") {
      if (_step_choices_list_compare(choices_list, cmp_choices_list)) {
        return true;
      }
    } else if (type === "ASTNODE") {
      if (_astnode_choices_list_compare(choices_list, cmp_choices_list)) {
        return true;
      }
    } else {
      throw Error("_choices_any_duplicate unknown type: " + type);
    }
  }
  return false;
}