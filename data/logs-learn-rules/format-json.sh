#!/bin/bash

for filename in $(find . -iname "*.json"); do
  cp $filename $filename.tmp &&
  jq . $filename.tmp > $filename &&
  rm $filename.tmp
done
