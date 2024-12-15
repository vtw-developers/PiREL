from typing import List, Callable
import util_hash
import grammar_expand


_translators_cache = {}


def get_translator(
  src_code: str,
  src_ast: list,
  src_ann: dict,
  srclang: str,
  tarlang: str,
  target_grammar: dict,
  transprog: str,
  _optional_dbg_info_save_func: Callable,
  slot_dedup_enabled: bool
) -> grammar_expand.TransSession:

  translator_key = util_hash.strings_sha256([src_code, transprog, srclang, tarlang, str(slot_dedup_enabled)])
  translator_info = None
  translator = None

  if translator_key in _translators_cache:
    translator_info = _translators_cache[translator_key]
    translator = translator_info["translator"]
    assert translator_info["source_code"] == src_code
    assert translator_info["trans_program_str"] == transprog
    assert translator_info["source_language"] == srclang
    assert translator_info["target_language"] == tarlang
  else:
    translator = grammar_expand.TransSession(
      src_code,  # str, source code of source program (comes with request object from frontend)
      src_ast,  # list[str, int, list[*]|str], AST of source program (generated with ast_parse.parse_text_dbg() function)
      src_ann,  # dict, boundaries of AST nodes (generated with ast_parse.parse_text_dbg() function)
      srclang,  # str, e.g. 'py' (comes with request object from frontend)
      tarlang,  # str, e.g. 'js' (comes with request object from frontend)
      target_grammar,  # dict, grammar for target program in some internal representation (tree-sitter grammar read from disk with json.loads())
      transprog,  # str, raw text of translation rules ~~~ (comes with request object from frontend)
      _optional_dbg_info_save_func,  # function, ?
      slot_dedup_enabled=slot_dedup_enabled  # bool, ? (depends on requese.choices type)
    )
    translator_info = {
      "source_code": src_code,
      "source_language": srclang,
      "target_language": tarlang,
      "trans_program_str": transprog,
      "translator": translator
    }
    _translators_cache[translator_key] = translator_info
  
  assert translator is not None and translator_info is not None

  return translator
