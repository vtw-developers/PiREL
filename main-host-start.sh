#!/bin/bash
if [ -d "/workspace" ]; then
  echo "This script is meant to be run outside of devcontainer."
  echo "Please run it directly on host."
  exit 1
fi

cd docker
./duoglot.start.sh