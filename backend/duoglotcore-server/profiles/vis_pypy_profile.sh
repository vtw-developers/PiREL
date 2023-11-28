# NOTE: execute this script from the parent folder
./pypy3.8/bin/vmprofshow ./profiles/translate.dat | grep -v unknown | grep 'grammar\|util_\|ast_' | less -r