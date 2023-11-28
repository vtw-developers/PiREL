// functions

function sleepAsync(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function sleepUntilAsync(cond_func, interval) {
  while (!cond_func()) {
    await sleepAsync(interval);
  }
}

function request(obj, resp_type = null) {
  return new Promise((resolve, reject) => {
    let xhr = new XMLHttpRequest();
    if (resp_type) xhr.responseType = resp_type;
    xhr.open(obj.method || "GET", obj.url);
    if (obj.headers) {
      Object.keys(obj.headers).forEach((key) => {
        xhr.setRequestHeader(key, obj.headers[key]);
      });
    }
    xhr.onload = () => {
      if (xhr.status >= 200 && xhr.status < 300) {
        resolve(xhr.response);
      } else {
        console.error("my XHR request unwanted statusCode:", xhr.status);
        reject(xhr.statusText);
      }
    };
    xhr.onerror = (e) => {
      console.error("my XHR request error:", e);
      reject(xhr.statusText);
    };
    xhr.send(obj.body);
  });
}

async function getAsync(prefix, path) {
  let netpath = prefix + path;
  let t1 = performance.now();
  let result = await request({
    url: netpath,
    method: "GET",
  });
  let t2 = performance.now();
  console.log(`# getAsync (${Math.round(t2 - t1)}ms)`, netpath);
  return result;
}

async function getPageRelAsync(relpath) {
  let t1 = performance.now();
  let result = await request({
    url: relpath,
    method: "GET",
  });
  let t2 = performance.now();
  console.log(`# getPageRelAsync (${Math.round(t2 - t1)}ms)`, relpath);
  return result;
}

async function postAsync(prefix, path, data) {
  let netpath = prefix + path;
  let t1 = performance.now();
  let result = await request({
    url: netpath,
    headers: { "Content-Type": "application/json;charset=UTF-8" },
    method: "POST",
    body: JSON.stringify(data),
  });
  let t2 = performance.now();
  console.log(`# postAsync (${Math.round(t2 - t1)}ms)`, netpath);
  return result;
}

async function postRawBinaryAsync(prefix, path, rawdata) {
  let netpath = prefix + path;
  let t1 = performance.now();
  let result = await request({
    url: netpath,
    headers: { "Content-Type": "application/octet-stream" },
    method: "POST",
    body: rawdata,
  });
  let t2 = performance.now();
  console.log(`# postRawBinaryAsync (${Math.round(t2 - t1)}ms)`, netpath);
  return result;
}

async function postRawTextAsync(prefix, path, rawtext) {
  let netpath = prefix + path;
  let t1 = performance.now();
  let result = await request({
    url: netpath,
    headers: { "Content-Type": "text/plain" },
    method: "POST",
    body: rawtext,
  });
  let t2 = performance.now();
  console.log(`# postRawTextAsync (${Math.round(t2 - t1)}ms)`, netpath);
  return result;
}

function url_to_origin_info(url = window.document.location.origin) {
  let url_origin_splits = url.split("://");
  let protocol = url_origin_splits[0];
  let origin = url_origin_splits[1];
  let [domain_name, port] = origin.split(":");
  return {
    protocol,
    domain_name,
    port,
  };
}

function origin_info_to_url(origin_info) {
  let { protocol, domain_name, port } = origin_info;
  return protocol + "://" + domain_name + ":" + String(port);
}

function create_url(prefix, path, params) {
  let netpath = prefix ? prefix + path : path;
  let url = prefix ? new URL(netpath) : new URL(netpath, window.document.location);
  url.search = new URLSearchParams(params);
  return url.toString();
}

function normalize_filepath(path) {
  let result = path;
  while (result.startsWith("./")) result = result.slice(2);
  result = result.replaceAll("/./", "/");
  result = result.replaceAll("//", "/");
  let result_segs = result.split("/");
  if (result_segs.indexOf("..") >= 0) throw Error("normalize_filepath: .. not implemented");
  return result;
}

function assertCB(cond, msg = null) {
  if (cond === false) throw Error("Assertion Violated. Message: " + msg);
}

function debounce(func, wait, immediate) {
  var timeout;
  return function () {
    var context = this,
      args = arguments;
    var later = function () {
      timeout = null;
      if (!immediate) func.apply(context, args);
    };
    var callNow = immediate && !timeout;
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
    if (callNow) func.apply(context, args);
  };
}

async function errorWrapperPromiseAsync(promise, errorFunc) {
  try {
    console.log("--- errorWrapperPromiseAsync ---");
    return await promise;
  } catch (e) {
    console.log("--- errorWrapperPromiseAsync error:", e);
    return await errorFunc(e);
  }
}

async function errorWrapperFuncAsync(func, errorFunc) {
  try {
    console.log("--- errorWrapperFuncAsync ---");
    return await func();
  } catch (e) {
    console.log("--- errorWrapperFuncAsync error:", e);
    return await errorFunc(e);
  }
}

async function errorWrapperFuncArgsAsync(func, args, errorFunc) {
  try {
    console.log("--- errorWrapperFuncArgsAsync ---");
    return await func(...args);
  } catch (e) {
    console.log("--- errorWrapperFuncArgsAsync error:", e);
    return await errorFunc(e);
  }
}

function error404Nullify(err) {
  if (String(err) === "NOT FOUND") {
    return null;
  }
  throw err;
}

function errorAnyAlert(err) {
  alert("!UNEXPECTED_ERROR! " + err);
  throw err;
}

function messageFunc1Gen(handler_list, default_func) {
  function _messageFunc(msg) {
    if (typeof msg === "string") {
      for (let [prefix, func] of handler_list) {
        if (msg.startsWith(prefix)) {
          return func(msg);
        }
      }
    }
    return default_func(msg);
  }
  return _messageFunc;
}

function combineVoidFuncN() {
  let func_list = arguments;
  function _combined_func() {
    for (let func of func_list) {
      func(...arguments);
    }
  }
  return _combined_func;
}

function composeFuncN() {
  let func_list = arguments;
  function _combined_func() {
    let current_args = arguments;
    let retval = null;
    for (let func of func_list) {
      retval = func(...current_args);
      current_args = [retval];
    }
    return retval;
  }
  return _combined_func;
}

////////////// string prototypes //////////

String.prototype.hashCode = function () {
  var hash = 0,
    i,
    chr;
  if (this.length === 0) {
    return hash;
  }
  for (i = 0; i < this.length; i++) {
    chr = this.charCodeAt(i);
    hash = (hash << 5) - hash + chr;
    hash |= 0; // Convert to 32bit integer
  }
  return hash;
};

///////////// git status utils ///////////

function parse_gitstatus(content) {
  let lines = content.split("\n");
  if (lines[0] !== "GITSTATUS") {
    throw Error("Unexpected gitstatus content.");
  }
  let commit_hash = lines[1];
  let is_clean = content.indexOf("working tree clean") >= 0;
  return { commit_hash: commit_hash, is_clean: is_clean };
}

////////////// string utils //////////////

function string_idx_to_line_column_func_gen(raw_str) {
  let seperated_lines = raw_str.split("\n");
  let char_before = [0];
  for (let line of seperated_lines) {
    char_before.push(char_before[char_before.length - 1] + line.length + 1);
  }
  return function (idx) {
    if (idx < 0) {
      return [-1, -1];
    }
    if (idx >= raw_str.length) {
      return [-1, -1];
    }
    let line_i = 0;
    for (; line_i < seperated_lines.length; line_i++) {
      if (idx >= char_before[line_i] && idx < char_before[line_i + 1]) break;
    }
    if (line_i === seperated_lines.length) {
      return [-1, -1];
    }
    return [line_i, idx - char_before[line_i]];
  };
}

function get_dirpath_of_filepath(filepath) {
  let segs = filepath.split("/");
  return segs.slice(0, -1).join("/") + "/";
}

function get_date_time_str(now) {
  let date =
    now.getFullYear() +
    "-" +
    String(now.getMonth() + 1).padStart(2, "0") +
    "-" +
    String(now.getDate()).padStart(2, "0");
  let time =
    String(now.getHours()).padStart(2, "0") +
    "-" +
    String(now.getMinutes()).padStart(2, "0") +
    "-" +
    String(now.getSeconds()).padStart(2, "0");
  let now_str = date + "-" + time;
  return now_str;
}

/////////////////// array utils //////////////////////

function collect_inc_until(array, start_idx, until_func) {
  let result = [];
  let result_idx = start_idx;
  for (; result_idx < array.length; result_idx++) {
    if (until_func(array[result_idx])) {
      result.push(array[result_idx]);
    } else {
      break;
    }
  }
  return [result, result_idx - 1];
}

function collect_dec_until(array, start_idx, until_func) {
  let result = [];
  let result_idx = start_idx;
  for (; result_idx >= 0; result_idx--) {
    if (until_func(array[result_idx])) {
      result.push(array[result_idx]);
    } else {
      break;
    }
  }
  return [result, result_idx + 1];
}

///////////////////////// json-ml utils ////////////////////////

// https://github.com/danklammer/bytesize-icons

function jsonml_svg_icon_move(class_sufix) {
  return [
    "svg" + class_sufix,
    {
      xmlns: "http://www.w3.org/2000/svg",
      viewBox: "0 0 32 32",
      width: "32",
      height: "32",
      fill: "none",
      stroke: "currentcolor",
      "stroke-linecap": "round",
      "stroke-linejoin": "round",
      "stroke-width": "2",
    },
    [
      "path",
      { d: "M3 16 L29 16 M16 3 L16 29 M12 7 L16 3 20 7 M12 25 L16 29 20 25 M25 12 L29 16 25 20 M7 12 L3 16 7 20" },
    ],
  ];
}

function jsonml_svg_icon_trash(class_sufix) {
  return [
    "svg" + class_sufix,
    {
      xmlns: "http://www.w3.org/2000/svg",
      viewBox: "0 0 32 32",
      width: "32",
      height: "32",
      fill: "none",
      stroke: "currentcolor",
      "stroke-linecap": "round",
      "stroke-linejoin": "round",
      "stroke-width": "2",
    },
    ["path", { d: "M28 6 L6 6 8 30 24 30 26 6 4 6 M16 12 L16 24 M21 12 L20 24 M11 12 L12 24 M12 6 L13 2 19 2 20 6" }],
  ];
}

///////////////// json utils //////////////////

function json_dump_list_elem_per_line(obj) {
  return "[\n" + obj.map((x) => "  " + JSON.stringify(x)).join(",\n") + "\n]";
}

///////////////// monaco utils //////////////////

async function monacoLoadCodeAsync(code_editor, lang, new_code_str) {
  let srcModel = code_editor.getModel();
  monaco.editor.setModelLanguage(srcModel, monaco_language_name_dict[lang]);
  code_editor.setValue(new_code_str);
}

function monacoApplyDecorations(code_editor, decos) {
  //see the doc about adding decorations in monaco editor
  //https://microsoft.github.io/monaco-editor/playground.html#interacting-with-the-editor-line-and-inline-decorations
  code_editor.__my_old_deco_ids = code_editor.deltaDecorations(
    code_editor.__my_old_deco_ids ? code_editor.__my_old_deco_ids : [],
    decos
  );
}

function monacoApplyGroupDecorations(code_editor, decos, group_name) {
  //see the doc about adding decorations in monaco editor
  //https://microsoft.github.io/monaco-editor/playground.html#interacting-with-the-editor-line-and-inline-decorations
  if (code_editor.__my_old_deco_groups_ids === undefined || code_editor.__my_old_deco_groups_ids === null)
    code_editor.__my_old_deco_groups_ids = {};
  code_editor.__my_old_deco_groups_ids[group_name] = code_editor.deltaDecorations(
    code_editor.__my_old_deco_groups_ids[group_name] ? code_editor.__my_old_deco_groups_ids[group_name] : [],
    decos
  );
}

//https://github.com/microsoft/vscode/blob/3a73bf805c0396d9e578f73586b90de63811dca2/extensions/npm/src/scriptHover.ts#L92-L99
//MIT License
function createMarkdownCommandLinkForMonaco(label, cmd, args, tooltip, separator = null) {
  let encodedArgs = encodeURIComponent(JSON.stringify(args));
  let prefix = "";
  if (separator) {
    prefix = ` ${separator} `;
  }
  return `${prefix}[${label}](command:${cmd}?${encodedArgs} "${tooltip}")`;
}
