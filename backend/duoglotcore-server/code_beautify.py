import jsbeautifier
import consts
import util_string


def beautify(language, code_str):
  # return code_str
  ret_code = None
  if language == "js":
    if True:# (code_str.find("function test()") < 0 or code_str.find("\\x") < 0):
      ret_code = jsbeautifier.beautify(code_str)
    else:
      if consts.DEBUG_VERBOSE > 0: print("# beautify WARNING: unsupported javascript code.")
      ret_code = code_str
  else:
    if consts.DEBUG_VERBOSE > 0: print("# beautify WARNING: unsupported language " + language)
    ret_code = code_str
  mapping_list = util_string.get_string_mapping_a(code_str, ret_code)
  return ret_code, mapping_list
