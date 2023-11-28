#!/bin/bash

for filename in cache/*.json; do
  cp $filename $filename.tmp &&
  jq . $filename.tmp > $filename &&
  rm $filename.tmp
done
