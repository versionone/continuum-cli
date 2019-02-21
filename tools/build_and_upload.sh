#!/usr/bin/env bash
VERSION=$1
BUILD=$2
BRANCH=$3

./build.sh
./upload.sh ${VERSION} ${BUILD} ${BRANCH}