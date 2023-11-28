#!/bin/bash

for filename in ./*/*.json; do
  cp $filename $filename.tmp &&
  jq . $filename.tmp > $filename &&
  rm $filename.tmp
done

for filename in ./*.json; do
  cp $filename $filename.tmp &&
  jq . $filename.tmp > $filename &&
  rm $filename.tmp
done
