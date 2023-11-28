// namespace for utils
var utils_ns = {};

// ==============================================================================
// ================= UTILS ======================================================
// ==============================================================================

/**
 * https://stackoverflow.com/questions/11935175/sampling-a-random-subset-from-an-array
*/
utils_ns.getRandomSubarray = function (arr, size) {
  var shuffled = arr.slice(0), i = arr.length, temp, index;
  while (i--) {
      index = Math.floor((i + 1) * Math.random());
      temp = shuffled[index];
      shuffled[index] = shuffled[i];
      shuffled[i] = temp;
  }
  return shuffled.slice(0, size);
}

utils_ns.sleep = async function (msDuration) {
  await new Promise((r) => setTimeout(r, msDuration));
}

// ==============================================================================
// ================= FILE I/O ===================================================
// ==============================================================================

/**
 * PARAMS
 * relDirectory - folder relative to `data/` directory
 * 
 * PRE1: relDirectory exists
*/
utils_ns.writeJsonWithTimestamp = async function (data, fileName, relDirectory) {
  const now = Date.now();
  await saveAnyTextfileAsync(relDirectory + `/${now}-${fileName}.json`, JSON.stringify(data));
}

/**
 * PARAMS
 * relDirectory - folder relative to `data/` directory
 * 
 * PRE1: relDirectory exists
*/
utils_ns.writeWithTimestamp = async function (text, fileNameWithExtension, relDirectory) {
  const now = Date.now();
  await saveAnyTextfileAsync(relDirectory + `/${now}-${fileNameWithExtension}`, text);
}

/**
 * relFilePath - path to file relative to `duoglot-root/data/`
*/
utils_ns.readFileFromDataDir = async function(relFilePath) {
  let fileContents = await errorWrapperPromiseAsync(anyfileAsync(relFilePath), error404Nullify);
  return fileContents;
}

/**
 * relFilePath - path to file relative to `duoglot-root/data/`
*/
utils_ns.writeFileToDataDir = async function(relFilePath, contents) {
  let result = await saveAnyTextfileAsync(relFilePath, contents);
  let resultDict = JSON.parse(result);
  return resultDict["result"] === "OK";
};

/**
 * NOTE very dangerous, invoke only when necessary
 * Creates dirs if don't exist
 * relFilePath - path to file relative to `duoglot-root/data/`
*/
utils_ns.writeFileToDataDirMakedirs = async function(relFilePath, contents) {
  let result = await saveAnyTextfileMakedirsAsync(relFilePath, contents);
  let resultDict = JSON.parse(result);
  return resultDict["result"] === "OK";
};
