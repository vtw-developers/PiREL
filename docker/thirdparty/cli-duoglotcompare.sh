if [ -d "/workspace" ]; then
  echo "You are in devcontainer. This script is NOT meant to be run inside devcontainer."
  exit
fi

docker rm thirdp-duoglotcompare-container || true
docker run -it --name thirdp-duoglotcompare-container \
  --mount type=bind,source=$PWD/../../,target=/workspace \
  thirdp-duoglotcompare /bin/bash \