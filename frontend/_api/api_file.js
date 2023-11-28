//////// initializer begin
(function () {
  let current_url = window.document.location.href;
  if (current_url.indexOf("/frontend/") >= 0) {
    window.SERVER_FILE_PREFIX = current_url.split("/frontend/")[0] + "/backend/file";
  } else {
    throw Error("Unexpected origin.");
  }
})();
//////// initializer end

async function jsonRefAsync(filepath, keypath) {
  let netpath = SERVER_FILE_PREFIX + "/anyfile/" + filepath;
  console.log("# jsonRefAsync", netpath);
  let result = await request({
    url: netpath,
    method: "GET",
  });
  let json_result = JSON.parse(result);
  function _get_val(data, keys) {
    if (keys.length === 0) {
      return data;
    }
    return _get_val(data[keys[0]], keys.slice(1));
  }
  return _get_val(json_result, keypath);
}

async function anyfileAsync(filepath) {
  let netpath = SERVER_FILE_PREFIX + "/anyfile/" + filepath;
  console.log("# anyfileAsync", netpath);
  let result = await request({
    url: netpath,
    method: "GET",
  });
  return result;
}

async function getMultipleTextFilesAsync(filepaths) {
  console.log("# getMultipleTextFilesAsync", filepaths);
  let resp_str = await postAsync(SERVER_FILE_PREFIX, "/getmultipletextfile", { filepaths: filepaths });
  let resp = JSON.parse(resp_str);
  return resp;
}

async function deleteMultipleFilesAsync(limiting_folder, filepaths) {
  console.log("# deleteMultipleFilesAsync (under " + limiting_folder + ")", filepaths);
  let resp_str = await postAsync(SERVER_FILE_PREFIX, "/removemultiplefile", {
    limiting_folder: limiting_folder,
    filepaths: filepaths,
  });
  let resp = JSON.parse(resp_str);
  return resp;
}

function anyfileLink(filepath) {
  return SERVER_FILE_PREFIX + "/anyfile/" + filepath;
}

async function ensurePathAsync(folderpath) {
  let netpath = "/ensurepath/" + folderpath;
  console.log("# ensurePathAsync", folderpath);
  let result = await getAsync(SERVER_FILE_PREFIX, netpath);
  let resp = JSON.parse(result);
  if (resp["result"] !== "OK") throw Error("ensurePathAsync failed: " + result);
}

async function saveAnyTextfileAsync(filepath, content) {
  let netpath = "/postanytextfile/" + filepath;
  console.log("# saveAnyTextfileAsync", netpath);
  let result = await postRawTextAsync(SERVER_FILE_PREFIX, netpath, content);
  return result;
}

// NOTE this is potentially dangerous function, as it creates directories under data/
async function saveAnyTextfileMakedirsAsync(filepath, content) {
  let netpath = "/postanytextfile_makedirs/" + filepath;
  console.log("# saveAnyTextfileMakedirsAsync", netpath);
  let result = await postRawTextAsync(SERVER_FILE_PREFIX, netpath, content);
  return result;
}

async function appendAnyTextfileAsync(filepath, content) {
  let netpath = "/postappendanytextfile/" + filepath;
  console.log("# appendAnyTextfileAsync", netpath);
  let result = await postRawTextAsync(SERVER_FILE_PREFIX, netpath, content);
  return result;
}

// async function anybinfileAsync(filepath) {
//   let netpath = SERVER_FILE_PREFIX + "/anybinfile/" + filepath;
//   console.log("# anybinfileAsync", netpath);
//   let result = await request({
//     "url": netpath,
//     "method": "GET"
//   });
//   return result;
// }

async function anybinfileRemoteAsync(remote_origin, filepath) {
  let netpath = remote_origin + "/anybinfile/" + filepath;
  console.log("# anybinfileAsync", netpath);
  let result = await request(
    {
      url: netpath,
      method: "GET",
    },
    "blob"
  );
  return result;
}

async function saveAnybinfileAsync(filepath, rawdata) {
  console.log("# anybinfileAsync", filepath);
  let result = await postRawBinaryAsync(SERVER_FILE_PREFIX, "/postanybinfile/" + filepath, rawdata);
  return result;
}

async function listGlobAsync(glob) {
  console.log("# listGlobAsync", glob);
  let resp_str = await postAsync(SERVER_FILE_PREFIX, "/listglob", { glob });
  let resp = JSON.parse(resp_str);
  return resp;
}

async function listDirAsync(lang, dirpath) {
  let resp_str = await postAsync(SERVER_FILE_PREFIX, "/listdir", { language: lang, dirpath: dirpath });
  return (resp = JSON.parse(resp_str));
}

async function listDirTreeAsync(lang, dirpath) {
  let resp_str = await postAsync(SERVER_FILE_PREFIX, "/listdirtree", { language: lang, dirpath: dirpath });
  return (resp = JSON.parse(resp_str));
}

async function listDirTreeNestedAsync(lang, dirpath) {
  let resp_str = await postAsync(SERVER_FILE_PREFIX, "/listdirtreenested", { language: lang, dirpath: dirpath });
  return (resp = JSON.parse(resp_str));
}

async function listDirAllMetaLocalAsync(dirpath, include_pattern, ignore_pattern) {
  let resp_str = await postAsync(SERVER_FILE_PREFIX, "/listdirallmeta", {
    dirpath: dirpath,
    include_pattern: include_pattern,
    ignore_pattern: ignore_pattern,
  });
  return (resp = JSON.parse(resp_str));
}

async function listDirAllMetaRemoteAsync(remote_origin, dirpath, include_pattern, ignore_pattern) {
  let resp_str = await postAsync(remote_origin, "/listdirallmeta", {
    dirpath: dirpath,
    include_pattern: include_pattern,
    ignore_pattern: ignore_pattern,
  });
  return (resp = JSON.parse(resp_str));
}

async function getGitStatusAsync() {
  let resp_str = await getAsync(SERVER_FILE_PREFIX, "/gitstatus");
  return JSON.parse(resp_str);
}

async function echoAsync(msg) {
  let resp_str = await getAsync(SERVER_FILE_PREFIX, "/echo/" + msg);
  return resp_str;
}
