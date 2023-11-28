//////// initializer begin
(function () {
  let current_url = window.document.location.href;
  if (current_url.indexOf("/frontend/") >= 0) {
    window.SERVER_TEST_PREFIX = current_url.split("/frontend/")[0] + "/backend/test";
  } else {
    throw Error("Unexpected origin.");
  }
})();
//////// initializer end

async function standaloneRunAsync(code, lang, detail = false) {
  let postdata = {
    code: code,
    lang: lang,
  };
  if (detail === true) {
    postdata["detail"] = true;
  }
  let resultStr = await postAsync(SERVER_TEST_PREFIX, "/starun", postdata);
  let parseResult = JSON.parse(resultStr);
  console.log("standaloneRunAsync:", lang, parseResult);
  return parseResult;
}

async function standalonePairFileRunAsync(src_code, tar_code, srclang, tarlang, is_dryrun = false) {
  let postdata = {
    source_code: src_code,
    target_code: tar_code,
    source_language: srclang,
    target_language: tarlang,
    is_dryrun: is_dryrun,
  };
  let resultStr = await postAsync(SERVER_TEST_PREFIX, "/stapairrun", postdata);
  let parseResult = JSON.parse(resultStr);
  console.log("standalonePairFileRunAsync:", srclang + " -> " + tarlang, parseResult);
  return parseResult;
}

async function nodeModuleRunAsync(cwd, main) {
  let postdata = {
    cwd: cwd,
    main: main,
  };
  let resultStr = await postAsync(SERVER_TEST_PREFIX, "/nodemodulerun", postdata);
  let parseResult = JSON.parse(resultStr);
  console.log("nodeModuleRunAsync:", cwd, main, parseResult);
  return parseResult;
}

async function anyCmdRunAsync(cwd, cmd) {
  let postdata = {
    cwd: cwd,
    cmd: cmd,
  };
  let resultStr = await postAsync(SERVER_TEST_PREFIX, "/anycmdrun", postdata);
  let parseResult = JSON.parse(resultStr);
  console.log("anyCmdRunAsync:", cwd, cmd, parseResult);
  return parseResult;
}
