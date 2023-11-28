window._postproc_source_copy_func = ((translated_code, src_code, src_ast, src_ann, src_ast_dict) => {
  const regexp = /SOURCE_AST_IDX\((\d+)\)/g;
  let all_match = [...translated_code.matchAll(regexp)];
  let return_code = translated_code;
  for (let match of all_match) {
    let piece = match[0];
    let astidx = parseInt(match[1]);
    let astann = src_ann[astidx];
    let [start, end] = astann;
    console.log("match_detail:", piece, astidx, start, end);
    let focus_text = src_code.slice(start, end);
    //console.log("match_focus:", focus_text);
    return_code = return_code.split(piece).join(focus_text);
    //return_code = return_code.replace(piece, focus_text); SHIT!
  }
  return return_code;
});

window._postproc_py_array_to_js_array_func = ((translated_code, src_code, src_ast, src_ann, src_ast_dict) => {
  const regexp = /SOURCE_AST_IDX\((\d+)\)/g;
  let all_match = [...translated_code.matchAll(regexp)];
  let return_code = translated_code;
  for (let match of all_match) {
    let piece = match[0];
    let astidx = parseInt(match[1]);
    let astann = src_ann[astidx];
    let [start, end] = astann;
    console.log("match_detail:", piece, astidx, start, end);
    let focus_text = src_code.slice(start, end);
    //transform py nexted list-tuple to js array
    let trans_chars = [];
    let is_in_string = false;
    let is_escaping = false;
    for (let i = 0; i < focus_text.length; i++) {
      let focus_char = focus_text[i];
      if (is_in_string) {
        if (focus_char == '\\') is_escaping = true;
        else if (is_escaping) is_escaping = false;
        else if (focus_char == '"') is_in_string = false;
      }
      else {
        if (focus_char === '(') { trans_chars.push('['); continue; }
        if (focus_char === ')') { trans_chars.push(']'); continue; }
      }
      trans_chars.push(focus_char);
    }
    if (trans_chars.length !== focus_text.length) throw Error("py_array_to_js_array string length mismatch");
    let new_focus_text = trans_chars.join("");
    return_code = return_code.replace(piece, new_focus_text);
  }
  return return_code;
});