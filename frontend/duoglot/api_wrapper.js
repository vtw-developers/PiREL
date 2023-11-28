
async function getTestfilesAsync() {
  let fileDictStr = await postAsync(SERVER_FILE_PREFIX, "/listdirtreenested", {language: null, "dirpath": "duoglot/tests/basic"});
  return JSON.parse(fileDictStr);
}

async function getProgfilesAsync() {
  let profDictStr = await postAsync(SERVER_FILE_PREFIX, "/listdirtreenested", {language: null, "dirpath": "duoglot/tests/trans_programs"});
  return JSON.parse(profDictStr);
}

async function getGeneralBenchFilesAsync(dirname) {
  let fileDictStr = await postAsync(SERVER_FILE_PREFIX, "/listdirtreenested", {language: null, "dirpath": "duoglot/tests/" + dirname});
  return JSON.parse(fileDictStr);
}

async function tryReadOutputFileAsync(filepath) {
  let fullpath = "duoglot/tests/_output_/" + filepath;
  return await errorWrapperPromiseAsync(anyfileAsync(fullpath), error404Nullify);
}

async function tryReadFileAsync(filepath) {
  let fullpath = filepath;
  return await errorWrapperPromiseAsync(anyfileAsync(fullpath), error404Nullify);
}

async function listOutputDirFilesAsync(outputDir) {
  let fullpath = "duoglot/tests/_output_/" + outputDir; //this is path, not url. This is post not get
  let result = await listDirAsync(null, fullpath);
  if ("error_msg" in result) {
    console.log("listOutputDirAsync error:", result["error_msg"]);
    return null;
  }
  let result_list = result["filepaths"];
  let ret_list = [];
  for (let file of result_list) {
    let pathsegs = file.split("/");
    ret_list.push(pathsegs[pathsegs.length - 1]);
  }
  return ret_list;
}

async function writeOutputFileAsync(filepath, content) {
  let fpath = "duoglot/tests/_output_/" + filepath;
  let fdir = get_dirpath_of_filepath(fpath);
  await ensurePathAsync(fdir);
  let resp = await saveAnyTextfileAsync(fpath, content);
  let parsed_resp = JSON.parse(resp);
  return parsed_resp;
}
