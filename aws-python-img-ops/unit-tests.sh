#!/bin/bash

directories=`ls -d src/*`

for dir in $directories
do
    set -xe
    python3 -m unittest discover $dir
    set +xe
done