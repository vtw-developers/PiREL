#!/bin/bash
set -e

if [ ! -d "/workspace" ]; then
  echo "This script is meant to be run inside devcontainer."
  echo "Please run main-dev-cli.sh to enter devcontainer command line first."
  exit
fi


if [[ $EUID > 0 ]]; then 
  echo "Please run as root/sudo (assuming root in container has access to the bind mount of docker.sock)"
  exit 1
fi

echo "========= installing frontend dependencies (node_modules) ========="

echo "--------- install monaco ---------"
cd /workspace/frontend/_common/monaco
npm install monaco-editor@0.31.1

echo "========= build docker images (using host docker) ========="
echo "--------- build docker images: thirdparty ---------"
cd /workspace/docker/thirdparty/
./build.sh
echo ""
echo "--------- build docker images: backendpybase ---------"
cd /workspace/docker/backendpybase/
./build.sh
echo ""
echo "--------- build docker images: backendtestingbase ---------"
cd /workspace/docker/backendtestingbase/
./build.sh
echo ""
echo "--------- build docker images: nginxbase ---------"
cd /workspace/docker/nginxbase/
./build.sh