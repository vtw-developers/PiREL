# NOTE: execute this script from the parent folder
echo "--------------- history link --------------- "
echo http://127.0.0.1:9898/snakeviz/%2Fhome%2Fubuntu%2Fgit_repos%2FCodeSnart%2Fbackend%2Fduoglotcore-server%2Fprofiles%2Ftranslate.notopt-last.prof
echo http://127.0.0.1:9898/snakeviz/%2Fhome%2Fubuntu%2Fgit_repos%2FCodeSnart%2Fbackend%2Fduoglotcore-server%2Fprofiles%2Ftranslate.op1-delayelemlist.prof

echo "--------------- new link --------------- "
echo http://127.0.0.1:9898/snakeviz/%2Fhome%2Fubuntu%2Fgit_repos%2FCodeSnart%2Fbackend%2Fduoglotcore-server%2Fprofiles%2Ftranslate.prof
python3 -m snakeviz -p 9898 -s ./profiles/translate.prof
