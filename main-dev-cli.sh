#!/bin/bash

if [ -d "/workspace" ]; then
  echo "You are already in devcontainer. This script is NOT meant to be run inside devcontainer."
  exit
fi

cd .devcontainer
docker build -t devprojbase -f ./Dockerfile .
docker rm devprojbase-container || true
WORKSPACEROOT=$(builtin cd "$PWD/../"; pwd)
docker run -it --name devprojbase-container \
  --mount type=bind,source=$PWD/../,target=/workspace \
  --user node \
  --env WORKSPACEROOT=$WORKSPACEROOT \
  --mount type=bind,source=/var/run/docker.sock,target=/var/run/docker.sock \
  -w /workspace devprojbase /bin/bash