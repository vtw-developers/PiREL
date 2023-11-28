from setuptools import Extension, setup
from Cython.Build import cythonize
from consts import ENABLE_CYTHON_PROFILE


extensions = [
    Extension("grammar_expand", ["grammar_expand.py"]),
    Extension("grammar_dlmparser", ["grammar_dlmparser.py"]),
    Extension("grammar", ["grammar.py"]),
    Extension("util_traverse", ["util_traverse.py"]),
]


def read_text(fname):
  with open(fname, 'r') as f:
    return f.read()


def save_text(filepath, content):
  with open(filepath, 'w') as f:
    f.write(content)


def build_params():
  return f"ENABLE_CYTHON_PROFILE={ENABLE_CYTHON_PROFILE}"


force_rebuild = False
build_param_filepath = "./profiles/lasttime_build_params"
this_time_param = build_params()

try:
  force_rebuild = True if read_text(build_param_filepath) != this_time_param else False
except:
  pass

save_text(build_param_filepath, this_time_param)

print("[setup_build] force_rebuild: ", force_rebuild)
print("[setup_build] ENABLE_CYTHON_PROFILE: ", ENABLE_CYTHON_PROFILE)

setup(
    name="DuoGlotCoreServer",
    ext_modules=cythonize(
        extensions,
        language_level=3,
        annotate=True,
        force=force_rebuild,
        compiler_directives= {'profile': True} if ENABLE_CYTHON_PROFILE else {}
    ),
)
